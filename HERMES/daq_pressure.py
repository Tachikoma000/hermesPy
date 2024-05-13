import random
import time
import threading
import queue
from queue import Queue

global global_queue
global_queue = queue.Queue()

def simulate_pressure_data(global_queue):
    while True:
        time.sleep(1)
        data = ('pressure', random.randint(0, 100), time.time())
        print("Acquired pressure data:", data[1])
        global_queue.put(data)
