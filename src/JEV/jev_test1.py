from typesafe_sdk import Noul,Choice,Score,TypeSafeClient
from dotenv import load_dotenv
import os
import sys
import logging
import traceback as tb

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

client = TypeSafeClient(api_key=os.getenv("TYPE_SAFE_API_KEY"), base_url=os.getenv("TYPE_SAFE_BASE_URL"))

state = "I was charged twice for my Udemy course purchase. Please fix this ASAP."

questions = {
    "Category":Choice(
        instructions="Choose the most appropriate category for the issue",
        criteria={"Billing": "Billing related issues", "Technical": "Technical issues", "Account": "Account related issues", "Other": "Other issues"}
    ),
    "Severity":Score(
        instructions="Rate and state the severity of the issue from 1 to 10",
         criteria=["Low", "Medium", "High"]
    ),
    "Urgency": Noul(
            instructions="Does the message convey urgency or time-sensitivity",
        )
}

try:
    response = client.system_one(model=os.getenv("TYPESAFE_MODEL"), questions=questions, state=state)
    logger.info("=" * 50)
    logger.info("Complete JEV Response: %s", response)
    logger.info("=" * 50)
    logger.info("")
    
    logger.info("--- Classification Summary ---")
    logger.info("Category Decision: %s", response.answers["Category"].choice)
    logger.info("Severity Value: %f", response.answers["Severity"].score)
    logger.info("Urgency Likelihood: %f", response.answers["Urgency"].noul * 100)

    
    logger.info("--- Metadata Logs ---")
    logger.info("Category Confidence: %f", response.answers["Category"].confidence * 100)
    logger.info("Full Category Probabilities: %s", response.answers["Category"].probabilities)
    logger.info("Severity Confidence: %f", response.answers["Severity"].confidence * 100)
    logger.info("Full Severity Probabilities: %s", response.answers["Severity"].probabilities)

    severity_obj = response.answers["Severity"]
  
    closest_index = round(severity_obj.score) 
    readable_severity = severity_obj.legend.get(closest_index) or severity_obj.legend.get(str(closest_index), "Unknown")

    logger.info("Calculated Severity Bucket: %s", readable_severity)
    logger.info("Urgency Likelihood (Percentage): %f", response.answers["Urgency"].noul * 100)

    logger.info("")

    PRICE_PER_MILLION_INPUT = 0.042
    
    # Read values from the Pydantic usage object directly
    in_tokens = response.usage.input_tokens
    out_tokens = response.usage.output_tokens
    
    # Financial calculation step
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
