import requests
from twilio.rest import Client


account_sid = 'ACa57db76fb22ce2ce9b2a7f83ab116835'
auth_token = 'aaba77a520af82d8dd07682a5338f4d8'
parameters = {
    "lat": -1.2746752,
    "lon": 36.847616,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
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
        from_='+16204078779',
        body='Its going to be a rainy day. Remember to carry an umbrella.',
        to='+254790758813'
    )

    print(message.status)
