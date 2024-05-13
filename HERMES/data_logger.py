import threading
import csv
from queue import Queue
import time
import prettytable 
from prettytable import PrettyTable
from tabulate import tabulate
from data_processor import processed_data_queue

# Define the global queue for communication
global_queue = Queue()

start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
end_time = ""

metadata = ["Data description: HERMES data log",
            "Acquisition start time: " + str(start_time),
            "Acquisition end time: " + str(end_time)]

# Define the processed data queue for communication
# processed_data_queue = Queue()

def data_logging(processed_data_queue):
    """
    Log aggregated and processed data to a CSV file with headers and metadata.
    """
    # Define CSV file path
    file_path = 'data.csv'
    
    # Define CSV headers
    headers = ["Timestamp", "Temperature (C)", "Pressure (Pa)", "Voltage (V)"]
    
    # Create and open CSV file for writing
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write metadata to the first row of the CSV file
        writer.writerow(metadata)
        
        # Write headers to the second row of the CSV file
        writer.writerow(headers)
        
        # Create a lock to ensure that only one thread modifies the processed_data_queue at a time
        lock = threading.Lock()
        
        while True:
            # Get data from the processed data queue
            with lock:
                if not processed_data_queue.empty():
                    data = processed_data_queue.get()
                else:
                    continue
            
            # Format data as a row in the CSV file
            row = [data[0], f"{data[1]:.2f}", f"{data[2]:.2f}", f"{data[3]:.2f}"]
            
            # Write data to the CSV file
            writer.writerow(row)
            print(row)

def print_table(processed_data_queue):
    """
    Print a table of the last 10 processed data items and new data as it arrives.
    """
    # Define CSV headers
    headers = ["Timestamp", "Temperature (C)", "Pressure (Pa)", "Voltage (V)"]

    # Create an empty PrettyTable object with headers
    table = PrettyTable(headers)

    # Add a short delay before trying to get data from the queue
    time.sleep(1)

    while True:
        print("Processing data queue size:", processed_data_queue.qsize())
        # Get the last 10 items from the processed data queue
        data_list = []
        while processed_data_queue.qsize() < 10:
            time.sleep(0.1)
        for i in range(10):
            data = processed_data_queue.get()
            data_list.append(data)

        # If there is enough data, print the table
        if len(data_list) == 10:
            print(tabulate(data_list, headers=headers, tablefmt="pretty"))



if __name__ == '__main__':
    # Start the data logging thread
    logging_thread = threading.Thread(target=data_logging, args=(processed_data_queue,))
    logging_thread.start()
    
    # Start the table printing thread
    table_thread = threading.Thread(target=print_table, args=(processed_data_queue,))
    table_thread.start()
