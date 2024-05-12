# Plugjuice
Setup of the Project:<br />
git clone https://github.com/Gaston202/Plugjuice.git<br />
cd Plugjuice<br />

# Software Dependencies:
Raspberry Pi OS (formerly Raspbian): Install the Raspberry Pi OS Lite version on your microSD card. You can download it from the official Raspberry Pi website.<br />

Python: Make sure Python is installed on your Raspberry Pi Zero. You can check by running python --version in the terminal.<br />

adafruit_ina219 Library: This Python library provides an interface for the INA219 current sensor. You can install it using pip:<br />
pip install adafruit-circuitpython-ina219<br />

busio and board Libraries: These libraries are required for I2C communication. They are part of the CircuitPython bundle and should be available by default.<br />

python3-rpi.gpio: This library allows you to interact with the GPIO pins on the Raspberry Pi.<br />
python3-smbus: Required for I2C communication.<br />
influxdb: Used for sending data to the InfluxDB database.<br />
You can install them using the following commands:<br />
sudo apt-get install python3-rpi.gpio<br />
sudo apt-get install python3-smbus<br />
sudo apt-get install python3-influxdb<br />
# Start Influxdb and Grafana:
sudo systemctl unmask influxdb.service<br />
sudo systemctl start influxdb<br />
sudo systemctl enable influxdb.service<br />
sudo dpkg -i --force-all grafana_6.0.1_armhf.deb<br />
sudo service grafana-server start<br />
# Run the code:
python send_data.py

