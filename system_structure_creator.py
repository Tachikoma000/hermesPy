import os

# create project directory
os.makedirs('HERMES')
os.chdir('HERMES')

# create data directory
os.makedirs('data')

# create Python files
with open('daq_temperature.py', 'w') as f:
    f.write('# TODO: add code for temperature data acquisition')

with open('daq_pressure.py', 'w') as f:
    f.write('# TODO: add code for pressure data acquisition')

with open('daq_voltage.py', 'w') as f:
    f.write('# TODO: add code for voltage data acquisition')

with open('data_aggregator.py', 'w') as f:
    f.write('# TODO: add code for data aggregation')

with open('data_processor.py', 'w') as f:
    f.write('# TODO: add code for data processing')

with open('data_logger.py', 'w') as f:
    f.write('# TODO: add code for data logging')

with open('main.py', 'w') as f:
    f.write('# TODO: add code for main function')
