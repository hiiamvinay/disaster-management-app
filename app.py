from flask import Flask, render_template, request, jsonify
import requests
from chatbot import chat_response

app = Flask(__name__)

API_KEY = "<YOUR_API_KEY>"  
system_prompt = """
You are an AI chatbot designed to assist users with disaster management information and support. Your primary goal is to provide accurate, helpful, and timely responses based on a pre-loaded knowledge base. You operate offline and do not have access to the internet.
Instructions:

    Tone and Style: Maintain a friendly, supportive, and informative tone. Use clear and concise language that is easy for users to understand.

    Capabilities:
        Provide information on emergency preparedness for various disasters (e.g., hurricanes, earthquakes, floods).
        Offer safety procedures and guidelines for what to do during an emergency.
        Share basic first aid information for common injuries and medical emergencies.
        Inform users about local resources, such as shelters and food banks, based on pre-loaded data.
        Provide mental health support resources and coping strategies for users feeling anxious or overwhelmed.
        Answer frequently asked questions related to disaster management.

    User Interaction:
        Prompt users to ask questions or request information by saying, "How can I assist you today?"
        Encourage follow-up questions to ensure users receive the information they need.
        If a user asks for information that is not available in your knowledge base, respond with, "I'm sorry, but I don't have that information. Is there something else I can help you with?"

    Response Generation: Use the pre-loaded knowledge base to generate responses. Ensure that all information provided is accurate and relevant to the user's query.

    Limitations: Remind users that you are an offline chatbot and do not have access to real-time data or updates.
"""
conversation_history = [{"role": "system", "content": system_prompt}]



def get_coordinates(location):
    url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json&limit=1"
    response = requests.get(url, headers={"User-Agent": "Flask-App"})
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    return None, None

# Helper to fetch weather forecast
def fetch_forecast(lat, lon):
    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(weather_url)
        
        data = response.json()
        
        today = {
            "max_temp": max(item["main"]["temp_max"] for item in data["list"][:8]),
            "min_temp": min(item["main"]["temp_min"] for item in data["list"][:8]),
            "description": data["list"][0]["weather"][0]["description"],
            "wind_speed": data["list"][0]["wind"]["speed"],
            "rain": data["list"][0].get("rain", {}).get("3h", 0),
        }
        forecast = []
        for item in data["list"]:
            forecast.append({
                "datetime": item["dt_txt"],
                "max_temp": item["main"]["temp_max"],
                "min_temp": item["main"]["temp_min"],
                "description": item["weather"][0]["description"],
                "wind_speed": item["wind"]["speed"],
                "rain": item.get("rain", {}).get("3h", 0),
            })
        return today, forecast
    except Exception as e:
        print(f"Error fetching forecast: {e}")
        return None, None

# Disaster detection logic
def detect_disasters(forecast):
    disasters = []
    for weather in forecast:
        description = weather["description"].lower()
        wind_speed = weather["wind_speed"]
        rain = weather["rain"]
        temp_max = weather["max_temp"]
        temp_min = weather["min_temp"]

        if "storm" in description or wind_speed > 20:
            disasters.append(f"Severe storm detected with wind speed {wind_speed} m/s.")
        if rain > 50:
            disasters.append(f"Heavy rainfall detected: {rain} mm in 3 hours.")
        if temp_max > 40:
            disasters.append(f"Heatwave alert: Maximum temperature {temp_max}°C.")
        if temp_min < 0:
            disasters.append(f"Cold spell alert: Minimum temperature {temp_min}°C.")

    return list(set(disasters))

# Routes
@app.route('/')
def home():
    conversation_history = [{"role": "system", "content": system_prompt}]
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    lat, lon = get_coordinates(location)

    if lat and lon:
        today, forecast = fetch_forecast(lat, lon)
        disasters = detect_disasters(forecast)  # Check for potential disasters
        return render_template('result.html', location=location, today=today, forecast=forecast, disasters=disasters)
    else:
        return render_template('error.html', message="Location not found.")



def chatbot_reply(message):
    conversation_history.append({"role": "user", "content": message})
    ai_response = chat_response(conversation_history)
    conversation_history.append({"role": "assistant", "content": ai_response})
    return ai_response

   

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    reply = chatbot_reply(user_message)
    return jsonify({"reply": reply})


@app.route('/chat', methods=['GET'])
def chat_info():
    return jsonify({"message": "This endpoint is for POST requests to handle chatbot messages."})

@app.route('/ai')
def ai():
    return render_template('ai.html')

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    forecast = fetch_forecast(location)
    alerts = detect_disasters(forecast)
    return render_template('result.html', forecast=forecast, alerts=alerts)