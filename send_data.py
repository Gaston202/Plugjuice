import time
from adafruit_ina219 import INA219
from influxdb import InfluxDBClient
from busio import I2C
from board import SCL, SDA
# Initialize I2C bus
i2c = I2C(SCL, SDA)

# Initialize the INA219 sensor
ina219 = INA219(i2c)

# InfluxDB configuration
hote_influxdb = "localhost"
port_influxdb = 8086
base_de_donnees_influxdb = "ma_base_de_donnees"
mesure_influxdb = "consommation_energie"
client = InfluxDBClient(host=hote_influxdb, port=port_influxdb, database=base_de_donnees_influxdb)

def obtenir_consommation_energie():
    # Get the current in amperes (A)
    current = ina219.current  # Convert mA to A
    return current

while True:
    try:
        horodatage = int(time.time() * 1000)
        consommation = obtenir_consommation_energie()

        point_de_donnees = [
            {
                "measurement": mesure_influxdb,
                "fields": {
                    "consommation_energie": consommation
                }
            }
        ]

        client.write_points(point_de_donnees)

        print(f"Current: {consommation:.4f} mA (sent to InfluxDB) - Current timestamp: {time.ctime()} (timestamp: {horodatage})")
        time.sleep(1)

    except KeyboardInterrupt:
        break