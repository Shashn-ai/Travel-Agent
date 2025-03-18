🌐 High-Level Workflow:
User Input:

The app asks for basic travel details like:

Departure and arrival airports

Travel dates (outbound and return)

Number of adults and children

Destination city for hotels

Preferences for activities

Travel Planning Steps:
The app uses a LangGraph workflow to manage each step of the travel planning process. The graph looks like this:

Flight Search: Finds flights based on user inputs.

Hotel Search: Looks for hotels near the destination.

Itinerary Planning: Creates a day-by-day plan of activities and travel.

Activity Suggestions: Recommends activities at the destination.

Booking Confirmation: Final step to confirm bookings and show a summary of the trip.

AI Assistance:

It uses ChatGroq LLM (Large Language Model) to help generate itinerary suggestions, activity ideas, and handle the conversation flow.

SerpApi is used to fetch real-time flight and hotel data from Google Flights and Google Hotels.

User Interface:

Built with Streamlit to create a clean web interface for users to input their travel details and view results.

Results for flights, hotels, and itineraries are displayed in the app.

State Management:

The app maintains a state object to track the user’s journey through the planning process.

Each step updates the state, passing data (like flight and hotel results) to the next step.

