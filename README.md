
---


# Disaster Management and Weather Forecasting App

This project is a **Disaster Management and Weather Forecasting App** that provides users with weather forecasts, disaster alerts, and AI-powered assistance for disaster-related queries.

---

## Features

1. **Weather Forecasts**:
   - Provides daily and 3-day weather forecasts.
   - Displays key weather parameters like temperature, wind speed, and rainfall.

2. **Disaster Alerts**:
   - Detects and alerts users about potential disasters such as storms, heavy rainfall, heatwaves, or cold spells.

3. **AI Chatbot**:
   - An AI-powered chatbot offering disaster preparedness tips, first aid guidance, and mental health support.
   - Supports user interaction for quick and informative responses.

4. **User-Friendly Interface**:
   - Intuitive web interface for entering locations and accessing forecasts or chatbot assistance.

---

## Tech Stack

- **Frontend**: 
  - HTML, CSS
  - JavaScript (including dynamic DOM manipulation for chatbot)
- **Backend**:
  - Python (Flask framework)
  - OpenWeatherMap API for weather data
  - OpenStreetMap API for location coordinates
- **AI**:
  - Llama3-based chatbot for disaster management queries via Groq

---

## Prerequisites

1. **Install Python**: Make sure you have Python 3.x installed.
2. **Install Required Libraries**:
   - Flask
   - Requests
   - Groq
```cmd
pip install flask requests groq
```
3. **Set Up API Keys**:
   - **Groq API Key**:
     - Obtain an API key from [Groq Console](https://console.groq.com/keys).
   - **OpenWeatherMap API Key**:
     - Obtain an API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/hiiamvinay/disaster-management-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd disaster-management-app
   ```

3. Set your API keys in the `API_KEY` variable in `app.py`:
   - Replace `<YOUR_API_KEY>` with your OpenWeatherMap API key.
   - Replace `<YOUR_GROQ_API_KEY>` with your Groq API key.

4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## Folder Structure

```
.
├── templates/
│   ├── index.html      # Home page
│   ├── result.html     # Weather results page
│   └── ai.html         # AI chatbot page
├── static/
│   ├── styles.css      # Styling for the application
├── app.py              # Main application file
├── chatbot.py          # Chatbot logic
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

---

## Usage

1. **Weather Forecast**:
   - Enter a location on the home page.
   - View the current and 3-day weather forecast, along with any disaster alerts.

2. **AI Chatbot**:
   - Navigate to the AI page and interact with the chatbot for disaster management information.

---

## Key Functions

- `get_coordinates(location)`: Fetches latitude and longitude for a given location.
- `fetch_forecast(lat, lon)`: Retrieves weather data using the OpenWeatherMap API.
- `detect_disasters(forecast)`: Identifies potential disaster scenarios from the forecast data.
- `chatbot_reply(message)`: Handles user interaction with the AI chatbot.

---

## Future Enhancements

- Add real-time disaster notifications.
- Expand chatbot knowledge base for localized emergency information.
- Enable multi-language support.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this application.

---

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for weather data.
- [OpenStreetMap](https://www.openstreetmap.org/) for geolocation services.
- Llama3-based AI for disaster-related queries, powered by [Groq](https://console.groq.com/keys).

---


