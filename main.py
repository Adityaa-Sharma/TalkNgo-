import requests
import os
from groq import Groq
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

foursquare_api_key = os.getenv("FOURSQUARE_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
opencage_api_key=os.getenv("OPEN_CAGE_API_KEY")

client = Groq(api_key=groq_api_key)

# initialising geocoder to convert the address into latitudes and longitudes.
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(opencage_api_key)

def get_place_details(address, category):
    results = geocoder.geocode(address)
    
    if not results:
        return {"error": "Address not found"}
    
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    url = "https://api.foursquare.com/v3/places/search"
    
    params = {
        "ll": f"{lat},{lng}",
        "query": category,  
        "radius": 1000,     
        "limit": 1        
    }
    
    headers = {
        "Accept": "application/json",
        "Authorization": foursquare_api_key
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch details, status code: {response.status_code}"}
    
    



details=get_place_details("c-scheme, jaipur , rajasthan","what are the nearest party clubs")
print(details)