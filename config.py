########  GENERAL APP INFORMATION  ##############

APP_TITLE = None
# APP_TITLE = "SC4x | Week 10 | Case Study | ML 1"

APP_INTRO = None
# APP_INTRO = """This app uses an AI API (OpenAI, Gemini, or Claude) to provide feedback on an open response question about machine learning: Do we need all of the features for a classification model? If not, which features would you exclude?"""

APP_HOW_IT_WORKS = None
# APP_HOW_IT_WORKS = """ """

SHARED_ASSET = {}
# SHARED_ASSET = {
#     "name":"NAME",
#     "path":"FILE.pdf",
#     "button_text":"Read this PDF first"
# }

HTML_BUTTON = {}

COMPLETION_MESSAGE = "Thank you for submitting a response!"
COMPLETION_CELEBRATION = False

SCORING_DEBUG_MODE = False

 ####### PHASES INFORMATION #########

PHASES = {
    "attempt1": {
        "type": "text_area",
        "height": 200,
        "label": """Which features would you exclude (if any) for a classification model?""",
        "instructions": """ The students are using machine learning for a classification problem to predict if an order may be delivered late or not. The features in the dataset they have available include: order_id, product_id, order_status, order_year, order_month, order_day_of_week, customer_city, customer_state, item_qty, price, freight_value, product_category_name, product_weight_g, product_length_cm, product_height_cm, product_width_cm, seller_city, and seller_state. They are asked if would exclude any of these features for a classification model. order_id and product_id would not useful for a model. The customer and seller location features (customer_city, customer_state, seller_city, and seller_state) provide similar information and they may only need one for customer and seller each. For some models, city make have too many categories and reduce performance, so state may be a more effective feature. They also may not need all of the dimensional features (product_weight_g, product_length_cm, product_height_cm, product_width_cm), and could focus on product_weight_g. They may create a composite feature for volume (e.g., product_length_cm x product_height_cm x product_width_cm). Please evaluate the response from the student and provide feedback based on some of these suggestions. """,
        "value": " ",
        "scored_phase": False,
        "rubric": """
            None
        """,
        "minimum_score": 2
    },
}

######## AI CONFIGURATION #############

########## AI ASSISTANT CONFIGURATION #######
ASSISTANT_NAME = "sc4x_wk10_CaseStudy_ML"
ASSISTANT_INSTRUCTIONS = """ You are an expert in machine learning and overseeing a course where students are learning the basics of machine learning. """

LLM_CONFIGURATION = {
    "gpt-4-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4-turbo",
        "temperature":0,
        "price_per_1k_prompt_tokens":.01,
        "price_per_1k_completion_tokens": .03
    },
    "gpt-4o":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-4o",
        "temperature":0,
        "price_per_1k_prompt_tokens":.0025,
        "price_per_1k_completion_tokens": .010
    },
    "gpt-3.5-turbo":{
        "name":ASSISTANT_NAME,
        "instructions": ASSISTANT_INSTRUCTIONS,
        "tools":[{"type":"file_search"}],
        "model":"gpt-3.5-turbo-0125",
        "temperature":0,
        "price_per_1k_prompt_tokens":0.0005,
        "price_per_1k_completion_tokens": 0.0015
    }
}

ASSISTANT_THREAD = ""
ASSISTANT_ID_FILE = "assistant_id.txt"