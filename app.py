import streamlit as st
from src.travel_agent.ui.streamlitui.loadui import initialize_state
from src.travel_agent.ui.streamlitui.display_results import display_packages, display_comparison, display_booking_confirmation
from src.travel_agent.graph.graph import travel_agent_graph

# Initialize session state if not already
if 'state' not in st.session_state:
    st.session_state['state'] = initialize_state()

# App title and description
st.title("AI Travel Agent 🚀")
st.write("Find the best travel deals and plan your perfect trip.")

# User input for travel request
user_input = st.text_input("What are you looking for?", "Find me travel packages for Bali for 5 days")
if st.button("Search"):
    with st.spinner("Searching for the best deals..."):
        st.session_state['state'] = travel_agent_graph(st.session_state['state'], user_input)

# Show results if available
if 'packages' in st.session_state['state'] and st.session_state['state']['packages']:
    display_packages(st.session_state['state']['packages'])

# Compare selected packages
if st.session_state['state']['compared_packages']:
    display_comparison(st.session_state['state']['compared_packages'])

# Booking confirmation
if st.session_state['state']['booking_details']:
    display_booking_confirmation(st.session_state['state']['booking_details'])

# Run the app
if __name__ == "__main__":
    st.experimental_rerun()
