from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time
import planets_module
from AE_conversion import km_to_au  # Import the AU conversion function
from astropy.coordinates import SkyCoord


# Function to calculate the distance to a celestial body
def get_distance_to_body(body_name):
    """
    Calculates the distance from Earth to the specified celestial body.
    Args:
        body_name (str): The name of the celestial body (e.g., 'Mars', 'Venus').
    Returns:
        float: The distance in kilometers.
    """
    try:
        # Get the current time
        now = Time.now()

        # Earth location
        earth_location = EarthLocation(lat=0.0, lon=0.0, height=0.0)

        # Retrieve the position of the celestial body
        body_position = get_body(body_name.lower(), now, earth_location)

        # Ensure the body_position is a SkyCoord object, and get its distance in AU
        if isinstance(body_position, SkyCoord):
            # Convert distance from AU to kilometers (1 AU = 149,597,870.7 km)
            distance_km = body_position.distance.to('km').value  # Convert to km directly
            return distance_km
        else:
            raise ValueError("Invalid body position data")
    except Exception as e:
        return f"Error calculating distance: {str(e)}"


# Main script logic
def main():
    # Display planet options
    planet_mapping = planets_module.display_planet_options()

    # Prompt user for input
    selected_id = input("\nEnter the number corresponding to your selection: ").strip()
    
    if selected_id not in planet_mapping:
        print("Invalid selection. Please restart and try again.")
        return
    
    selected_planet = planet_mapping[selected_id]
    print(f"\nCalculating distance to {selected_planet}...")

    # Calculate the distance
    distance = get_distance_to_body(selected_planet)
    if isinstance(distance, float):
        # Convert and display the distance in AU
        distance_au = km_to_au(distance) 
        print(f"The current distance from Earth to {selected_planet} is approximately {distance_au:.6f} AU or {distance:.2f} km.")
    else:
        print(distance)


# Run the program
if __name__ == "__main__":
    main()
