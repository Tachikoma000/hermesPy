import threading
from queue import Queue
import time
from datetime import datetime

# Define the global queue for communication
global_queue = Queue()

def data_aggregator():
    """
    Aggregate data from the global queue into time series data with a global timestamp.
    """
    # Define global timestamp
    global_timestamp = time.time()

    # Initialize empty data lists
    data_list = []

    while True:
        # Get data from the global queue
        data = global_queue.get()
        
        # Append data to the data list
        data_list.append((data[0], data[1], global_timestamp))

        # Check if data lists are complete and process the data
        temperature_data = [x for x in data_list if x[0] == 'temperature']
        pressure_data = [x for x in data_list if x[0] == 'pressure']
        voltage_data = [x for x in data_list if x[0] == 'voltage']
        
        if len(temperature_data) >= 10 and len(pressure_data) >= 10 and len(voltage_data) >= 10:
            # Process data
            temperature_mean = sum([x[1] for x in temperature_data[-10:]])/10
            pressure_mean = sum([x[1] for x in pressure_data[-10:]])/10
            voltage_mean = sum([x[1] for x in voltage_data[-10:]])/10
            processed_data = [(global_timestamp, temperature_mean, pressure_mean, voltage_mean)]
            
            # Put processed data to global queue
            global_queue.put(processed_data[0])
            
            # Update global timestamp
            global_timestamp = time.time()

