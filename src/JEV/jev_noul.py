from typesafe_sdk import Noul,TypeSafeClient
import os 
import logging 
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = TypeSafeClient(api_key=os.getenv("TYPE_SAFE_API_KEY"), base_url=os.getenv("TYPE_SAFE_BASE_URL"))

state = "I was charged twice for my Udemy course purchase. Please fix this ASAP."

questions = {
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
    logger.info("Urgency Likelihood: %f", response.answers["Urgency"].noul * 100)

    
    logger.info("--- Metadata Logs ---")
    logger.info("Urgency Likelihood (Percentage): %f", response.answers["Urgency"].noul * 100)
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