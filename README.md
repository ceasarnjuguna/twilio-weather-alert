**Rain Alert SMS**
This Python script uses the OpenWeather API and Twilio API to send an SMS message when it is going to rain in the next 12 hours. It uses the latitude and longitude of a location to retrieve the weather forecast from the OpenWeather API, and if rain is expected, it sends an SMS message using the Twilio API.

**Setup**
**Prerequisites**
. Python 3.x
. requests library
. twilio library

**Installation**
1.Clone this repository or download the ZIP file and extract it to a directory of your choice.
2.Install the required libraries by running the following command:

_pip install requests twilio_

**Configuration**
Before running the script, you need to set the following environment variables:

. TWILIO_ACCOUNT_SID: Your Twilio account SID.
. TWILIO_AUTH_TOKEN: Your Twilio auth token.
. OPENWEATHER_API_KEY: Your OpenWeather API key.
You can set environment variables on your system or by creating a .env file in the project directory with the following contents:

_TWILIO_ACCOUNT_SID=your_twilio_account_sid_
_TWILIO_AUTH_TOKEN=your_twilio_auth_token_
_OPENWEATHER_API_KEY=your_openweather_api_key_

Replace your_twilio_account_sid, your_twilio_auth_token, and your_openweather_api_key with your actual values.

**Usage**
To use the script, run the following command:

_python rain_alert_sms.py_

The script will check the weather forecast for the latitude and longitude specified in the parameters dictionary, and if rain is expected in the next 12 hours, it will send an SMS message to the phone number specified in the to field of the client.messages.create() method.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

