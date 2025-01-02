# planets_module.py
def display_planet_options():
    planets = {
        "1": "Mercury",
        "2": "Venus",
        "3": "Earth",
        "4": "Mars",
        "5": "Jupiter",
        "6": "Saturn",
        "7": "Uranus",
        "8": "Neptune",
        "9": "Pluto",
        "10": "Moon"
    }

    print("Select one planet you want to send your music to:")
    for key, value in planets.items():
        print(f"{key}: {value}")
    return planets

# utilities.py
def send_music_to_planet(planet):
    print(f"Your music has been sent to {planet}!")

# main.py
import planets_module
import utilities

# Main application file to orchestrate functionality
def main():
    print("Welcome to the Music Sender App!")
    planets = planets_module.display_planet_options()
    choice = input("Enter the number of your choice: ")

    if choice in planets:
        utilities.send_music_to_planet(planets[choice])
    else:
        print("Invalid choice. Please select a valid number.")

if __name__ == "__main__":
    main()