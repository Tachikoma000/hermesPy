import threading
from queue import Queue
import time
import pandas as pd
import statistics
import tabulate
import pandas as pd

# Define the global queue for communication
global_queue = Queue()

# Define the headers for the processed data DataFrame
headers = ["Timestamp", "Temperature (C)", "Pressure (Pa)", "Voltage (V)"]

# Initialize an empty DataFrame for processed data
processed_data_df = pd.DataFrame(columns=['timestamp', 'temperature_mean', 'pressure_mean', 'voltage_mean'])

# Define the processed data queue for communication
processed_data_queue = Queue()

def data_processor(global_queue, processed_data_df):
    temperature_mean = 0
    pressure_mean = 0
    voltage_mean = 0
    temperature_count = 0
    pressure_count = 0
    voltage_count = 0

    while True:
        data = global_queue.get()
        data_type, data_value, timestamp = data
        if data_type == 'temperature':
            temperature_mean = (temperature_mean * temperature_count + data_value) / (temperature_count + 1)
            temperature_count += 1
        elif data_type == 'pressure':
            pressure_mean = (pressure_mean * pressure_count + data_value) / (pressure_count + 1)
            pressure_count += 1
        elif data_type == 'voltage':
            voltage_mean = (voltage_mean * voltage_count + data_value) / (voltage_count + 1)
            voltage_count += 1

        print(f"Temperature Mean: {temperature_mean}")
        print(f"Pressure Mean: {pressure_mean}")
        print(f"Voltage Mean: {voltage_mean}")

        # Add processed data to the processed_data_df DataFrame
        processed_data = {'timestamp': timestamp, 'temperature_mean': temperature_mean, 'pressure_mean': pressure_mean, 'voltage_mean': voltage_mean}
        processed_data_df.loc[len(processed_data_df)] = processed_data
        
def print_table():
    """
    Print a table of the last 10 processed data items.
    """
    # Define CSV headers
    headers = ["Timestamp", "Temperature (C)", "Pressure (Pa)", "Voltage (V)"]

    while True:
        # Get the last 10 items from the processed data queue
        data_list = []
        temp_queue = Queue()
        while processed_data_queue.qsize() < 10:
            time.sleep(0.1)
        for i in range(processed_data_queue.qsize()):
            data = processed_data_queue.get()
            temp_queue.put(data)
            data_list.append(data)

        # Move the items back to the original queue
        while not temp_queue.empty():
            processed_data_queue.put(temp_queue.get())

        # Print the table
        print(tabulate(data_list[-10:], headers=headers, tablefmt="pretty"))
