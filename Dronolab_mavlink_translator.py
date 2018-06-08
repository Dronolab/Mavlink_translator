import time
import json
import socket
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
            msg = self.mavs.recv_match(blocking=True)
            msg_type = msg.get_type()

            if (msg_type == "ATTITUDE"):
                self.attitudeMsgHandler(msg)

            if (msg_type == "ALTITUDE"):
                self.altitudeMsg_Handler(msg)

            if (msg_type == "HIGHRES_IMU"):
                self.highersImuMsgHandler(msg)

            if (msg_type == "GPS_RAW_INT"):
                self.gpsRawIntMsg_Handler(msg)

            if (msg_type == "GLOBAL_POSITION_INT"):
                self.globalPositionMsgHandler(msg)

            if (msg_type == "VFR_HUD"):
                self.vrfHudMsgHandler(msg)

            if (msg_type == "LOCAL_POSITION_NED"):
                self.localPositionNedMsgHandler(msg)

    def send_to_interop(self, msg):
        message = json.dumps(msg)
        self.sock.sendto(message.encode('utf-8'), (self.UDP_IP, self.UDP_PORT))

    def attitudeMsgHandler(self, m):
        response = {
            "packet_id": 30,
            "time_boot_ms": m.time_boot_ms,
            "roll": m.roll,
            "pitch": m.pitch,
            "yaw": m.yaw,
            "rollspeed": m.rollspeed,
            "pitchspeed": m.pitchspeed,
            "yawspeed": m.yawspeed
        }

        self.send_to_interop(response)

    def altitudeMsg_Handler(self, m):
        response = {
            "packet_id": 141,
            "time_usec": m.time_usec,
            "altitude_monotonic": m.altitude_monotonic,
            "altitude_amsl": m.altitude_amsl,
            "altitude_local": m.altitude_local,
            "altitude_relative": m.altitude_relative,
            "altitude_terrain": m.altitude_terrain,
            "bottom_clearance": m.bottom_clearance
        }
        self.send_to_interop(response)

    def highersImuMsgHandler(self, m):
        response = {
            "packet_id": 105,
            "time_usec": m.time_usec,
            "xacc": m.xacc,
            "yacc": m.yacc,
            "zacc": m.zacc,
            "xgyro": m.xgyro,
            "ygyro": m.ygyro,
            "zgyro": m.zgyro,
            "xmag": m.xmag,
            "ymag": m.ymag,
            "zmag": m.zmag,
            "abs_pressure": m.abs_pressure,
            "diff_pressure": m.diff_pressure,
            "pressure_alt": m.pressure_alt,
            "temperature": m.temperature,
            "fields_updated": m.fields_updated
        }
        self.send_to_interop(response)

    def gpsRawIntMsg_Handler(self, m):
        response = {
            "packet_id": 24,
            "time_usec": m.time_usec,
            "fix_type": m.fix_type,
            "lat": m.lat,
            "lon": m.lon,
            "alt": m.alt,
            "eph": m.eph,
            "epv": m.epv,
            "vel": m.vel,
            "cog": m.cog,
            "satellites_visible": m.satellites_visible
        }
        self.send_to_interop(response)

    def globalPositionMsgHandler(self, m):
        response = {
            "packet_id": 33,
            "time_boot_ms": m.time_boot_ms,
            "lat": m.lat,
            "lon": m.lon,
            "alt": m.alt,
            "relative_alt": m.relative_alt,
            "vx": m.vx,
            "vy": m.vy,
            "vz": m.vz,
            "hdg": m.hdg
        }
        self.send_to_interop(response)

    def vrfHudMsgHandler(self, m):
        response = {
            "packet_id": 74,
            "groundspeed": m.groundspeed,
            "heading": m.heading,
            "throttle": m.throttle,
            "alt": m.alt,
            "climb": m.climb
        }
        self.send_to_interop(response)

    def localPositionNedMsgHandler(self, m):
        response = {
            "packet_id": 32,
            "time_boot_ms": m.time_boot_ms,
            "x": m.x,
            "y": m.y,
            "z": m.z,
            "vx": m.vx,
            "vy": m.vy,
            "vz": m.vz
        }
        self.send_to_interop(response)


print("Starting")
while True:
    try:
        mav = mavlinkHandler()
        mav.loop()
    except:
        continue