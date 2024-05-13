import random
import time
import threading
import queue
from queue import Queue

global global_queue
global_queue = queue.Queue()

def simulate_voltage_data(global_queue):
    while True:
        time.sleep(1)
        data = ('voltage', random.randint(0, 100), time.time())
        print("Acquired voltage data:", data[1])
        global_queue.put(data)
