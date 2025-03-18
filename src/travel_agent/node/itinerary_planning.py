from src.travel_agent.tools.itinerary_tool import generate_itinerary

def itinerary_planning_node(state):
    """
    Node for planning a travel itinerary based on flight and hotel details.
    """
    flight_details = state.get("flight_details", {})
    hotel_details = state.get("hotel_details", {})

    # Generate itinerary based on flight and hotel details
    itinerary = generate_itinerary(flight_details, hotel_details)
    
    # Update state with itinerary details
    state["itinerary"] = itinerary
    return state