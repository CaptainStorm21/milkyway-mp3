import random
import time

# Constants
SPEED_OF_LIGHT_KMPS = 299792  # Speed of light in km/s
PACKET_SIZE = 1024  # 1 KB per packet (just for simulation)
song_volume = 10 * 1024 * 1024  # Example file size: 10 MB (in bytes)

# Planets and their average distances from Earth in kilometers
planets = {
    "Moon": 384400,  # km
    "Mercury": 91.7e6,  # km
    "Venus": 41.4e6,  # km
    "Mars": 78.3e6,  # km
    "Jupiter": 628.7e6,  # km
    "Saturn": 1.2e9,  # km
    "Uranus": 2.6e9,  # km
    "Neptune": 4.3e9,  # km
}

# Function to calculate time for light to travel and packet upload to a planet
def calculate_arrival_time(planet, distance_km, song_volume):
    # Calculate the travel time of light to the planet in seconds
    travel_time_seconds = distance_km / SPEED_OF_LIGHT_KMPS
    
    # Calculate the number of packets needed to send the song (1 KB per packet)
    packets_needed = song_volume / PACKET_SIZE
    print(f"Sending {packets_needed} packets to {planet}...")
    
    # Simulate the time it takes to upload each packet (in seconds)
    transmission_time_per_packet = random.uniform(0.5, 1.5)  # Simulated time to transmit each packet
    total_packet_time = packets_needed * transmission_time_per_packet

    # Total time is the sum of light travel time and packet transmission time
    total_time_seconds = travel_time_seconds + total_packet_time

    # Convert the total time to hours
    total_time_hours = total_time_seconds / 3600  # Convert seconds to hours

    return total_time_hours

# Simulate the time for each planet
for planet, distance in planets.items():
    arrival_time = calculate_arrival_time(planet, distance, song_volume)
    print(f"Time for file to arrive at {planet}: {arrival_time:.2f} hours\n")
