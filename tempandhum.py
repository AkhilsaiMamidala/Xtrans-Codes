import time
import board
import adafruit_dht

# Set up DHT11 on GPIO4 (Pin 7)
dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            print(f"Temp: {temperature}°C    Humidity: {humidity}%")
        except RuntimeError as error:
            print(f"Sensor error: {error.args[0]}")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting program.")
