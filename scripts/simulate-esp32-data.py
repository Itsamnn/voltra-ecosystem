#!/usr/bin/env python3
"""
ESP32 Data Simulator for Voltra Ecosystem
Simulates realistic energy consumption data for testing purposes.
"""

import json
import time
import random
import math
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db

# Configuration
FIREBASE_URL = "https://your-project-default-rtdb.firebaseio.com/"
SERVICE_ACCOUNT_PATH = "../serviceAccount.json"
SIMULATION_INTERVAL = 30  # seconds

# Appliance profiles (power consumption patterns)
APPLIANCES = {
    "refrigerator": {"base_power": 150, "variation": 50, "always_on": True},
    "washing_machine": {"base_power": 500, "variation": 200, "cycle_duration": 3600},
    "microwave": {"base_power": 1200, "variation": 100, "usage_probability": 0.1},
    "tv": {"base_power": 200, "variation": 50, "usage_probability": 0.3},
    "lights": {"base_power": 100, "variation": 30, "usage_probability": 0.4},
    "air_conditioner": {"base_power": 2000, "variation": 500, "usage_probability": 0.2}
}

class EnergySimulator:
    def __init__(self):
        self.initialize_firebase()
        self.appliance_states = {}
        self.base_voltage = 230.0  # Volts
        self.start_time = time.time()
        
    def initialize_firebase(self):
        """Initialize Firebase connection"""
        try:
            cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
            firebase_admin.initialize_app(cred, {
                'databaseURL': FIREBASE_URL
            })
            print("✅ Firebase initialized successfully")
        except Exception as e:
            print(f"❌ Firebase initialization failed: {e}")
            exit(1)
    
    def simulate_appliance_usage(self, appliance, config):
        """Simulate individual appliance power consumption"""
        current_time = time.time()
        
        # Initialize appliance state if not exists
        if appliance not in self.appliance_states:
            self.appliance_states[appliance] = {
                "is_on": config.get("always_on", False),
                "cycle_start": None,
                "last_toggle": current_time
            }
        
        state = self.appliance_states[appliance]
        
        # Handle always-on appliances (like refrigerator)
        if config.get("always_on", False):
            # Simulate compressor cycles
            cycle_time = (current_time - self.start_time) % 1800  # 30-minute cycles
            if cycle_time < 600:  # On for 10 minutes
                power = config["base_power"] + random.uniform(-config["variation"], config["variation"])
            else:
                power = config["base_power"] * 0.1  # Standby power
            return max(0, power)
        
        # Handle cyclic appliances (like washing machine)
        if "cycle_duration" in config:
            if state["cycle_start"] and (current_time - state["cycle_start"]) < config["cycle_duration"]:
                # In cycle - simulate power curve
                cycle_progress = (current_time - state["cycle_start"]) / config["cycle_duration"]
                power_multiplier = 0.5 + 0.5 * math.sin(cycle_progress * 2 * math.pi)
                power = config["base_power"] * power_multiplier
                return power + random.uniform(-config["variation"], config["variation"])
            elif random.random() < 0.001:  # 0.1% chance to start cycle each check
                state["cycle_start"] = current_time
                return config["base_power"]
            else:
                return 5  # Standby power
        
        # Handle probabilistic appliances
        usage_prob = config.get("usage_probability", 0.1)
        
        # Toggle logic
        if not state["is_on"] and random.random() < usage_prob * 0.01:
            state["is_on"] = True
            state["last_toggle"] = current_time
        elif state["is_on"] and (current_time - state["last_toggle"]) > random.uniform(300, 1800):
            state["is_on"] = False
            state["last_toggle"] = current_time
        
        if state["is_on"]:
            power = config["base_power"] + random.uniform(-config["variation"], config["variation"])
            return max(0, power)
        else:
            return random.uniform(0, 5)  # Standby power
    
    def generate_sensor_data(self):
        """Generate realistic sensor readings"""
        # Calculate total power from all appliances
        total_power = 0
        appliance_breakdown = {}
        
        for appliance, config in APPLIANCES.items():
            power = self.simulate_appliance_usage(appliance, config)
            appliance_breakdown[appliance] = round(power, 2)
            total_power += power
        
        # Add some noise and base load
        base_load = 50  # Base household consumption
        noise = random.uniform(-20, 20)
        total_power += base_load + noise
        
        # Calculate electrical parameters
        voltage = self.base_voltage + random.uniform(-5, 5)  # Voltage variation
        current = total_power / voltage if voltage > 0 else 0
        power_factor = random.uniform(0.85, 0.95)  # Typical household power factor
        
        # Calculate energy (kWh) - cumulative
        energy_kwh = (total_power / 1000) * (SIMULATION_INTERVAL / 3600)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "voltage": round(voltage, 2),
            "current": round(current, 3),
            "power": round(total_power, 2),
            "energy_kwh": round(energy_kwh, 6),
            "power_factor": round(power_factor, 3),
            "frequency": round(50 + random.uniform(-0.5, 0.5), 2),
            "appliance_breakdown": appliance_breakdown,
            "device_id": "ESP32_SIM_001"
        }
    
    def send_to_firebase(self, data):
        """Send data to Firebase Realtime Database"""
        try:
            # Send to main telemetry path
            ref = db.reference('telemetry')
            ref.push(data)
            
            # Update latest reading
            latest_ref = db.reference('latest')
            latest_ref.set(data)
            
            print(f"📊 Sent data: {data['power']:.1f}W, {data['voltage']:.1f}V, {data['current']:.2f}A")
            
        except Exception as e:
            print(f"❌ Failed to send data: {e}")
    
    def run_simulation(self):
        """Run continuous simulation"""
        print("🚀 Starting ESP32 data simulation...")
        print(f"📡 Sending data every {SIMULATION_INTERVAL} seconds")
        print("🔌 Simulating appliances:", list(APPLIANCES.keys()))
        print("⏹️  Press Ctrl+C to stop\n")
        
        try:
            while True:
                data = self.generate_sensor_data()
                self.send_to_firebase(data)
                time.sleep(SIMULATION_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n🛑 Simulation stopped by user")
        except Exception as e:
            print(f"\n❌ Simulation error: {e}")

if __name__ == "__main__":
    simulator = EnergySimulator()
    simulator.run_simulation()