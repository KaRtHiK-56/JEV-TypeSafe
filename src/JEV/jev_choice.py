from typesafe_sdk import Choice,TypeSafeClient
import os
import logging 
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

client = TypeSafeClient(api_key=os.getenv("TYPESAFE_API_KEY"),base_url=os.getenv("TYPESAFE_BASE_URL"))

state = "I was charged twice for my Udemy course purchase. Please fix this ASAP."

questions = {
    "Department": Choice(
            instructions="Which department should this ticket be routed to?",
            criteria={"Sales": "Sales department for product inquiries", "Support": "Support department for technical issues", "Billing": "Billing department for payment issues", "Technical": "Technical department for system issues"},
        )
}

try:
    response = client.system_one(model=os.getenv("TYPESAFE_MODEL"), questions=questions, state=state)
    logger.info("=" * 50)
    logger.info("Complete JEV Response: %s", response)
    logger.info("=" * 50)
    logger.info("")
    
    logger.info("--- Classification Summary ---")
    logger.info("Department Decision: %s", response.answers["Department"].choice)
    
    logger.info("--- Metadata Logs ---")
    logger.info("Department Confidence: %f", response.answers["Department"].confidence * 100)
    logger.info("Full Department Probabilities: %s", response.answers["Department"].probabilities)

    logger.info("")

    PRICE_PER_MILLION_INPUT = 0.042
    
    in_tokens = response.usage.input_tokens
    out_tokens = response.usage.output_tokens
    
    calculated_cost = (in_tokens / 1_000_000) * PRICE_PER_MILLION_INPUT

    logger.info("--- Resource & Token Billing ---")
    logger.info("Input Volume: %d tokens", in_tokens)
    logger.info("Output Volume: %d tokens (Billed at $0.00)", out_tokens)
    logger.info("Calculated Cost: $%s", f"{calculated_cost:.8f}") 
    logger.info("")

except Exception as e:
    tb.print_exc()
    tb_info = tb.extract_tb(sys.exc_info()[2])[-1]
    filename = tb_info.filename
    line_number = tb_info.lineno
    
    logger.error("Error in %s at line %s: %s", filename, line_number, e)
    raise