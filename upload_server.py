from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

# Simulate packet reception
@app.route('/upload', methods=['POST'])
def upload_packet():
    packet_data = request.data  # The packet sent from the client (satellite)
    
    # Simulate the packet processing time (latency)
    packet_number = random.randint(1, 1000)  # Simulate a random packet number for logging
    transmission_time = random.uniform(0.5, 1.5)  # Random time for packet processing
    print(f"Receiving packet {packet_number}...")

    # Simulate a slight delay to mimic network or processing time
    time.sleep(transmission_time)

    # Simulate a successful packet reception
    success = random.choice([True, False])  # Randomly decide if the packet is successfully received
    if success:
        print(f"Packet {packet_number} received successfully.")
        return jsonify({"status": "success", "packet_number": packet_number}), 200
    else:
        print(f"Error receiving packet {packet_number}.")
        return jsonify({"status": "error", "packet_number": packet_number}), 500

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
