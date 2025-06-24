import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

location_name = input("Enter a location name: ")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:

    # Create a map centered on the user's location
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

    marker = folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)

    display(HTML(clcoding._repr_html_()))
else:
    print(f"Location '{location_name}' not found. Please try again with a different name.")

# This code uses the Folium library to create an interactive map centered on a user-provided location name.
# It uses the Geopy library to convert the location name into geographic coordinates (latitude and longitude
# using the Nominatim geocoding service).
# If the location is found, it creates a Folium map centered on those coordinates and adds
# a marker with the location name as a popup.
# If the location is not found, it prompts the user to try again with a different name
# The map is displayed using IPython's display and HTML functions, allowing for interactive viewing in Jupyter notebooks.
# Folium is a powerful library for creating interactive maps in Python, and it is often used
# in data visualization and geographic data analysis projects.
# The Geopy library provides a simple way to perform geocoding, which is the process of converting
# addresses or location names into geographic coordinates.
# This code is useful for applications that require mapping and location-based services,
# such as travel planning, location tracking, or geographic data visualization.
# Folium allows for easy integration of maps into web applications and Jupyter notebooks,
# making it a popular choice for data scientists and developers working with geographic data.

