import requests
from twilio.rest import Client


account_sid = ''
auth_token = ''
parameters = {
    "lat": -1.2746752,
    "lon": 36.847616,
    "appid": "",
    "exclude": "current,minutely,daily"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
will_rain = False
for i in range(0, 12):
    weather_data = response.json()["hourly"][i]["weather"][0]["id"]
    if int(weather_data) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='',
        body='Its going to be a rainy day. Remember to carry an umbrella.',
        to=''
    )

    print(message.status)
