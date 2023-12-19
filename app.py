import streamlit as st
import requests
import pandas as pd

# Function to get nearby recycling centers using Google Places API
def get_nearby_recycling_centers(api_key, location, radius=5000, keyword="recycling center"):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "keyword": keyword,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "results" in data:
        return data["results"]
    else:
        return None

# Streamlit app
def main():
    st.title("Nearby Recycling Centers Finder")

    # Input API key and location
    api_key = "AIzaSyDZAvo3v6mDbEEvNPO_N_yRYAPZ_lKPpLM"
    location = st.text_input("Enter your location (latitude,longitude):")

    if not api_key or not location:
        st.warning("Please location.")
        st.stop()

    # Get nearby recycling centers
    recycling_centers = get_nearby_recycling_centers(api_key, location)

    if recycling_centers:
        # Display the results in a DataFrame
        df = pd.json_normalize(recycling_centers)
        st.dataframe(df)

        # Display the locations on a map
        st.map(df[["geometry.location.lat", "geometry.location.lng"]])
    else:
        st.warning("No recycling centers found nearby.")

if __name__ == "__main__":
    main()
