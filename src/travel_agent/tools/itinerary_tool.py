from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
from typing import Optional, List

class ItineraryInput(BaseModel):
    destination: str = Field(..., description="Destination for the trip")
    flight_details: dict = Field(..., description="Flight details including departure, arrival times")
    hotel_details: dict = Field(..., description="Hotel details including check-in and check-out times")
    preferences: Optional[List[str]] = Field(None, description="User preferences for activities")

@tool(args_schema=ItineraryInput)
def itinerary_planner(destination: str, flight_details: dict, hotel_details: dict, preferences: Optional[List[str]] = None):
    """
    Generates a personalized travel itinerary based on flights, hotel, and user preferences.
    """
    itinerary = []

    # Extract flight info
    arrival_time = flight_details.get('arrival_time', '14:00')
    departure_time = flight_details.get('departure_time', '12:00')

    # Extract hotel info
    check_in_time = hotel_details.get('check_in_time', '15:00')
    check_out_time = hotel_details.get('check_out_time', '11:00')

    # Day 1 - Arrival and Hotel Check-in
    itinerary.append(f"Arrive in {destination} at {arrival_time}.")
    itinerary.append(f"Check-in at the hotel by {check_in_time}.")
    itinerary.append("Relax and explore nearby attractions or enjoy a welcome drink.")

    # Middle days - Activities based on preferences
    for i in range(2, len(preferences) + 1):
        itinerary.append(f"Day {i}: {preferences[i - 2]}")

    # Last day - Check-out and Departure
    itinerary.append(f"Check-out from the hotel by {check_out_time}.")
    itinerary.append(f"Depart from {destination} at {departure_time}.")

    return "\n".join(itinerary)
