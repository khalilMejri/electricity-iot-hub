# Smart Meter node publisher and subscriber
# to MQTT broker hosted whitin Adafruit.IO IOT cloud
# https://github.com/adafruit/Adafruit_IO_Python

# Author: khalil Mejri, Dec 2020

# Import standard python modules.
import random
import sys
import os
import time
import threading

# Import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

from dotenv import load_dotenv
load_dotenv()

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = os.getenv("ADAFRUIT_IO_USERNAME")

# Feeds within the group
feed_production_id = 'production'
feed_consumption_id = 'consumption'
feed_price_id = 'price'
feed_voltage_id = 'voltage_control'

# Feed publish frequencies
feed_production_freq = 30
feed_consumption_freq = 40

# Define callback functions which will be called when certain events happen.


def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to topic changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    # Subscribe to changes on a feed, `feed_name`
    print('Listening for changes on feed > ', feed_price_id)
    client.subscribe(feed_price_id, None, qos=0)
    # Subscribe to changes on a feed, `feed_name`
    print('Listening for changes on feed > ', feed_voltage_id)
    client.subscribe(feed_voltage_id, None, qos=1)


def subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('** Subscribed to {0} with QoS {1}'.format(mid, granted_qos[0]))


def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('-------- Disconnected from Adafruit IO! --------')
    sys.exit(1)


def message(client, topic_id, payload):
    # Message function will be called when a subscribed topic has a new value.
    # The topic_id parameter identifies the topic, and the payload parameter has
    # the new value.
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('<< Topic {0} received new value: {1} at {2}'.format(
        topic_id, payload, current_time))


# trigger function on custom time interval
def set_interval(mqtt, feed, sec):
    def func_wrapper():
        set_interval(mqtt, feed, sec)
        value = random.randint(10, 100)
        print('>> Publishing {0} to {1}.'.format(
            value, feed))
        mqtt.publish(feed, value)

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()

# Now send new values with correspondant frequency.
print(
    'Publishing a new message every {0} seconds (press Ctrl-C to quit)...'.format(feed_consumption_freq))
set_interval(client, feed_consumption_id, feed_consumption_freq)

print(
    'Publishing a new message every {0} seconds (press Ctrl-C to quit)...'.format(feed_production_freq))
set_interval(client, feed_production_id, feed_production_freq)
