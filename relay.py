import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define relay pins
PIN_RELAY_1 = 13


# Initialize relay pins as output
GPIO.setup(PIN_RELAY_1, GPIO.OUT)


try:
    # Turn on relay 1
    GPIO.output(PIN_RELAY_1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(PIN_RELAY_1, GPIO.LOW)
except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()
