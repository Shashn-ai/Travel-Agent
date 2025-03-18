from src.travel_agent.tools.hotels_finder import hotels_finder

def hotel_search_node(state):
    """
    Node to handle hotel search in the travel agent workflow.
    """
    print("Hotel Search Node: Initiating hotel search...")
    
    # Extract hotel search parameters from the state
    destination = state.get('destination')
    check_in_date = state.get('check_in_date')
    check_out_date = state.get('check_out_date')
    adults = state.get('adults', 1)
    children = state.get('children', 0)
    budget = state.get('budget')
    preferences = state.get('preferences', [])

    # Call the hotel finder tool
    hotel_search_params = {
        'destination': destination,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'adults': adults,
        'children': children,
        'budget': budget,
        'preferences': preferences
    }
    hotels = hotels_finder(hotel_search_params)

    print(f"Hotel Search Node: Found {len(hotels)} hotels.")

    # Update the state with the hotel search results
    state['hotel_results'] = hotels
    return state