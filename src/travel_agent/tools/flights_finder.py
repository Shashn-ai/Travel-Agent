from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from serpapi import GoogleSearch  # Import GoogleSearch, not serpapi directly
import os
from dotenv import load_dotenv

load_dotenv()

class FlightsInput(BaseModel):
    departure_airport: Optional[str] = Field(description='Departure airport code (IATA)')
    arrival_airport: Optional[str] = Field(description='Arrival airport code (IATA)')
    outbound_date: Optional[str] = Field(description='Outbound date in YYYY-MM-DD format')
    return_date: Optional[str] = Field(None, description='Return date in YYYY-MM-DD format (optional)')
    adults: Optional[int] = Field(1, description='Number of adults (default: 1)')
    children: Optional[int] = Field(0, description='Number of children (default: 0)')

class FlightsInputSchema(BaseModel):
    params: FlightsInput

@tool(args_schema=FlightsInputSchema)
def flights_finder(params: FlightsInput):
    """
    Find flights using the Google Flights engine.
    """
    serpapi_key = os.getenv('SERPAPI_KEY')
    if not serpapi_key:
        return "Missing SerpAPI key. Please set the SERPAPI_KEY environment variable."

    search_params = {
        'api_key': serpapi_key,
        'engine': 'google_flights',
        'hl': 'en',
        'gl': 'us',
        'departure_id': params.departure_airport,
        'arrival_id': params.arrival_airport,
        'outbound_date': params.outbound_date,
        'return_date': params.return_date,
        'adults': params.adults,
        'children': params.children,
        'currency': 'USD'
    }

    try:
        search = GoogleSearch(search_params)  # Correct usage
        results = search.get_dict()
        return results.get('best_flights', [])
    except Exception as e:
        return str(e)