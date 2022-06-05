import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")


    weather = await client.find("Washington DC")

    celsius = weather.current.temperature-32/1.8

    print(str(round(celsius)) + "°C")

    print(weather.current.sky_text)

    print(weather.location_name)

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())