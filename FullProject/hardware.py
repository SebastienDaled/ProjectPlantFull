import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, jsonify
import Adafruit_GPIO.SPI as SPI
import spidev
import numpy as np

app = Flask(__name__)

# Set GPIO pin number
pin = 21

@app.route('/home')
def home():
    return render_template('components/home.html')

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/sensoren')
def sensoren():
    # Read the moisture level
    moisture_data = read_moisture_level()

    # Return the moisture data as a JSON response
    return jsonify(moisture_data)

# Set GPIO mode and pin number
#GPIO.setmode(GPIO.BCM)
#moisture_pin = 21

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0) 

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def read_moisture_level():
    # Set GPIO pin as input
    GPIO.setup(moisture_pin, GPIO.IN)
    
    # Read moisture level (assuming higher moisture means lower ADC value)
    moisture_value = GPIO.input(moisture_pin)
    
    # Convert moisture value to percentage
    moisture_1or0 = moisture_value
    moisture_percentage = (1 - moisture_value) * 100
    
    # Determine the moisture level category
    moisture_status = "Need water" if moisture_percentage < 30 else "Don't need water"
    
    # Create a dictionary with moisture data
    moisture_data = {
        'moisture_HorL': moisture_1or0,
        'moisture_percentage': moisture_percentage,
        'moisture_status': moisture_status,
        
    }
    
    return moisture_data

try:
    while True:
        moisture = read_moisture_level()
#        print(f"Moisture HorL: {moisture['moisture_HorL']}")
        print(f"Moisture status: {moisture['moisture_status']}")
        #print(f"Moisture precentage: {moisture['moisture_percentage']}%")
        output = analogInput(0) # Reading from CH0
        output = np.interp(output, [0, 1023], [100, 0])
        output = int(output)
        print("Moisture:", output, " %")
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
