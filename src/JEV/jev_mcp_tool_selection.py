from typesafe_sdk import Noul,Choice,Score,TypeSafeClient
import os 
import logging
from dotenv import load_dotenv
import traceback as tb
import sys
from utils import MCP_SERVERS
import time

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

load_dotenv()

client = TypeSafeClient(api_key=os.getenv("TYPE_SAFE_API_KEY"),base_url=os.getenv("TYPE_SAFE_BASE_URL"))

user_question = input("Enter the state to take a decison: ")

logger.info(f"Selected state: {user_question}")

state ={
    "user_question": user_question,
    "available_tools": list(MCP_SERVERS.keys())
}

questions = {
   "is_mcp_routable": Noul(
    instructions=(
        "Can the user's request be fulfilled using one of the "
        "MCP servers and tools available to the application?"
    ),
    criteria={
        "true": (
            "At least one available MCP server provides a tool "
            "capable of fulfilling the user's request."
        ),
        "false": (
            "None of the available MCP servers provide a tool "
            "that can fulfill the user's request."
        ),
    },
),

    "mcp_server": Choice(
        instructions="Which MCP server is the most appropriate for the user query?",
        criteria={
            name: details["description"]
            for name, details in MCP_SERVERS.items()
        },
    ),
}

try:
    response = client.system_one(model=os.getenv("TYPESAFE_MODEL"), questions=questions, state=state)
    logger.info("=" * 50)
    logger.info("Complete JEV Response: %s", response)
    logger.info("=" * 50)
    logger.info("")

    is_mcp = response.answers["is_mcp_routable"].noul
    
    logger.info("Is MCP routable: %.2f", is_mcp)

    selected_server = response.answers["mcp_server"].choice
    server_confidence = response.answers["mcp_server"].confidence
    server_probabilities = response.answers["mcp_server"].probabilities
    is_mcp_routable_noul = response.answers["is_mcp_routable"].noul

    logger.info(
    "Selected server: %s | Confidence: %.2f | Probabilities: %s | MCP Routable Noul: %.2f", 
    selected_server, 
    server_confidence, 
    server_probabilities,
    is_mcp_routable_noul
)

    if is_mcp < 0.5:
        logger.info("Not an MCP routable problem.")
        sys.exit(0)


    CONFIDENCE_THRESHOLD = 0.70

    if server_confidence < CONFIDENCE_THRESHOLD:
        logger.warning("⚠ MCP routing is uncertain")
        logger.warning("⚠ Server selection is only %.0f%% confident", server_confidence * 100)
        logger.warning("→ Do not execute automatically")

        # Detailed contextual logging for debugging the pipeline state
        logger.info("Contextual Pipeline State:")
        logger.info("  - Evaluated Server: %s", selected_server)
        logger.info("  - Raw Confidence: %.4f", server_confidence)
        logger.info("  - MCP Routable Noul Score: %.4f", is_mcp_routable_noul)
        logger.info("  - Complete Distribution Probabilities: %s", server_probabilities)
    
    else:
        logger.info("MCP routing is confident enough to execute automatically")

        selected_server = response.answers["mcp_server"].choice
        logger.info("Selected server: %s", selected_server)

        server_info = MCP_SERVERS.get(selected_server)
        logger.info("Server info: %s", server_info)

        if not server_info:
            raise ValueError(f"Unknown MCP server: {selected_server}")

        available_tools = server_info["tools"]
        logger.info("Available tools: %s", available_tools)

        state = {
            "user_question": user_question,
            "selected_server": selected_server,
            "available_tools": available_tools
        }

        questions = {
        "mcp_tool": Choice(
        instructions=(
            f"Which single tool from the {selected_server} MCP server is most appropriate for fulfilling the user's request?"
        ),
        criteria=available_tools,
    )
    }

    try:
        time.sleep(60)

        tool_response = client.system_one(
            model=os.getenv("TYPESAFE_MODEL"),
            questions=questions,
            state=state,
        )

        logger.info("Tool response: %s", tool_response)

        selected_tool = tool_response.answers["mcp_tool"].choice
        tool_confidence = tool_response.answers["mcp_tool"].confidence
        tool_probabilities = tool_response.answers["mcp_tool"].probabilities

        logger.info(
            "Selected tool: %s | Confidence: %.2f | Probabilities: %s",
            selected_tool,
            tool_confidence,
            tool_probabilities,
        )

        time.sleep(60)

        score_questions = {
        "selection_quality": Score(
        instructions=(
            "How appropriate is the selected MCP server and "
            "selected MCP tool for fulfilling the user's request?"
        ),
        criteria=[
            "Completely inappropriate",
            "Mostly inappropriate",
            "Partially appropriate",
            "Appropriate",
            "Highly appropriate",
        ],
    )
        }

        try:
            score_response = client.system_one(
                model=os.getenv("TYPESAFE_MODEL"),
                questions=score_questions,
                state=state,
            )

            logger.info("Score response: %s", score_response)

            selection_quality = score_response.answers["selection_quality"].score
            closest_index = round(selection_quality)
            readable_selection_quality = score_response.answers["selection_quality"].legend.get(closest_index) or score_response.answers["selection_quality"].legend.get(str(closest_index), "Unknown")
            selection_quality_confidence = score_response.answers["selection_quality"].confidence * 100
            
            logger.info(
                "Selection quality: %s | Confidence: %.2f",
                readable_selection_quality,
                 selection_quality_confidence,
            )

            selection_quality_probabilities = (
                score_response.answers["selection_quality"].probabilities
            )

            selection_quality_legend = (
                score_response.answers["selection_quality"].legend
            )
            logger.info(
                "Score probabilities: %s",
                selection_quality_probabilities,
            )

            logger.info(
                "Score legend: %s",
                selection_quality_legend,
            )
        except Exception as e:
            logger.error(f"Error in JEV 3 processing: {e}")
            logger.error(f"Traceback: {tb.format_exc()}")
            sys.exit(1)


    except Exception as e:
        logger.error(f"Error in JEV 2 processing: {e}")
        logger.error(f"Traceback: {tb.format_exc()}")

    
except Exception as e:
    logger.error(f"Error in JEV 1 processing: {e}")
    logger.error(f"Traceback: {tb.format_exc()}")
    sys.exit(1)