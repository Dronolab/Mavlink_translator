import time
import json
import socket
import random
from pymavlink import mavutil
import GeneralSettings
import pymavlink.dialects.v20.ardupilotmega


class mavlinkHandler:
    def __init__(self):
        self.mavs = mavutil.mavlink_connection(GeneralSettings.mavlink_endpoint, input=True)
        self.UDP_IP = "127.0.0.1"
        self.UDP_PORT = 5555
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                socket.SOCK_DGRAM)

    def loop(self):
        while True:
            time.sleep(0.1)
            self.globalPositionMsgHandler()


    def send_to_interop(self, msg):
        message = json.dumps(msg)
        self.sock.sendto(message.encode('utf-8'), (self.UDP_IP, self.UDP_PORT))

    def globalPositionMsgHandler(self):
        response = {
            "packet_id": 33,
            "time_boot_ms": 0,
            "lat": int(38.145125  * 10000000) + random.randint(-100, 100),
            "lon": int(-76.428262 * 10000000) + random.randint(-100, 100),
            "alt": 10,
            "relative_alt":22,
            "vx": 0,
            "vy": 0,
            "vz": 0,
            "hdg": 10
        }
        print(response)
        self.send_to_interop(response)


print("Starting")
while True:
    try:
        mav = mavlinkHandler()
        mav.loop()
    except:
        continue