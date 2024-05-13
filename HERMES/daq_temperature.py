import random
import time
import threading
import queue
from queue import Queue

global global_queue
global_queue = queue.Queue()

def simulate_temperature_data(global_queue):
    while True:
        time.sleep(1)
        data = ('temperature', random.randint(0, 100), time.time())
        print("Acquired temperature data:", data[1])
        global_queue.put(data)
