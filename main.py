import json
import os
from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time
from astropy.coordinates import SkyCoord
import planets_module
from AE_conversion import km_to_au  # Assuming you have this function defined

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

# Function to load songs from song_tracks.json
def load_songs_from_json(file_path):
    """
    Loads song data from a JSON file.
    Args:
        file_path (str): The path to the song_tracks.json file.
    Returns:
        list: A list of songs with 'id', 'artist', and 'title_song'.
    """
    try:
        with open(file_path, 'r') as file:
            songs = json.load(file)
        return songs
    except Exception as e:
        return f"Error loading songs from file: {str(e)}"

# Function to display songs and let the user select one
def display_songs_and_select(songs):
    """
    Displays all songs and allows the user to select one.
    Args:
        songs (list): A list of song dictionaries to display.
    """
    # Display all songs with id, artist, and song title
    for song in songs:
        print(f"{song['id']} - Artist: {song['artist']} - Song: {song['title_song']}")

    # Ask the user to pick a song by its id
    try:
        song_id = int(input("\nEnter the id of the song you want to select: ").strip())

        # Find the song with the selected id
        selected_song = next((song for song in songs if song['id'] == song_id), None)

        if selected_song:
            print(f"\nYou selected: Artist: {selected_song['artist']}, Song: {selected_song['title_song']}")
        else:
            print("Invalid song ID selected. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main script logic
def main():
    # Display planet options
    planet_mapping = planets_module.display_planet_options()

    # Prompt user for input to calculate distance to a celestial body
    selected_id = input("\nEnter the number corresponding to your selection for celestial body: ").strip()

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

    # Load song data from song_tracks.json (assuming it's in the root of the project)
    print("\nNow, let's load and display songs from song_tracks.json!")

    song_file = 'song_tracks.json'  # Since it's located in the root of the project

    if os.path.exists(song_file) and os.path.isfile(song_file):
        # Load the songs
        songs = load_songs_from_json(song_file)

        if isinstance(songs, list) and songs:
            # Display songs and allow the user to select one
            display_songs_and_select(songs)
        else:
            print("No songs found or error loading songs.")
    else:
        print("Invalid file path. Please ensure song_tracks.json is located in the root of the project.")

# Run the program
if __name__ == "__main__":
    main()
