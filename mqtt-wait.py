#!/usr/bin/env python

import sys
import time
import paho.mqtt.client as mqtt

MQTT_SERVER = 'mqtt'  # Change this to your MQTT server hostname
TOPIC = 'WAITFOR'
WAIT_ID = ''
APOPTOSIS = False


def errPrint(buf):
  sys.stderr.write(buf + '\n')
  sys.stderr.flush()

def on_connect(client, userdata, flags, rc):
  global WAIT_ID
  client.subscribe(f'{TOPIC}/{WAIT_ID}')

def on_message(client, userdata, msg):
  global APOPTOSIS
  print("Got message.  Let's go!")
  APOPTOSIS = True

def on_log(client, userdata, level, buf):
  if level != 16:
    errPrint(f'{level}: {buf}')

def main():
  global WAIT_ID, APOPTOSIS
  source = False
  if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} WAIT_ID [source]')
    sys.exit(1)
  if len(sys.argv) == 3:
    source = True
  WAIT_ID = sys.argv[1].strip()
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_log = on_log
  client.connect(MQTT_SERVER, 1883, 60)
  client.loop_start()
  if source:
    print("Press <ENTER> to signal.")
    sys.stdin.read(1)
    client.publish(f'{TOPIC}/{WAIT_ID}', 'GO')
  else:
    print("Waiting for signal.")
  while not APOPTOSIS:
    time.sleep(.001)


if __name__ == '__main__':
  main()
