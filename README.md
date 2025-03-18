# 🧳 **Travel Agent AI**

Welcome to the **Travel Agent AI** — your smart travel companion! 🌍 This app helps you find flights, hotels, plan itineraries, get activity suggestions, and confirm bookings, all in one place.

---

## 📌 **Features**

- ✈️ **Flight Search:** Find the best flights with just a few details.
- 🏨 **Hotel Search:** Get hotel recommendations tailored to your preferences.
- 📅 **Itinerary Planning:** Create detailed itineraries for your trips.
- 🎉 **Activity Suggestions:** Discover fun activities at your destination.
- ✅ **Booking Confirmation:** Get a summary of your bookings.

---

## 🏗️ **Tech Stack**

- **Python** 🐍
- **LangGraph** for workflow orchestration
- **Streamlit** for the user interface
- **ChatGroq** for LLM-powered responses
- **SerpAPI** for fetching real-time travel data

---

## ⚙️ **Setup Instructions**

1. Clone the repository:
```bash
 git clone https://github.com/Shashn-ai/Travel-Agent.git
```
2. Navigate into the project directory:
```bash
 cd Travel-Agent
```
3. Create a virtual environment and activate it:
```bash
 python -m venv venv
 source venv/bin/activate  # For Linux/macOS
 venv\Scripts\activate     # For Windows
```
4. Install dependencies:
```bash
 pip install -r requirements.txt
```
5. Add your API keys directly in the app sidebar:
   - When running the app, enter your `GROQ_API_KEY` and `SERPAPI_KEY` in the sidebar input fields.

6. Run the app:
```bash
 streamlit run app.py
```

---

## 📂 **Project Structure**

```
Travel-Agent/
├── src/
│   ├── travel_agent/
│   │   ├── graph/
│   │   ├── node/
│   │   ├── tools/
│   │   ├── ui/
│   │   └── state/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## 📝 **How to Use**

1. Enter your travel details in the app.
2. Click through the steps: flight search → hotel search → itinerary planning → activity suggestions → booking confirmation.
3. Review your trip summary and enjoy your travels! 🌟

---

## 💬 **Contributing**

Want to improve Travel Agent AI? Contributions are welcome!
1. Fork the repository.
2. Create a new branch:
```bash
 git checkout -b feature/new-feature
```
3. Commit your changes and push to your branch.
4. Open a Pull Request.

---

## 📧 **Contact**

- **GitHub:** [Shashn-ai](https://github.com/Shashn-ai)
- **Email:** nshashi.223@gmail.com

Happy Traveling! 🌍✨

