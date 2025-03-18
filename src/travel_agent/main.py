import streamlit as st
from travel_agent.graph.graph import travel_agent_graph
from src.travel_agent.ui.streamlitui.loadui import display_package_view
from travel_agent.state.state_handler import StateHandler

def main():
    st.set_page_config(page_title="AI Travel Agent", layout="wide")
    st.title("🌍 AI Travel Agent")

    # Initialize State
    state_handler = StateHandler()
    state = state_handler.get_state()

    # Initialize Graph
    travel_agent_graph = travel_agent_graph()

    # User Input
    user_query = st.text_input("What are you looking for?", "Find me travel packages for Bali for 5 days")

    if st.button("Search"):
        with st.spinner("Finding the best travel deals..."):
            result = travel_agent_graph.run(user_query)
            state_handler.update_state(result)

    # Show Results
    if state.get('packages'):
        travel_agent_graph(state)
    else:
        st.info("No packages found. Try refining your search.")

if __name__ == "__main__":
    main()
