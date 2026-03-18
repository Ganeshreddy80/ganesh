user = input("Enter username: ")
password = int(input("Enter password: "))

if user == "sunny" and password == 995910:
    print("\nLogin Successful.\n")

    building_count = int(input("Enter number of buildings to analyze: "))
    energy_readings = []

    for i in range(building_count):
        reading_value = int(input(f"Enter reading for building {i+1}: "))
        energy_readings.append(reading_value)

    valid_readings = [val for val in energy_readings if val >= 0]
    total_energy = sum(valid_readings)

    energy_categories = {
        "efficient": [val for val in energy_readings if 0 <= val <= 50],
        "moderate": [val for val in energy_readings if 51 <= val <= 150],
        "high": [val for val in energy_readings if val > 150],
        "invalid": [val for val in energy_readings if val < 0]
    }

    total_buildings = len(energy_readings)
    summary = (total_energy, total_buildings)

    high_usage_count = len(energy_categories["high"])
    efficient_count = len(energy_categories["efficient"])
    moderate_count = len(energy_categories["moderate"])

    if total_energy > 600:
        conclusion = "Energy Waste Detected. The electricity board is not happy."
    elif high_usage_count > 3:
        conclusion = "Overconsumption detected. Too much power usage."
    elif (efficient_count - moderate_count <= 1) and (moderate_count - efficient_count <= 1):
        conclusion = "Balanced usage. Everything looks under control."
    elif efficient_count > max(moderate_count, high_usage_count):
        conclusion = "Efficient campus. Good job managing energy."
    else:
        conclusion = "Moderate usage. Nothing unusual."

    print("Energy usage classification:")
    for category, values in energy_categories.items():
        print(f"{category} buildings: {values}")

    print("\nTotal energy consumed:", summary[0])
    print("Number of buildings analyzed:", summary[1])
    print("System Conclusion:", conclusion)

else:
    print("\nInvalid login. Access denied.")
