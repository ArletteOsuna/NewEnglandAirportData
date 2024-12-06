"""
Class: CS230--1
Name: Arlette Osuna
Description: Assignment 4 - the purpose of this program is to build a weather
analysis tool and collects weather data from various cities.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import os


def read_states(file_path):
    state_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            state_full, state_abbr = line.strip().split(', ')
            # Store both lowercase keys for case-insensitive matching
            state_dict[state_abbr.lower()] = state_full
            state_dict[state_full.lower()] = state_full
    return state_dict


def read_weather_files(folder_path, state_dict):
    weather_data = {}
    for filename in os.listdir(folder_path):
        # Skip non-weather files and the state file
        if not filename.endswith('.txt') or filename == 'us_states.txt':
            continue
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                parts = line.split(', ')
                if len(parts) != 4:  # Validate line format
                    print(f"Skipping malformed line {line_number} in file {filename}: {line}")
                    continue
                try:
                    city, state, avg_temp, avg_hum = parts
                    avg_temp = float(avg_temp.split()[0])  # Remove 'F' and convert to float
                    avg_hum = float(avg_hum[:-1])  # Remove '%' and convert to float
                except (ValueError, IndexError) as e:
                    print(f"Error parsing line {line_number} in file {filename}: {line} ({e})")
                    continue

                # Normalize state to lowercase
                state = state.lower()
                if state in state_dict:
                    state_full = state_dict[state]  # Convert to full state name
                else:
                    continue

                # Add data to weather_data
                if state_full not in weather_data:
                    weather_data[state_full] = {'temperatures': [], 'humidities': []}
                weather_data[state_full]['temperatures'].append(avg_temp)
                weather_data[state_full]['humidities'].append(avg_hum)
    return weather_data


def calculate_weather_statistics(weather_data):
    weather_stats = {}
    for state, data in weather_data.items():
        temps = data['temperatures']
        hums = data['humidities']
        weather_stats[state] = {
            'MaxTemperature': max(temps),
            'MinTemperature': min(temps),
            'AverageTemperature': sum(temps) / len(temps),
            'MaxHumidity': max(hums),
            'MinHumidity': min(hums),
            'AverageHumidity': sum(hums) / len(hums),
        }
    return weather_stats


def show_weather_information(states, weather_stats, state_dict):
    print("\nWeather Information:\n")
    print(f"{'State':<15}{'Max Temp (F)':<15}{'Min Temp (F)':<15}{'Avg Temp (F)':<15}"
          f"{'Max Hum (%)':<15}{'Min Hum (%)':<15}{'Avg Hum (%)':<15}")

    # Separate states with and without data
    states_with_data = []
    states_no_data = []

    for state in states:
        # Normalize input to handle abbreviations and case insensitivity
        state = state.strip().lower()
        if state in state_dict:
            state_full = state_dict[state]
        else:
            state_full = state.title()
            states_no_data.append(state_full)
            continue
        if state_full in weather_stats:
            states_with_data.append((state_full, weather_stats[state_full]))
        else:
            states_no_data.append(state_full)

    # Display states with data first
    for state_full, stats in states_with_data:
        print(f"\n{state_full:<15}{stats['MaxTemperature']:<15.2f}{stats['MinTemperature']:<15.2f}"
              f"{stats['AverageTemperature']:<15.2f}{stats['MaxHumidity']:<15.2f}"
              f"{stats['MinHumidity']:<15.2f}{stats['AverageHumidity']:<15.2f}")

    # Display "No data available" for states without data
    for state_full in states_no_data:
        print(f"\n{state_full:<15}No data available")


def main():
    # Folder path containing all data files
    folder_path = 'weather_data'
    state_file = 'weather_data/us_states.txt'

    # Read states and weather data
    state_dict = read_states(state_file)
    weather_data = read_weather_files(folder_path, state_dict)

    # Calculate weather statistics
    weather_stats = calculate_weather_statistics(weather_data)

    # Get user input for states
    user_input = input("Enter states (full name or abbreviation, separated by commas): ")
    states = user_input.split(',')

    # Show weather information
    show_weather_information(states, weather_stats, state_dict)


if __name__ == "__main__":
    main()
