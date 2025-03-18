from src.travel_agent.tools.flights_finder import flights_finder
from src.travel_agent.state.state_handler import State

def flight_search_node(state: State) -> State:
    """
    Node for searching flights.
    """
    # Extract parameters from state
    departure = state.get("departure_airport")
    arrival = state.get("arrival_airport")
    outbound_date = state.get("outbound_date")
    return_date = state.get("return_date")
    adults = state.get("adults", 1)
    children = state.get("children", 0)
    infants_in_seat = state.get("infants_in_seat", 0)
    infants_on_lap = state.get("infants_on_lap", 0)

    # Call flight finder tool
    flight_results = flights_finder(
        departure_airport=departure,
        arrival_airport=arrival,
        outbound_date=outbound_date,
        return_date=return_date,
        adults=adults,
        children=children,
        infants_in_seat=infants_in_seat,
        infants_on_lap=infants_on_lap
    )

    # Update state with flight results
    state["flight_results"] = flight_results

    return state
