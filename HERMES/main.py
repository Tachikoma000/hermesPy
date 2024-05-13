import queue
import threading
from daq_pressure import simulate_pressure_data
from daq_temperature import simulate_temperature_data
from daq_voltage import simulate_voltage_data
from data_processor import data_processor
from data_logger import data_logging, print_table
from data_processor import processed_data_queue, processed_data_df

# Define global queue for communication
global_queue = queue.Queue()

# Create threads for data acquisition processes
temperature_thread = threading.Thread(target=simulate_temperature_data, args=(global_queue,))
pressure_thread = threading.Thread(target=simulate_pressure_data, args=(global_queue,))
voltage_thread = threading.Thread(target=simulate_voltage_data, args=(global_queue,))

# Start the threads
temperature_thread.start()
pressure_thread.start()
voltage_thread.start()

# Start the data processing and logging threads
data_processor_thread = threading.Thread(target=data_processor, args=(global_queue, processed_data_df))
data_processor_thread.start()

data_logging_thread = threading.Thread(target=data_logging, args=(processed_data_queue,))
data_logging_thread.start()

# Start the table printing thread
table_thread = threading.Thread(target=print_table, args=(processed_data_queue,))
table_thread.start()
