from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_geolocation(zip_code, city, state):
    # Combine the address components
    address = f"{zip_code}, {city}, {state}"

    # Initialize the geocoder
    geolocator = Nominatim(user_agent="my_geocoder")

    try:
        # Get the location information
        location = geolocator.geocode(address)

        if location:
            # Print the latitude and longitude
            print("Latitude:", location.latitude)
            print("Longitude:", location.longitude)
        else:
            print("Location not found.")
    except Exception as e:
        print("Error:", str(e))

# Example usage
get_geolocation("81560","curitiba","PR")

def calculate_distance(coord1, coord2):
    # coord1 and coord2 are tuples of (latitude, longitude)
    distance = geodesic(coord1, coord2).kilometers
    return distance

# Example coordinates
coordinate1 = (-22.9056391, -47.059564)  # Example coordinate for campinas
coordinate2 = (-25.4295963, -49.2712724)  # Example coordinate for Curitiba

# Calculate distance
distance = calculate_distance(coordinate1, coordinate2)

# Print the distance
print(f"The distance between the two coordinates is approximately {distance:.2f} kilometers.")