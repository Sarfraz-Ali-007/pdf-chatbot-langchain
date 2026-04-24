import os

GROQ_API_KEY = os.getenv("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")
#COHERE_API_KEY = os.getenv("okwfI0RLiqXZlhNfjtL9TNevA0tqyMMAlOhZxVNg")

from dotenv import load_dotenv
import os

load_dotenv()

COHERE_API_KEY=os.getenv("okwfI0RLiqXZlhNfjtL9TNevA0tqyMMAlOhZxVNg")

print("Loaded API KEY:", COHERE_API_KEY)