import planets_module
import utilities

# Main application file to orchestrate functionality
def main():
    print("Welcome to the Milky Way  App!")
    planets_module.display_planet_options()
    choice = input("Enter the number of your choice: ")

    if choice in planets_module.planets:
        utilities.send_music_to_planet(planets_module.planets[choice])
    else:
        print("Invalid choice. Please select a valid number.")

if __name__ == "__main__":
    main()
