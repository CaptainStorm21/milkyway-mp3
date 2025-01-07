import requests
import time
import random

def send_mp3_to_planets(satellite_url, mp3_file, packets_needed):
    packet_size = 1024  # Assuming each packet is 1 KB
    total_size = len(mp3_file)
    transmission_time_per_packet = random.uniform(0.5, 1.5)  # Simulate time to transmit each packet (0.5-1.5 seconds)

    print(f"Sending MP3 file of size {total_size / 1024:.2f} MB in {packets_needed} packets.")

    for i in range(0, total_size, packet_size):
        packet = mp3_file[i:i + packet_size]
        packet_number = i // packet_size + 1
        # Simulate sending the packet to the fake upload server (Flask server)
        print(f"Sending packet {packet_number}/{packets_needed} to satellite...")
        
        # Simulate sending the packet to the Flask server
        response = requests.post(satellite_url, data=packet)
        
        if response.status_code == 200:
            print(f"Packet {packet_number} sent successfully.")
        else:
            print(f"Error sending packet {packet_number}. Server response: {response.status_code}")
        
        time.sleep(transmission_time_per_packet)  # Simulating time taken to send each packet
