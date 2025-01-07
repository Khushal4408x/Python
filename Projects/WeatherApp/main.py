import requests

def get_weather(city, api_key):
    # OpenWeatherMap API endpoint
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    #http://api.weatherapi.com/v1/current.json?key={api_key}}&q={city}&aqi=no
    # Make a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        city_name = data['location']['name']
        region = data['location']['region']
        country= data['location']['country']
        tempra
        weather_description = data['weather'][0]['description']
        
        # Print the weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

def main():
    api_key = "bcecc816e68a4050aa8163505250501"  
    city = input("Enter the city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()