from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
from typing import Optional, List

class ActivitiesInput(BaseModel):
    destination: str = Field(..., description="Destination city or location")
    interests: Optional[List[str]] = Field(default=None, description="List of interests like adventure, relaxation, sightseeing, etc.")
    budget: Optional[float] = Field(default=None, description="Budget for activities in USD")
    travel_dates: Optional[List[str]] = Field(default=None, description="Travel dates for activity availability check")

class ActivitiesInputSchema(BaseModel):
    params: ActivitiesInput

@tool(args_schema=ActivitiesInputSchema)
def activities_finder(params: ActivitiesInput):
    """
    Find activities based on destination, interests, budget, and travel dates.
    Returns:
        list: Suggested activities.
    """
    # Simulated activity data (Replace with actual API call or DB lookup)
    activities_db = [
        {"destination": "Bali", "name": "Beach Surfing", "interest": "adventure", "price": 50},
        {"destination": "Bali", "name": "Temple Tour", "interest": "sightseeing", "price": 30},
        {"destination": "Bali", "name": "Spa Relaxation", "interest": "relaxation", "price": 80},
    ]

    # Filtering activities based on inputs
    filtered_activities = [
        activity for activity in activities_db
        if activity['destination'].lower() == params.destination.lower()
        and (not params.interests or activity['interest'] in params.interests)
        and (not params.budget or activity['price'] <= params.budget)
    ]

    return filtered_activities
