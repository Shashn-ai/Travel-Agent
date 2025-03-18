from src.travel_agent.state.state_handler import State
from typing import Dict

def booking_confirmation_node(state: State) -> State:
    """
    Node to handle booking confirmation for flights, hotels, and activities.
    """
    # Extract booking details from the state
    flight_details = state.get("flight_details", {})
    hotel_details = state.get("hotel_details", {})
    activities = state.get("activities", [])

    # Simulate booking confirmation logic
    booking_confirmation = {
        "flight": flight_details.get("booking_reference", "Not Booked"),
        "hotel": hotel_details.get("booking_reference", "Not Booked"),
        "activities": [activity.get("booking_reference", "Not Booked") for activity in activities]
    }

    # Update the state with booking confirmation
    state["booking_confirmation"] = booking_confirmation
    return state