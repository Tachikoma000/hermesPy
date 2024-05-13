# HermesPy : Queued State Machine Producer-Consumer (QSM-PC) Architecture Implementation in Python

HERMES is a Python project that implements the Queued State Machine Producer-Consumer (QSM-PC) architecture for simulating data acquisition, aggregation, processing, and logging. The project aims to simulate three parallel data acquisition processes (temperature, pressure, voltage) and includes an aggregator, a data processor for basic statistical analysis, and a data logging processor that saves the data to a CSV file.

For questions or feature requests, please contact 0xtachi@gmail.com. As an independent researcher, I built this project purely for the joy of creating something both enjoyable and practical. If you love to tinker and build innovative control systems, feel free to email me!

## Table of Contents

- [Project Objective](#project-objective)
- [Fundamentals of the system](#fundamentals-of-the-system)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [How to Run the system](#how-to-run-the-system)
- [Project Structure](#project-structure)
- [Conclusion](#conclusion)

## Project Objective

The objective of the HERMES project is to implement the QSM-PC architecture in Python to simulate data acquisition, aggregation, processing, and logging. Specifically, the project aims to accomplish the following:

- Simulate three parallel data acquisition processes (temperature, pressure, voltage).
- Aggregate and process the acquired data into time series.
- Perform basic statistical analysis on the processed data.
- Log the aggregated and processed data to a CSV file.

## Fundamentals of the system

The Queued State Machine Producer-Consumer (QSM-PC) architecture is a design pattern that allows for efficient processing of large amounts of data in a parallel and asynchronous manner.

In the QSM-PC architecture, the data acquisition is done by producer threads that acquire data from different sources and add it to a global queue. Then, the consumer threads read from the queue and perform the necessary processing tasks, such as data aggregation, statistical analysis, and logging.

The use of a queue in the QSM-PC architecture allows for efficient and scalable data transfer between different threads. The queue ensures that the processing tasks are executed in the order that the data was acquired, while allowing for multiple threads to process the data in parallel.

Overall, the QSM-PC architecture provides a flexible and scalable framework for processing large amounts of data in a parallel and asynchronous manner, making it ideal for real-time data acquisition and analysis applications.

In the context of Python, the Queued State Machine Producer-Consumer (QSM-PC) architecture is a design pattern that facilitates efficient communication and coordination between different processes or threads. This pattern is implemented in the HERMES project to simulate data acquisition, aggregation, processing, and logging.

In QSM-PC, each process or thread is treated as a state machine that operates on a queue of inputs and outputs. The producer process or thread generates the inputs and puts them in a queue, while the consumer process or thread retrieves the inputs from the queue and generates the outputs. The state of the system is defined by the contents of the input and output queues.

In the HERMES project, the three data acquisition processes (temperature, pressure, and voltage) act as producers, while the aggregator, data processor, and data logging processor act as consumers. The producer threads simulate the data acquisition by generating random data and putting it into a global queue. The aggregator thread retrieves the data from the global queue and aggregates it into time series. The data processor thread retrieves the aggregated data and performs basic statistical analysis on it. The data logging processor thread retrieves the processed data and logs it to a CSV file.

By implementing the QSM-PC architecture, the HERMES project achieves parallel processing and efficient communication between different processes or threads. This allows the project to simulate the data acquisition, aggregation, processing, and logging in a highly efficient and scalable way.

## Prerequisites

To run the HERMES project, you need to have the following Python packages installed:

- queue
- threading
- csv
- time
- datetime
- pandas
- prettytable
- tabulate

## Getting Started

To get started with HERMES, you can follow these steps:

- Clone the repository to your local machine.
- Install the required Python packages.
- Open a terminal or command prompt and navigate to the project directory.
- Run the main script by executing python main.py.

## How to Run the system

- To run the HERMES project, follow these steps: `git clone https://github.com/YOUR-USERNAME/HermesPy.git`

- Clone the repository to your local machine: `cd HermesPy`

- Navigate to the project directory:  `pip install pandas prettytable tabulate`

- Install the required Python packages: `pip install pandas prettytable tabulate`

- Run the main script by executing python main.py: `python main.py`

- The program will run until you stop it with Ctrl+C. The processed data will be logged to a CSV file called data.csv, and a table of the last 10 processed data items will be printed to the console.

## Project Structure

The HERMES project follows the following file structure:

- `main.py`: Main script that runs the project and creates threads for the DAQs, aggregator, data processor, and data logging processor.
- `daq_temperature.py, daq_pressure.py, daq_voltage.py`: Separate threads that simulate the data acquisition process for each type of data.
- `data_aggregator.py`: Separate thread that aggregates the data from the DAQs into time series.
- `data_processor.py`: Separate thread that processes the aggregated data by performing basic statistical analysis.
- `data_logger.py`: Separate thread that logs the aggregated and processed data to a CSV file and prints a table of the last 10 processed data items.
- `processed_data.csv`: CSV file that stores the logged data.
- `README.md`: Project documentation that provides an overview of the project, instructions on how to set up and run the project, and a detailed outline of the project structure.

## Conclusion
HERMES is a Python project that demonstrates the implementation of the QSM-PC architecture for simulating data acquisition, aggregation, processing, and logging. It provides an example of how to use Python packages like `queue`, `threading`, `csv`, `time`, and `datetime` to achieve parallel processing and efficient data communication between different processes.
