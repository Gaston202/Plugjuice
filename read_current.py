# read_current.py

import time
from adafruit_ina219 import INA219
from busio import I2C
from board import SCL, SDA

# Initialize I2C bus
i2c = I2C(SCL, SDA)

# Initialize the INA219 sensor
ina219 = INA219(i2c)

def main():
    print("Measuring current through INA219 sensor...")
    while True:
        try:
            current = ina219.current / 1000  # Convert mA to A
            voltage = ina219.bus_voltage + ina219.shunt_voltage  # Total voltage
            power = ina219.power / 1000  # Convert mW to W
            
            print(f"Current: {current:.4f} A")
            print(f"Voltage: {voltage:.4f} V")
            print(f"Power: {power:.4f} W")
            print("-" * 40)
            
            time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
