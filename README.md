# MQTT, Adafruit IO & Electricity!

<!-- https://adafruit-io-python-client.readthedocs.io/en/latest/index.html -->
<!-- https://github.com/adafruit/Adafruit_IO_Python -->

## About

In an **electricity network**, smart meters deployed at customers' premises send periodically a set of data concerning consumption, generation in
case of installation of **renewable energy sources**, etc. **The counters**, being constrained devices will not maintain long-term connections. For this a asynchronous communication protocol is to be used to ensure these data flows, in our case **MQTT**.

> We have programmed a **python** SM (Smart meter) node as publisher/subscriber as well as MDMS (Meter data management system) node and MQTT broker deployed in Adafruit.IO IOT cloud.\*\*

![](https://cdn-learn.adafruit.com/assets/assets/000/057/153/original/adafruit_io_iopython.png?1530802073)

## What's included

Within the download you'll find the following directories and files:

```sh
Electricity IOT Hub
.
├── README.md
├── captures
│   ├── Annotation_yyyy-mm-dd_xxxxx.png
│   ├── ..
│   └── Annotation_yyyy-mm-dd_xxxxx.png
├── .gitignore
├── .env
├── SM.py
├── MDMS.py
└── requirements.txt
```

## Getting started

- Clone the project from our repository using: `git clone https://github.com/khalil-mejri/electricity-iot-hub.git`
- Create or sign in to your [Adafruit.IO](https://io.adafruit.com/) account to start new project.
- Create the following feeds (topics) on **My Feeds**
  > These feeds help implement 4 different data flows detailed below:

| Flow ID | Source | Destination |       Label       | Frequence |    QoS     |
| :-----: | :----: | :---------: | :---------------: | :-------: | :--------: |
|    1    |   SM   |    MDMS     |    consumption    |  1/60min  | MQTT_QOS_0 |
|    2    |   SM   |    MDMS     |    production     |  1/15min  | MQTT_QOS_0 |
|    3    |  MDMS  |     SM      |       price       |  1/60min  | MQTT_QOS_1 |
|    4    |  MDMS  |     SM      | Voltage reduction |   1/min   | MQTT_QOS_0 |

- Copy your Adafruit.IO **secret key** into `ADAFRUIT_IO_KEY` enironment variable under `.env` file.
- Copy your Adafruit.IO **username** it into `ADAFRUIT_IO_USERNAME` enironment variable under `.env` file.
- Install python +3.4.x on your system
- Install following project [dependencies](#) using `pip`
- Start your Smart Meter (SM) node simulator `python SM.py`
- Start your Meter Data Management System node simulator `python MDMS.py`

- Go ahead and create your Dashboard with Adafruit.IO dashboard widgets
  ![img](#)
- Enjoy! :)

## Notes

**MQTT** has some basic Quality of Service **'QoS'** capability built in. Basically, say you were using MQTT over a radio, and your toaster is sending radio signals to some base station...there's a chance those messages won't arrive. Heck, even with WiFi or Ethernet, there's a chance your message doesnt actually get to the **MQTT broker**.

Sending messages without knowing for sure they were received is called **"QoS 0" (zero).**

You may also want **QoS 1**, which lets you know the message was received. Basically, after each publication, the subscriber says "OK". In MQTT-speak this is called the **"PUBACK" (Publication Acknowledgement)**

Turning it on is easy, in the Adafruit_MQTT_Publish creation, put **MQTT_QOS_1** and that feed will be **QoS 1**. By default, feeds are created with **MQTT_QOS_0** and you don't need to specify **QoS0**.

## Questions? Need Help? Found a bug?

If you've got questions about setup, deploying, special feature implementation in your fork, or just want to chat with me, please feel free to start a thread in the Discussions tab!

Found a bug with Electricity IOT-HUB? Go ahead and submit an issue. And, of course, feel free to submit pull requests with bug fixes or changes to the dev branch.