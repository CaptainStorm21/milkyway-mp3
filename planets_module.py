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

