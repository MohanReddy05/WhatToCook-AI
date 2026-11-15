
from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
from typing import Dict, Any
import os

load_dotenv()

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """
    Search the internet for authentic cooking recipes.
    Returns recipe titles, URLs, and search result content.
    """
    try:
        result = tavily_client.search(
            query,
            max_results=5
        )
        return result
    except Exception as e:
        return {"error": str(e)}
