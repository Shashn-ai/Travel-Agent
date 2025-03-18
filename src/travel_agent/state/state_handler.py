from typing import TypedDict, List, Optional
from typing_extensions import Annotated  # Add this line
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    messages: Annotated[list, add_messages]
    selected_package: dict
    user_preferences: dict

def initialize_state() -> State:
    return State(
        messages=[],
        selected_package={},
        user_preferences={}
    )


class FlightDetails(TypedDict):
    airline: str
    flight_number: str
    departure: str
    arrival: str
    price: float

class HotelDetails(TypedDict):
    name: str
    location: str
    check_in: str
    check_out: str
    price_per_night: float
    total_price: float

class ActivityDetails(TypedDict):
    name: str
    location: str
    date: str
    price: float

class BookingDetails(TypedDict):
    flight_reference: Optional[str]
    hotel_reference: Optional[str]
    activity_references: Optional[List[str]]

class State(TypedDict):
    messages: List[HumanMessage | AIMessage]
    flights: Optional[List[FlightDetails]]
    hotels: Optional[List[HotelDetails]]
    activities: Optional[List[ActivityDetails]]
    itinerary: Optional[str]
    booking_details: Optional[BookingDetails]

    # Ensures messages are updated across nodes
    _messages: List[HumanMessage | AIMessage] = add_messages
