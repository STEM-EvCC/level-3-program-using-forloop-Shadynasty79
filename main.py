# Sample data
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Initialize counters and lists
total_missions = 0
successful_missions = 0
missions_before_2000 = []

# Iterate through the list of missions
for i in range(len(mission_names)):
    total_missions += 1  # Count each mission
    if mission_success[i]:
        successful_missions += 1  # Count successful missions
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])  # List missions before 2000

# Calculate success rate
success_rate = (successful_missions / total_missions) * 100

# Output the results
print(f"Total number of missions: {total_missions}")
print(f"Number of successful missions: {successful_missions}")
print(f"Success rate: {success_rate:.2f}%")
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(f"- {mission}")
