# 🌦️ Weather Data Analysis Tool

This Python script allows users to analyze temperature and humidity data by U.S. state. It reads weather data from a directory of city-level files and maps them to state-level statistics including max, min, and average temperature and humidity. Users can input any combination of state names or abbreviations and receive a clean, formatted report.

---

## 📁 Project Structure

```
├── us_states.txt                 # Contains state names and their abbreviations
├── weather_data/                # Folder containing weather data files (e.g., city_weather.txt)
│   ├── city1_weather.txt
│   └── ...
├── weather_script.py            # Main Python script (this file)
```

---

## ⚙️ How It Works

1. **Reads U.S. states and abbreviations** from `us_states.txt`
2. **Processes weather files** in a specified folder (`weather_data/`)
3. **Calculates weather statistics** (max, min, avg for temp and humidity) by state
4. **Accepts user input** for any number of states (abbreviated or full name)
5. **Displays results** in a clean, tabular format in the console

---

## 💡 Example Input

```bash
Enter states (full name or abbreviation, separated by commas): NY, California, TX
```

## 📊 Example Output

```
State               Max Temp (F)       Min Temp (F)       Avg Temp (F)       Max Hum (%)        Min Hum (%)        Avg Hum (%)
New York               85.20              65.00              74.35              90.00              40.00              65.50
California             102.00             66.50              81.25              70.00              30.00              50.50
Texas                  99.00              70.00              82.60              80.00              50.00              67.40
```

States without data will be listed at the end as:  
`Florida             No data available`

---

## 🛠️ Technologies Used

- Python 3.x
- Standard libraries: `os`

---

## 📝 Notes

- All state abbreviations are case-insensitive.
- Data must be formatted correctly in each weather file:  
  `City, State, Temperature (F), Humidity (%)`

---

## 🚀 How to Run

```bash
python weather_script.py
```

Make sure the working directory includes:
- `us_states.txt`
- A folder named `weather_data/` with properly formatted weather files

---

## 📬 Contact

Created by **Tim Nolan**  
For questions or suggestions, feel free to connect on [LinkedIn](https://www.linkedin.com/in/tjnolan319/)
