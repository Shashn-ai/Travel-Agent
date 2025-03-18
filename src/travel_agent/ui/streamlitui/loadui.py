from typing import TypedDict, Annotated, List, Optional
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    messages: Annotated[list, add_messages]
    selected_package: dict
    user_preferences: dict
    compared_packages: List[dict]  # For package comparison
    filters: dict  # Filters like budget, hotel type, etc.
    sort_by: str  # Sorting preferences
    booking_details: Optional[dict]  # Store booking details

def initialize_state() -> State:
    return State(
        messages=[],
        selected_package={},
        user_preferences={},
        compared_packages=[],
        filters={},
        sort_by="price",  # Default sorting by price
        booking_details=None
    )

def apply_filters(packages: List[dict], filters: dict) -> List[dict]:
    """Applies filters to the list of travel packages."""
    filtered_packages = [pkg for pkg in packages if all(
        str(pkg.get(key, '')).lower() == str(value).lower() for key, value in filters.items()
    )]
    return filtered_packages

def sort_packages(packages: List[dict], sort_by: str) -> List[dict]:
    """Sorts the list of travel packages based on user preference."""
    return sorted(packages, key=lambda pkg: pkg.get(sort_by, float('inf')))

def compare_packages(package_list: List[dict]) -> List[dict]:
    """Compares selected travel packages and returns a comparison."""
    comparison = [{key: pkg.get(key) for key in ('name', 'price', 'hotel', 'flights')} for pkg in package_list]
    return comparison

def book_package(selected_package: dict) -> dict:
    """Handles booking of the selected package."""
    booking_confirmation = {
        "status": "confirmed",
        "package": selected_package,
        "message": f"Your package to {selected_package.get('destination')} has been booked successfully!"
    }
    return booking_confirmation
