"""Flag feverish readings in a list of ward temperatures."""
import pandas as pd

THRESHOLD = 37.5    # degrees Celsius: this value and above counts as a fever

readings = pd.read_csv("ward_temperatures.csv")
readings["fever"] = readings["temperature_c"] >= THRESHOLD

print(readings)
print(f"Patients checked: {len(readings)}")
print(f"Patients with feverish temperatures: {readings['fever'].sum()}")
print(len(readings), "readings read")