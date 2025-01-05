import planets_module
import utilities

def main():
    print("Welcome to the Music Sender App!")
    planets_module.display_planet_options()
    choice = input("Enter the number of your choice: ")

    switch = {
        "1": lambda: utilities.send_music_to_planet(planets_module.planets["1"]),
        "2": lambda: utilities.send_music_to_planet(planets_module.planets["2"]),
        "3": lambda: utilities.send_music_to_planet(planets_module.planets["3"]),
        "4": lambda: utilities.send_music_to_planet(planets_module.planets["4"]),
        "5": lambda: utilities.send_music_to_planet(planets_module.planets["5"]),
        "6": lambda: utilities.send_music_to_planet(planets_module.planets["6"]),
        "7": lambda: utilities.send_music_to_planet(planets_module.planets["7"]),
        "8": lambda: utilities.send_music_to_planet(planets_module.planets["8"]),
        "9": lambda: utilities.send_music_to_planet(planets_module.planets["9"]),
    }

    # Using the switch dictionary to call the appropriate function
    switch.get(choice, lambda: print("Invalid choice. Please select a valid number."))()

if __name__ == "__main__":
    main()