# planets_module.py
planets = {
    "1": "Mercury",
    "2": "Venus",
    "3": "Mars",
    "4": "Jupiter",
    "5": "Saturn",
    "6": "Uranus",
    "7": "Neptune",
    "8": "Pluto",
    "9": "Moon"
}

def display_planet_options():
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

# Main application file to display functionality
def main():
    print("Welcome to the Music Sender App!")
    choice = input("Enter the number of your choice: ")

    if choice in planets_module.planets:
        utilities.send_music_to_planet(planets_module.planets[choice])
    else:
        print("Invalid choice. Please select a valid number.")

if __name__ == "__main__":
    main()
