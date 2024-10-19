# File: features/weather.py

import aiohttp

async def weather(location):
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if data["cod"] != "404":
                main = data["main"]
                weather_desc = data['weather'][0]['description']
                temp = main['temp']
                humidity = main['humidity']
                return f"Weather in {location}: {weather_desc.capitalize()}, Temperature: {temp}°C, Humidity: {humidity}%"
            else:
                return "City not found"