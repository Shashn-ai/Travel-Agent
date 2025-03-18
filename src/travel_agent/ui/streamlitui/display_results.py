import streamlit as st
from typing import List, Dict

def display_package_card(package: Dict, index: int):
    """Displays a travel package card with key details."""
    st.markdown(f"### {package.get('name', 'Package')} - ${package.get('price', 'N/A')}")
    st.write(f"**Destination:** {package.get('destination', 'N/A')}")
    st.write(f"**Hotel:** {package.get('hotel', 'N/A')}")
    st.write(f"**Flights:** {package.get('flights', 'N/A')}")
    st.write(f"**Activities:** {', '.join(package.get('activities', []))}")
    
    if st.button(f"Select Package {index + 1}", key=f"select_{index}"):
        st.session_state.selected_package = package

def display_packages(packages: List[Dict]):
    """Displays all available travel packages."""
    st.title("Available Travel Packages")
    for index, package in enumerate(packages):
        with st.container():
            display_package_card(package, index)
            st.markdown("---")

def display_comparison(compared_packages: List[Dict]):
    """Displays a side-by-side comparison of selected packages."""
    st.title("Compare Packages")
    if not compared_packages:
        st.write("No packages selected for comparison.")
        return
    
    col1, col2, col3 = st.columns(3)
    for i, package in enumerate(compared_packages):
        with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
            display_package_card(package, i)

def display_booking_confirmation():
    """Displays booking confirmation after user books a package."""
    if "selected_package" in st.session_state and st.session_state.selected_package:
        st.success(f"Your package to {st.session_state.selected_package['destination']} has been booked successfully!")
        st.write(f"**Package:** {st.session_state.selected_package['name']}")
        st.write(f"**Price:** ${st.session_state.selected_package['price']}")
        st.write("Thank you for booking with us! Safe travels! 🌍")
