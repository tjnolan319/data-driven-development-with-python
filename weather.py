import os

def read_states(file_path):
    state_dict = {}
    with open(file_path, 'r') as us_states:
        for line in us_states:
            section = line.strip().split(", ")
            if len(section) == 2:
                fullstatename, abbreviation = section
                state_dict[abbreviation.lower()] = fullstatename.lower()
    return state_dict


def read_weather_files(folder_path, state_dict):
    weather_data = {}
    city_weather_list = []

    weather_files = os.listdir(folder_path)

    for file_name in weather_files:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r') as citiesweather:
            for line in citiesweather:
                city_weather_list.append(line.strip())
                section = line.strip().split(", ")
                if len(section) == 4:
                    city, state, tempstring, humstring = section
                    temp = float(tempstring.split()[0])
                    hum = float(humstring.split()[0].replace('%', ''))
                    full_state_name = state_dict.get(state.lower(), state).title()

                    if full_state_name not in weather_data:
                        weather_data[full_state_name] = {
                            "temperatures": [],
                            "humidities": [] }

                    weather_data[full_state_name]["temperatures"].append(temp)
                    weather_data[full_state_name]["humidities"].append(hum)

    return weather_data, city_weather_list


def calculate_weather_statistics(weather_data):
    weather_stats = {}
    for state, data in weather_data.items():
        temps = data["temperatures"]
        hums = data["humidities"]
        max_temp = max(temps)
        min_temp = min(temps)
        avg_temp = round(sum(temps) / len(temps), 2) if temps else 0
        max_hum = max(hums)
        min_hum = min(hums)
        avg_hum = round(sum(hums) / len(hums), 2) if hums else 0

        weather_stats[state] = {
            "max_temp": max_temp,
            "min_temp": min_temp,
            "avg_temp": avg_temp,
            "max_hum": max_hum,
            "min_hum": min_hum,
            "avg_hum": avg_hum
        }
    return weather_stats


def show_weather_information(states, weather_stats, state_dict, city_weather_list):

    userinput = [state.strip().lower() for state in states.split(",")]

    states_with_data = []
    states_without_data = []

    # Process through the input list and categorize the states
    for state in userinput:
        if len(state) == 2:  #Abbreviations
            full_state_name = state_dict.get(state)
            if full_state_name is not None:
                full_state_name = full_state_name.title()
        else:  # Full states name
            full_state_name = ' '.join(word.title() for word in state.strip().split())

        # Check if the state exists in weather_stats
        if full_state_name in weather_stats:
            states_with_data.append(full_state_name)
        else:
            states_without_data.append(full_state_name)

    # Header
    print(

        f"{'State':<20}{'Max Temp (F)':^20}{'Min Temp (F)':^20}{'Avg Temp (F)':^20}{'Max Hum (%)':^20}{'Min Hum (%)':^20}{'Avg Hum (%)':^20}"
    )

    for full_state_name in states_with_data:
        weather = weather_stats[full_state_name]

        print(
            f"{full_state_name:<20}"
            f"{weather['max_temp']:^20.2f}"
            f"{weather['min_temp']:^20.2f}"
            f"{weather['avg_temp']:^20.2f}"
            f"{weather['max_hum']:^20.2f}"
            f"{weather['min_hum']:^20.2f}"
            f"{weather['avg_hum']:^20.2f}"
        )

    # Print states with no data available at the end
    for full_state_name in states_without_data:
        print(f"{full_state_name:<20}No data available{' ' * 50}")





def main():
    currentpath = os.getcwd()
    folder_path = os.path.join(currentpath, "weather_data")

    state_file = "us_states.txt"
    state_dict = read_states(state_file)

    weather_data, city_weather_list = read_weather_files(folder_path, state_dict)
    weather_stats = calculate_weather_statistics(weather_data)

    userinput = input("Enter states (full name or abbreviation, separated by commas): ")
    print("Weather Information:")
    show_weather_information(userinput, weather_stats, state_dict, city_weather_list)


main()






