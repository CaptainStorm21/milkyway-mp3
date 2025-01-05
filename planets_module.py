planets = {
    "1": "Mercury",
    "2": "Venus",
    "3": "Mars",
    "4": "Jupiter",
    "5": "Saturn",
    "6": "Uranus",
    "7": "Neptune",
    "8": "Pluto",  # Pluto is no longer officially a planet but included for reference
    "9": "Moon"
}

def display_planet_options():
    """
    Displays the list of planets for user selection.
    Returns:
        dict: The mapping of planet IDs to their names.
    """
    print("Where are we sending music to? Pick your celestial body:")
    for key, value in planets.items():
        print(f"{key}: {value}")
    return planets