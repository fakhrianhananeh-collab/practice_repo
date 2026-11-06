"""Flag feverish readings in a list of ward temperatures."""
import pandas as pd

THRESHOLD = 37.8     # degrees Celsius: this value and above counts as a fever

readings = pd.read_csv("ward_temperatures.csv")
readings["fever"] = readings["temperature_c"] >= THRESHOLD

print(readings)
print(f"{readings['fever'].sum()} of {len(readings)} readings are feverish")
print(len(readings), "readings read")