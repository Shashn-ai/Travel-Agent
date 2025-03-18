from src.travel_agent.tools.activities_tool import suggest_activities
from src.travel_agent.state.state_handler import State

def activity_suggestions_node(state: State) -> State:
    """
    Node to suggest activities based on the itinerary, location, and preferences.
    """
    # Extract location and preferences from the state
    location = state.get('destination')
    preferences = state.get('preferences', {})

    # Call the activity suggestion tool
    activity_suggestions = suggest_activities(location, preferences)

    # Update the state with activity suggestions
    state['activity_suggestions'] = activity_suggestions

    return state