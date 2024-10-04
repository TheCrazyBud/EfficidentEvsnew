# import random
# import time

# class EVDataSimulator:
#     def __init__(self):
#         self.battery_level = random.randint(60, 100)
#         self.charging_status = False
#         self.distance_remaining = random.randint(100, 300)
#         self.charging_stations = [(50.5, 30.5), (48.8, 31.6), (47.5, 34.0)]
    
#     def update_data(self):
#         if not self.charging_status:
#             self.battery_level -= random.uniform(0.1, 0.5)
#             self.distance_remaining -= random.uniform(1, 5)
        
#         if self.battery_level < 20:
#             self.charging_status = True
#             self.battery_level += random.uniform(5, 10)
        
#         if self.battery_level >= 80:
#             self.charging_status = False
    
#     def get_data(self):
#         return {
#             "battery_level": round(self.battery_level, 2),
#             "charging_status": self.charging_status,
#             "distance_remaining": round(self.distance_remaining, 2),
#             "nearest_charging_station": self.get_nearest_charging_station()
#         }
    
#     def get_nearest_charging_station(self):
#         return self.charging_stations[0]

# def predict_energy_usage(battery_level, distance_remaining):
#     if battery_level > 50 and distance_remaining < 100:
#         return "Optimal for a short trip."
#     elif battery_level < 50 and distance_remaining > 100:
#         return "Consider charging soon."
#     else:
#         return "Monitor your usage."

# def smart_route_suggestion(ev_data):
#     if ev_data["charging_status"]:
#         return f"Charging at station. Battery level: {ev_data['battery_level']}%"
#     else:
#         return f"Suggest nearest charging station at {ev_data['nearest_charging_station']}."

# # Main Loop
# ev_data_sim = EVDataSimulator()

# while True:
#     ev_data_sim.update_data()
#     current_data = ev_data_sim.get_data()
    
#     print(f"Real-time Data: {current_data}")
    
#     energy_prediction = predict_energy_usage(current_data['battery_level'], current_data['distance_remaining'])
#     print(f"Energy Prediction: {energy_prediction}")
    
#     route_suggestion = smart_route_suggestion(current_data)
#     print(f"Route Suggestion: {route_suggestion}")
    
#     time.sleep(5)


# With additional features 



# import random
# import datetime
# import json

# class ElectricVehicle:
#     def __init__(self):
#         # Existing vehicle parameters
#         self.battery_level = random.uniform(30, 100)  # percentage
#         self.battery_health = random.uniform(85, 100)  # Battery health percentage
#         self.motor_efficiency = random.uniform(90, 100)  # Motor efficiency percentage
#         self.tire_pressure = random.uniform(30, 35)  # PSI
#         self.regenerative_energy = 0  # Regenerative braking energy (kWh)
#         self.distance_remaining = random.uniform(50, 300)  # km left
#         self.charging_rate = self.get_dynamic_charging_rate()  # dynamic charging rate (kW)
#         self.weather = random.choice(["sunny", "rainy", "snowy", "windy"])  # Weather condition
#         self.traffic_condition = random.choice(["light", "moderate", "heavy"])  # Traffic condition
#         self.location = (random.uniform(10, 100), random.uniform(10, 100))  # Mock location
#         self.alerts = []
        
#         # New vehicle parameters
#         self.vehicle_id = random.randint(1000, 9999)  # Unique vehicle ID for fleet management
#         self.multi_vehicle_support = {}  # Placeholder for multiple vehicle data
#         self.last_maintenance_check = datetime.datetime.now()
#         self.cloud_data = []  # Placeholder for cloud storage
#         self.v2g_enabled = True  # Vehicle-to-grid support enabled
#         self.driving_mode = "Normal"  # Default driving mode

#     def get_dynamic_charging_rate(self):
#         return random.uniform(5, 25)  # kW

#     def get_nearest_charging_station(self):
#         # Mock charging station location
#         return random.choice([
#             {"station_name": "ChargePoint", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Available", "price_per_kWh": random.uniform(0.1, 0.5)},
#             {"station_name": "Tesla Supercharger", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Busy", "price_per_kWh": random.uniform(0.1, 0.5)},
#         ])

#     def get_alerts(self):
#         # Vehicle health and performance alerts
#         alerts = []
#         if self.battery_level < 10:
#             alerts.append("Low battery! Consider charging.")
#         if self.battery_health < 75:
#             alerts.append("Battery health is low! Consider battery check.")
#         if self.tire_pressure < 30:
#             alerts.append("Tire pressure low! Check tires.")
#         return alerts

#     def battery_degradation_prediction(self):
#         if self.battery_health < 80:
#             return "Battery health is degrading. Expect replacement in 1-2 years."
#         else:
#             return "Battery health is stable."

#     def calculate_eta(self):
#         average_speed = random.randint(50, 80)  # Mock speed in km/h
#         eta_hours = self.distance_remaining / average_speed
#         eta = datetime.datetime.now() + datetime.timedelta(hours=eta_hours)
#         return eta.strftime("%H:%M:%S")

#     def store_data_in_cloud(self):
#         # Simulate storing data in the cloud
#         vehicle_data = {
#             "battery_level": self.battery_level,
#             "battery_health": self.battery_health,
#             "motor_efficiency": self.motor_efficiency,
#             "tire_pressure": self.tire_pressure,
#             "regenerative_energy": self.regenerative_energy,
#             "distance_remaining": self.distance_remaining,
#             "weather": self.weather,
#             "traffic_condition": self.traffic_condition,
#             "location": self.location
#         }
#         self.cloud_data.append(vehicle_data)
#         return "Data stored in cloud"

#     def suggest_driving_mode(self):
#         # Suggest a driving mode based on energy efficiency and driving conditions
#         if self.traffic_condition == "heavy" or self.weather in ["rainy", "snowy"]:
#             self.driving_mode = "Eco Mode"
#         else:
#             self.driving_mode = "Sport Mode"
#         return self.driving_mode

#     def get_v2g_status(self):
#         # Simulate V2G (Vehicle-to-Grid) functionality
#         if self.v2g_enabled:
#             return "V2G enabled. You can discharge energy to the grid during peak hours."
#         else:
#             return "V2G not available."

#     def route_planning_with_range_anxiety(self):
#         # Smart route planner to minimize range anxiety
#         if self.distance_remaining < 50:
#             return "Route planning suggests a nearby charging station due to low range."
#         else:
#             return "Route planning optimal, no immediate charging required."

#     def fleet_management(self, fleet_data):
#         # Example of supporting multiple vehicles (Fleet management)
#         for vehicle_id, data in fleet_data.items():
#             print(f"Vehicle {vehicle_id} - Battery Level: {data['battery_level']}%, Location: {data['location']}")

#     def dynamic_pricing_for_charging(self):
#         # Dynamic charging price suggestion based on real-time electricity pricing
#         nearest_station = self.get_nearest_charging_station()
#         return f"Current price at {nearest_station['station_name']}: {nearest_station['price_per_kWh']} $/kWh"

#     def carbon_emission_offset(self):
#         # Calculate avoided emissions by using EV instead of gasoline vehicle
#         emissions_saved = self.distance_remaining * 0.2  # Mock calculation: 0.2 kg of CO2 saved per km
#         return f"Carbon emissions avoided: {emissions_saved} kg CO2"

#     def predictive_maintenance(self):
#         # Predictive maintenance suggestions based on vehicle health
#         days_since_last_maintenance = (datetime.datetime.now() - self.last_maintenance_check).days
#         if days_since_last_maintenance > 90:
#             return "Time for a maintenance check!"
#         else:
#             return "No maintenance required."

# # Mock use case demonstrating multiple new features
# def main():
#     ev = ElectricVehicle()

#     # Collect and print EV data
#     current_data = {
#         "battery_level": ev.battery_level,
#         "battery_health": ev.battery_health,
#         "motor_efficiency": ev.motor_efficiency,
#         "tire_pressure": ev.tire_pressure,
#         "regenerative_energy": ev.regenerative_energy,
#         "distance_remaining": ev.distance_remaining,
#         "weather": ev.weather,
#         "traffic_condition": ev.traffic_condition,
#         "nearest_charging_station": ev.get_nearest_charging_station(),
#         "dynamic_pricing": ev.dynamic_pricing_for_charging(),
#         "v2g_status": ev.get_v2g_status(),
#         "driving_mode": ev.suggest_driving_mode(),
#         "carbon_offset": ev.carbon_emission_offset(),
#         "eta": ev.calculate_eta(),
#         "route_planning": ev.route_planning_with_range_anxiety(),
#         "alerts": ev.get_alerts(),
#         "predictive_maintenance": ev.predictive_maintenance()
#     }
    
#     # Store data in cloud (simulated)
#     cloud_response = ev.store_data_in_cloud()

#     # Print data to simulate dashboard
#     print(json.dumps(current_data, indent=4))
#     print(cloud_response)

#     # Fleet management example
#     fleet_data = {
#         1001: {"battery_level": 60, "location": (55.5, 40.3)},
#         1002: {"battery_level": 80, "location": (60.1, 42.9)}
#     }
#     ev.fleet_management(fleet_data)

# if __name__ == "__main__":
#     main()


# with additional features 





# import random
# import datetime
# import json

# class ElectricVehicle:
#     def __init__(self):
#         # Existing vehicle parameters
#         self.battery_level = random.uniform(30, 100)
#         self.battery_health = random.uniform(85, 100)
#         self.motor_efficiency = random.uniform(90, 100)
#         self.tire_pressure = random.uniform(30, 35)
#         self.regenerative_energy = 0
#         self.distance_remaining = random.uniform(50, 300)
#         self.charging_rate = self.get_dynamic_charging_rate()
#         self.weather = random.choice(["sunny", "rainy", "snowy", "windy"])
#         self.traffic_condition = random.choice(["light", "moderate", "heavy"])
#         self.location = (random.uniform(10, 100), random.uniform(10, 100))
#         self.alerts = []

#         # Additional vehicle parameters
#         self.vehicle_id = random.randint(1000, 9999)
#         self.last_maintenance_check = datetime.datetime.now()
#         self.cloud_data = []
#         self.v2g_enabled = True
#         self.driving_mode = "Normal"
#         self.trip_data = []  # Trip energy consumption data
#         self.battery_temp = random.uniform(20, 40)  # Battery temperature in Celsius
#         self.energy_consumed = 0  # Energy consumed in kWh for each trip

#         # New parameters for additional features
#         self.geofenced_areas = [{"name": "Home", "location": (50, 50), "radius": 5}]
#         self.charging_schedule = []  # Schedule for charging
#         self.battery_swapping_stations = [{"station_name": "SwapStation1", "location": (60, 60)}]
#         self.reviews = []  # Reviews for charging stations

#     def get_dynamic_charging_rate(self):
#         return random.uniform(5, 25)

#     def get_nearest_charging_station(self):
#         return random.choice([
#             {"station_name": "ChargePoint", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Available", "price_per_kWh": random.uniform(0.1, 0.5)},
#             {"station_name": "Tesla Supercharger", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Busy", "price_per_kWh": random.uniform(0.1, 0.5)},
#         ])

#     def get_alerts(self):
#         alerts = []
#         if self.battery_level < 10:
#             alerts.append("Low battery! Consider charging.")
#         if self.battery_health < 75:
#             alerts.append("Battery health is low! Consider battery check.")
#         if self.tire_pressure < 30:
#             alerts.append("Tire pressure low! Check tires.")
#         return alerts

#     def battery_degradation_rate(self):
#         degradation_rate = random.uniform(1, 5)  # Mock degradation rate in % per year
#         return f"Battery degradation rate is {degradation_rate}% per year."

#     def calculate_eta(self):
#         average_speed = random.randint(50, 80)
#         eta_hours = self.distance_remaining / average_speed
#         eta = datetime.datetime.now() + datetime.timedelta(hours=eta_hours)
#         return eta.strftime("%H:%M:%S")

#     def store_data_in_cloud(self):
#         vehicle_data = {
#             "battery_level": self.battery_level,
#             "battery_health": self.battery_health,
#             "motor_efficiency": self.motor_efficiency,
#             "tire_pressure": self.tire_pressure,
#             "regenerative_energy": self.regenerative_energy,
#             "distance_remaining": self.distance_remaining,
#             "weather": self.weather,
#             "traffic_condition": self.traffic_condition,
#             "location": self.location
#         }
#         self.cloud_data.append(vehicle_data)
#         return "Data stored in cloud"

#     def suggest_driving_mode(self):
#         if self.traffic_condition == "heavy" or self.weather in ["rainy", "snowy"]:
#             self.driving_mode = "Eco Mode"
#         else:
#             self.driving_mode = "Sport Mode"
#         return self.driving_mode

#     def get_v2g_status(self):
#         if self.v2g_enabled:
#             return "V2G enabled. You can discharge energy to the grid during peak hours."
#         else:
#             return "V2G not available."

#     def route_planning_with_range_anxiety(self):
#         if self.distance_remaining < 50:
#             return "Route planning suggests a nearby charging station due to low range."
#         else:
#             return "Route planning optimal, no immediate charging required."

#     def dynamic_pricing_for_charging(self):
#         nearest_station = self.get_nearest_charging_station()
#         return f"Current price at {nearest_station['station_name']}: {nearest_station['price_per_kWh']} $/kWh"

#     def carbon_emission_offset(self):
#         emissions_saved = self.distance_remaining * 0.2
#         return f"Carbon emissions avoided: {emissions_saved} kg CO2"

#     def predictive_maintenance(self):
#         days_since_last_maintenance = (datetime.datetime.now() - self.last_maintenance_check).days
#         if days_since_last_maintenance > 90:
#             return "Time for a maintenance check!"
#         else:
#             return "No maintenance required."

#     def calculate_energy_consumed(self, distance):
#         self.energy_consumed = random.uniform(0.15, 0.25) * distance  # kWh per km
#         self.trip_data.append(self.energy_consumed)
#         return f"Energy consumed for this trip: {self.energy_consumed} kWh"

#     def battery_temperature_monitoring(self):
#         if self.battery_temp > 40:
#             return "Battery overheating! Adjust driving or stop charging."
#         elif self.battery_temp < 0:
#             return "Battery freezing! Move vehicle to a warmer area."
#         else:
#             return "Battery temperature is optimal."

#     def geofence_charging_optimization(self):
#         for area in self.geofenced_areas:
#             if self.is_within_geofence(area):
#                 return f"You are within the geofenced area '{area['name']}'. Consider charging here."
#         return "No geofenced areas detected."

#     def is_within_geofence(self, area):
#         distance_to_area = ((self.location[0] - area["location"][0]) ** 2 + (self.location[1] - area["location"][1]) ** 2) ** 0.5
#         return distance_to_area <= area["radius"]

#     def smart_charging_schedule(self):
#         # Example schedule for charging at night (off-peak hours)
#         self.charging_schedule.append({"time": "02:00", "duration": "3 hours"})
#         return "Charging scheduled for 2 AM for 3 hours."

#     def battery_swapping_station_integration(self):
#         nearest_station = random.choice(self.battery_swapping_stations)
#         return f"Nearest battery swapping station: {nearest_station['station_name']} at location {nearest_station['location']}."

#     def leave_review(self, station_name, review_text):
#         self.reviews.append({"station_name": station_name, "review": review_text})
#         return f"Review left for {station_name}: {review_text}"

#     def get_reviews(self):
#         return self.reviews if self.reviews else "No reviews available for charging stations."

# # Mock use case with new features
# def main():
#     ev = ElectricVehicle()

#     # Collect and print EV data
#     current_data = {
#         "battery_level": ev.battery_level,
#         "battery_health": ev.battery_health,
#         "battery_degradation_rate": ev.battery_degradation_rate(),
#         "motor_efficiency": ev.motor_efficiency,
#         "tire_pressure": ev.tire_pressure,
#         "battery_temperature_monitoring": ev.battery_temperature_monitoring(),
#         "energy_consumed": ev.calculate_energy_consumed(50),  # Example for 50 km trip
#         "nearest_charging_station": ev.get_nearest_charging_station(),
#         "dynamic_pricing": ev.dynamic_pricing_for_charging(),
#         "v2g_status": ev.get_v2g_status(),
#         "driving_mode": ev.suggest_driving_mode(),
#         "carbon_offset": ev.carbon_emission_offset(),
#         "eta": ev.calculate_eta(),
#         "predictive_maintenance": ev.predictive_maintenance(),
#         "cloud_data_storage": ev.store_data_in_cloud(),
#         "geofence_charging_optimization": ev.geofence_charging_optimization(),
#         "smart_charging_schedule": ev.smart_charging_schedule(),
#         "battery_swapping_station": ev.battery_swapping_station_integration(),
#         "reviews": ev.get_reviews(),
#     }
#     print(json.dumps(current_data, indent=2))

#     # Example usage of leaving a review
#     ev.leave_review("ChargePoint", "Great service and fast charging!")
#     ev.leave_review("Tesla Supercharger", "Very busy but worth the wait.")

# if __name__ == "__main__":
#     main()



more and more features- 

import random
import datetime
import json
import requests

class ElectricVehicle:
    def __init__(self):
        # Existing vehicle parameters
        self.battery_level = random.uniform(30, 100)
        self.battery_health = random.uniform(85, 100)
        self.motor_efficiency = random.uniform(90, 100)
        self.tire_pressure = random.uniform(30, 35)
        self.regenerative_energy = 0
        self.distance_remaining = random.uniform(50, 300)
        self.charging_rate = self.get_dynamic_charging_rate()
        self.weather = self.get_weather_data()
        self.traffic_condition = self.get_traffic_data()
        self.location = (random.uniform(10, 100), random.uniform(10, 100))
        self.alerts = []

        # Additional vehicle parameters
        self.vehicle_id = random.randint(1000, 9999)
        self.last_maintenance_check = datetime.datetime.now()
        self.cloud_data = []
        self.v2g_enabled = True
        self.driving_mode = "Normal"
        self.trip_data = []  # Trip energy consumption data
        self.battery_temp = random.uniform(20, 40)  # Battery temperature in Celsius
        self.energy_consumed = 0  # Energy consumed in kWh for each trip

        # New parameters for additional features
        self.geofenced_areas = [{"name": "Home", "location": (50, 50), "radius": 5}]
        self.charging_schedule = []  # Schedule for charging
        self.battery_swapping_stations = [{"station_name": "SwapStation1", "location": (60, 60)}]
        self.reviews = []  # Reviews for charging stations

    def get_dynamic_charging_rate(self):
        return random.uniform(5, 25)

    def get_weather_data(self):
        # Example API call (mocked for this case)
        return random.choice(["sunny", "rainy", "snowy", "windy"])

    def get_traffic_data(self):
        # Example API call (mocked for this case)
        return random.choice(["light", "moderate", "heavy"])

    def get_nearest_charging_station(self):
        return random.choice([
            {"station_name": "ChargePoint", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Available", "price_per_kWh": random.uniform(0.1, 0.5)},
            {"station_name": "Tesla Supercharger", "location": (random.uniform(10, 100), random.uniform(10, 100)), "availability": "Busy", "price_per_kWh": random.uniform(0.1, 0.5)},
        ])

    def get_alerts(self):
        alerts = []
        if self.battery_level < 10:
            alerts.append("Low battery! Consider charging.")
        if self.battery_health < 75:
            alerts.append("Battery health is low! Consider battery check.")
        if self.tire_pressure < 30:
            alerts.append("Tire pressure low! Check tires.")
        return alerts

    def battery_degradation_rate(self):
        degradation_rate = random.uniform(1, 5)  # Mock degradation rate in % per year
        return f"Battery degradation rate is {degradation_rate}% per year."

    def calculate_eta(self):
        average_speed = random.randint(50, 80)
        eta_hours = self.distance_remaining / average_speed
        eta = datetime.datetime.now() + datetime.timedelta(hours=eta_hours)
        return eta.strftime("%H:%M:%S")

    def store_data_in_cloud(self):
        vehicle_data = {
            "battery_level": self.battery_level,
            "battery_health": self.battery_health,
            "motor_efficiency": self.motor_efficiency,
            "tire_pressure": self.tire_pressure,
            "regenerative_energy": self.regenerative_energy,
            "distance_remaining": self.distance_remaining,
            "weather": self.weather,
            "traffic_condition": self.traffic_condition,
            "location": self.location
        }
        self.cloud_data.append(vehicle_data)
        return "Data stored in cloud"

    def suggest_driving_mode(self):
        if self.traffic_condition == "heavy" or self.weather in ["rainy", "snowy"]:
            self.driving_mode = "Eco Mode"
        else:
            self.driving_mode = "Sport Mode"
        return self.driving_mode

    def get_v2g_status(self):
        if self.v2g_enabled:
            return "V2G enabled. You can discharge energy to the grid during peak hours."
        else:
            return "V2G not available."

    def route_planning_with_range_anxiety(self):
        if self.distance_remaining < 50:
            return "Route planning suggests a nearby charging station due to low range."
        else:
            return "Route planning optimal, no immediate charging required."

    def dynamic_pricing_for_charging(self):
        nearest_station = self.get_nearest_charging_station()
        return f"Current price at {nearest_station['station_name']}: {nearest_station['price_per_kWh']} $/kWh"

    def carbon_emission_offset(self):
        emissions_saved = self.distance_remaining * 0.2
        return f"Carbon emissions avoided: {emissions_saved} kg CO2"

    def predictive_maintenance(self):
        days_since_last_maintenance = (datetime.datetime.now() - self.last_maintenance_check).days
        if days_since_last_maintenance > 90:
            return "Time for a maintenance check!"
        else:
            return "No maintenance required."

    def calculate_energy_consumed(self, distance):
        self.energy_consumed = random.uniform(0.15, 0.25) * distance  # kWh per km
        self.trip_data.append(self.energy_consumed)
        return f"Energy consumed for this trip: {self.energy_consumed} kWh"

    def battery_temperature_monitoring(self):
        if self.battery_temp > 40:
            return "Battery overheating! Adjust driving or stop charging."
        elif self.battery_temp < 0:
            return "Battery freezing! Move vehicle to a warmer area."
        else:
            return "Battery temperature is optimal."

    def geofence_charging_optimization(self):
        for area in self.geofenced_areas:
            if self.is_within_geofence(area):
                return f"You are within the geofenced area '{area['name']}'. Consider charging here."
        return "No geofenced areas detected."

    def is_within_geofence(self, area):
        distance_to_area = ((self.location[0] - area["location"][0]) ** 2 + (self.location[1] - area["location"][1]) ** 2) ** 0.5
        return distance_to_area <= area["radius"]

    def smart_charging_schedule(self):
        # Example schedule for charging at night (off-peak hours)
        self.charging_schedule.append({"time": "02:00", "duration": "3 hours"})
        return "Charging scheduled for 2 AM for 3 hours."

    def battery_swapping_station_integration(self):
        nearest_station = random.choice(self.battery_swapping_stations)
        return f"Nearest battery swapping station: {nearest_station['station_name']} at location {nearest_station['location']}."

    def leave_review(self, station_name, review_text):
        self.reviews.append({"station_name": station_name, "review": review_text})
        return f"Review left for {station_name}: {review_text}"

    def get_reviews(self):
        return self.reviews if self.reviews else "No reviews available for charging stations."

    def get_statistics(self):
        # Collect statistics for startup analytics
        return {
            "battery_level": self.battery_level,
            "battery_health": self.battery_health,
            "energy_consumed": self.energy_consumed,
            "trips": len(self.trip_data),
            "alerts": self.get_alerts(),
        }

# Mock use case with new features
def main():
    ev = ElectricVehicle()

    # Collect and print EV data
    current_data = {
        "battery_level": ev.battery_level,
        "battery_health": ev.battery_health,
        "battery_degradation_rate": ev.battery_degradation_rate(),
        "motor_efficiency": ev.motor_efficiency,
        "tire_pressure": ev.tire_pressure,
        "battery_temperature_monitoring": ev.battery_temperature_monitoring(),
        "energy_consumed": ev.calculate_energy_consumed(50),  # Example for 50 km trip
        "nearest_charging_station": ev.get_nearest_charging_station(),
        "dynamic_pricing": ev.dynamic_pricing_for_charging(),
        "v2g_status": ev.get_v2g_status(),
        "driving_mode": ev.suggest_driving_mode(),
        "carbon_offset": ev.carbon_emission_offset(),
        "eta": ev.calculate_eta(),
        "predictive_maintenance": ev.predictive_maintenance(),
        "cloud_data_storage": ev.store_data_in_cloud(),
        "geofence_charging_optimization": ev.geofence_charging_optimization(),
        "smart_charging_schedule": ev.smart_charging_schedule(),
        "battery_swapping_station": ev.battery_swapping_station_integration(),
        "statistics": ev.get_statistics(),
    }
    print(json.dumps(current_data, indent=2))

    # Example usage of leaving a review
    ev.leave_review("ChargePoint", "Great service and fast charging!")
    print(ev.get_reviews())

if __name__ == "__main__":
    main()
