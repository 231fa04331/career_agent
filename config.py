import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

# Load environment variables from .env
load_dotenv()

# Read API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Validate API Keys
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in .env")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

# Initialize Tavily Client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)