# mqtt-wait

Dead-simple mqtt utility to synchronize command runs between different terminals or machines.

## Requirements

- python 3.x
- paho-mqtt python library

## Configuration

Edit **mqtt-wait.py** and change the MQTT_SERVER variable to the hostname of your MQTT server.

## Usage

Specify an arbitary ID for the clients to be synchonized and pick one to the source.  

`mqtt-wait.py ID [source]`

Example:  
### Source

```
$ mqtt-wait.py ABC 1 ; date
Press <ENTER> to signal.
```

### Client
```
$ mqtt-wait.py ABC ; date
Waiting for signal.
```

When you press <ENTER> on the source terminal, the client terminal will continue execution simultaneously.   You can have as many clients as you want.  Having more than one *source* is meaningless, as the redundant sources will hang at the _Press <ENTER>_ prompt.

The ID string is simply to enable multiple groups of clients without them interfering with each other, in case you want to get fancy.

---
![mqtt-wait](https://cdn.phreakmonkey.com/misc/mqtt-wait.jpeg "mqtt-wait screenshot")
