# Weather Alert Notification System

This project uses the OpenWeatherMap API to check the weather forecast and sends a WhatsApp message via Twilio if it detects rain in the forecast.

## Technologies Used:
- **Python**: Core programming language
- **Twilio**: API to send WhatsApp messages
- **OpenWeatherMap (OWM)**: API for weather data

## Requirements:
- Python 3.x
- Twilio account with a verified WhatsApp number
- OpenWeatherMap API key

## Project Setup:

### 1. Clone the project:
```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Install dependencies:
Ensure you have Python 3 installed, and then install required packages:
```bash
pip install requests twilio python-dotenv
```

### 3. Get your API keys:
- **OpenWeatherMap**: Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and generate an API key.
- **Twilio**: Create a Twilio account at [Twilio](https://www.twilio.com/) and get your `Account SID`, `Auth Token`, and set up WhatsApp messaging.

### 4. Create a `.env` file:
In the project directory, create a `.env` file and add your API keys as follows:
```bash
OWM_API_KEY=<your_openweather_api_key>
TWILIO_ACCOUNT_SID=<your_twilio_account_sid>
TWILIO_AUTH_TOKEN=<your_twilio_auth_token>
```

### 5. Edit Weather and WhatsApp Details:
In the Python script, adjust the weather coordinates and WhatsApp phone numbers:
- `lat` and `lon`: Use your desired latitude and longitude.
- `to`: Replace with the recipient's WhatsApp number in the format `whatsapp:+<country_code><number>`.
- `from_`: Use Twilio’s sandbox WhatsApp number (`whatsapp:+14155238886`).

### 6. Running the script:
Once setup is complete, run the script:
```bash
python weather_alert.py
```

The script will fetch the weather forecast for your specified location and send a WhatsApp message if rain is predicted.

## How It Works:
1. **Fetch Weather Data**: The script makes a request to the OpenWeatherMap API to retrieve the weather forecast for a specified location.
2. **Check for Rain**: It checks the weather condition codes for upcoming hours. If the condition code is less than 700, it indicates rain.
3. **Send WhatsApp Alert**: If rain is detected, a WhatsApp message is sent to notify the user to carry an umbrella. If the weather is clear, a different message is sent.

## Environment Variables:
The project relies on the following environment variables stored in the `.env` file:
- `OWM_API_KEY`: Your OpenWeatherMap API key.
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token.

## Example Output:
When you run the script, the Twilio API will send one of the following WhatsApp messages:
- **If rain is predicted**: "It's going to rain today⛈️. Remember to bring an umbrella☔"
- **If the weather is clear**: "The weather is clear today☀️😀"
