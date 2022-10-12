from fractions import Fraction
from socket import socket
import time
from djitellopy import Tello
from droneapp.models.base import Singleton
import os
import subprocess
import threading

import cv2 as cv
import numpy as np

DEFAULT_DISTANCE = 0.30
DEFAULT_SPEED = 10
DEFAULT_DEGREE = 10
FRAME_X = int(960/3)
FRAME_Y = int(720/3)
FRAME_AREA = FRAME_X * FRAME_Y
FRAME_SIZE = FRAME_AREA * 3
FRAME_CENTER_X = FRAME_X / 2
FRAME_CENTER_Y = FRAME_Y / 2

CMD_FFMPEG = f'ffmpeg -hwaccel auto -hwaccel_device opencl -i pipe:0 -pix_fmt bgr24 -s {FRAME_X}x{FRAME_Y} -f rawvideo pipe:1'


class DroneManager(metaclass=Singleton):
    def __init__(self, is_imperial=False):
        self.is_imperial = is_imperial

        self.drone = Tello()
        self.drone.connect()
        self.proc = subprocess.Popen(CMD_FFMPEG.split(
            ' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.proc_stdin = self.proc.stdin
        self.proc_stdout = self.proc.stdout

        self.video_port = 11111
        self._receive_video_thread = threading.Thread(
            target= self.receive_video,
            args = (self.stop_event, self.proc_stdin, self.host_ip, self.video_port,)
        )
        self._receive_video_thread.start()

        # self.set_speed(DEFAULT_SPEED)
    # def __dell__(self):
    #     self.stop()

    # def stop(self):
    #     self.socket.close()

    def takeoff(self):
        self.drone.takeoff()

    def land(self):
        self.drone.land()

    def imperialDistance(self, distance):
        distance = float(distance)
        if self.is_imperial:
            distance = int(round(distance * 30.48))
        else:
            distance = int(round(distance*100))
        return distance

    def up(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_up(distance)

    def down(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_down(distance)

    def left(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_left(distance)

    def right(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_right(distance)

    def forward(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_forward(distance)

    def back(self, distance=DEFAULT_DISTANCE):
        distance = self.imperialDistance(distance)
        self.drone.move_back(distance)

    def set_speed(self, speed):
        self.drone.set_speed(speed)

    def clockwise(self, angle=DEFAULT_DEGREE):
        self.drone.rotate_clockwise(angle)

    def counter_clockwise(self, angle=DEFAULT_DEGREE):
        self.drone.rotate_counter_clockwise(angle)

    def flip_front(self):
        self.drone.flip_forward()

    def flip_back(self):
        self.drone.flip_back()

    def flip_right(self):
        self.drone.flip_right()

    def flip_left(self):
        self.drone.flip_left()

    def receive_video(self, stop_event, pipe_in, host_ip, video_port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock_video:
            sock_video.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            