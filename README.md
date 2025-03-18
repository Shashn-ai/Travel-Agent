🧳 Travel Agent AI

Welcome to the Travel Agent AI — your smart travel companion! 🌍 This app helps you find flights, hotels, plan itineraries, get activity suggestions, and confirm bookings, all in one place.

📌 Features

✈️ Flight Search: Find the best flights with just a few details.

🏨 Hotel Search: Get hotel recommendations tailored to your preferences.

📅 Itinerary Planning: Create detailed itineraries for your trips.

🎉 Activity Suggestions: Discover fun activities at your destination.

✅ Booking Confirmation: Get a summary of your bookings.

🏗️ Tech Stack

Python 🐍

LangGraph for workflow orchestration

Streamlit for the user interface

ChatGroq for LLM-powered responses

SerpAPI for fetching real-time travel data

⚙️ Setup Instructions

Clone the repository:

 git clone https://github.com/Shashn-ai/Travel-Agent.git

Navigate into the project directory:

 cd Travel-Agent

Create a virtual environment and activate it:

 python -m venv venv
 source venv/bin/activate  # For Linux/macOS
 venv\Scripts\activate     # For Windows

Install dependencies:

 pip install -r requirements.txt

Add your API keys:

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key
SERPAPI_KEY=your_serpapi_key

Run the app:

 streamlit run app.py

📂 Project Structure

Travel-Agent/
├── src/
│   ├── travel_agent/
│   │   ├── graph/
│   │   ├── node/
│   │   ├── tools/
│   │   ├── ui/
│   │   └── state/
│   └── app.py
├── .env
├── requirements.txt
└── README.md

📝 How to Use

Enter your travel details in the app.

Click through the steps: flight search → hotel search → itinerary planning → activity suggestions → booking confirmation.

Review your trip summary and enjoy your travels! 🌟

💬 Contributing

Want to improve Travel Agent AI? Contributions are welcome!

Fork the repository.

Create a new branch:

 git checkout -b feature/new-feature

Commit your changes and push to your branch.

Open a Pull Request.

📧 Contact

GitHub: Shashn-ai

Email: your.email@example.com

Happy Traveling! 🌍✨

