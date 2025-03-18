from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from serpapi import GoogleSearch  # Import GoogleSearch directly
from src.travel_agent.ui.streamlitui.loadui import load_streamlit_ui

from dotenv import load_dotenv
import os

load_dotenv()

class HotelsInput(BaseModel):
    destination: str = Field(description="Destination city or location for hotel search")
    check_in_date: str = Field(description="Check-in date (YYYY-MM-DD)")
    check_out_date: str = Field(description="Check-out date (YYYY-MM-DD)")
    adults: Optional[int] = Field(1, description="Number of adults (default: 1)")
    children: Optional[int] = Field(0, description="Number of children (default: 0)")
    rooms: Optional[int] = Field(1, description="Number of rooms (default: 1)")
    currency: Optional[str] = Field("USD", description="Currency for pricing (default: USD)")

class HotelsInputSchema(BaseModel):
    params: HotelsInput

@tool(args_schema=HotelsInputSchema)
def hotels_finder(params: HotelsInput):
    """
    Find hotels using the Google Hotels engine.
    
    Returns:
        dict: Hotel search results.
    """
    serpapi_key = load_streamlit_ui('SERPAPI_KEY')
    if not serpapi_key:
        return {"error": "Missing SerpAPI key. Please set the SERPAPI_KEY."}

    search_params = {
        "api_key": serpapi_key,
        "engine": "google_hotels",
        "q": params.destination,
        "check_in_date": params.check_in_date,
        "check_out_date": params.check_out_date,
        "adults": params.adults,
        "children": params.children,
        "rooms": params.rooms,
        "currency": params.currency
    }

    try:
        search = GoogleSearch(search_params)  # Correct usage
        results = search.get_dict().get("hotels", [])
    except Exception as e:
        results = {"error": str(e)}
    
    return results