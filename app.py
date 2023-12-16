import streamlit as st
import requests

# Function to get the latitude and longitude of a place using Google Maps Geocoding API
def get_lat_lng(place_name):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key=AIzaSyDZAvo3v6mDbEEvNPO_N_yRYAPZ_lKPpLM"
    response = requests.get(url)
    data = response.json()
    location = data['results'][0]['geometry']['location']
    return location['lat'], location['lng']

# Function to get the e-waste facilities near a specific location
def get_nearby_e_waste_facilities(city):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={city}&radius=5000&type=point_of_interest&keyword=e-waste%20facility&key=AIzaSyDZAvo3v6mDbEEvNPO_N_yRYAPZ_lKPpLM"
    response = requests.get(url)
    data = response.json()
    return data

# Streamlit interface
st.title('Nearby E-Waste Facilities')

# Get the place name from the user
place_name = st.text_input('Enter a place name (e.g., city, address):')

# Display the nearby e-waste facilities based on the input place name
if st.button('Find E-Waste Facilities'):
    try:
        facilities = get_nearby_e_waste_facilities(place_name)
        for facility in facilities['results']:
            st.write(facility['name'])
    except IndexError:
        st.write('Location not found. Please enter a valid place name.')
