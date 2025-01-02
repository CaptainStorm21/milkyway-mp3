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