from langgraph.graph import StateGraph
from src.travel_agent.state.state_handler import State
from src.travel_agent.node.flight_search import flight_search_node
from src.travel_agent.node.hotel_search import hotel_search_node
from src.travel_agent.node.itinerary_planning import itinerary_planning_node
from src.travel_agent.node.activity_suggestions import activity_suggestions_node
from src.travel_agent.node.booking_confirmation import booking_confirmation_node

# Initialize the graph with the state
travel_agent_graph = StateGraph(State)

# Add nodes to the graph
travel_agent_graph.add_node("flight_search", flight_search_node)
travel_agent_graph.add_node("hotel_search", hotel_search_node)
travel_agent_graph.add_node("itinerary_planning", itinerary_planning_node)
travel_agent_graph.add_node("activity_suggestions", activity_suggestions_node)
travel_agent_graph.add_node("booking_confirmation", booking_confirmation_node)

# Set entry point for the graph
travel_agent_graph.set_entry_point("flight_search")

# Define edges between nodes
travel_agent_graph.add_edge("flight_search", "hotel_search")
travel_agent_graph.add_edge("hotel_search", "itinerary_planning")
travel_agent_graph.add_edge("itinerary_planning", "activity_suggestions")
travel_agent_graph.add_edge("activity_suggestions", "booking_confirmation")

# Compile the graph
travel_agent_graph = travel_agent_graph.compile()