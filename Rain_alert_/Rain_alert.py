import requests
import smtplib
OWEndpoint='https://api.openweathermap.org/data/2.5/forecast'
API_KEY='1517223ba2a86e570ac3d8b138ad5a0f'
wheather_params={

    'lat':17.443622,
    'lon':78.351964,
    'cnt':4,
    'appid':API_KEY

}
response=requests.get(OWEndpoint,params=wheather_params)
response.raise_for_status()
data=response.json()
will_rain=False

for hour in data['list']:
    condtion=hour['weather'][0]['id']
    if condtion<700:
        will_rain=True
if will_rain:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='YOUR_MAIL',password="YOUR_PASSWORD")
        connection.sendmail(to_addrs="RECEIVER EMAIL",
                            from_addr="YOUR_MAIL",
                            msg="Subject:Take your umbrella☂\n\nMESSAGE")


