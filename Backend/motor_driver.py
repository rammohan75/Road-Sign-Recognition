# Mock version of GPIO for environments where RPi.GPIO is unavailable
# Replace this section with 'import RPi.GPIO as GPIO' on actual Raspberry Pi
class MockGPIO:
    BCM = 'BCM'
    OUT = 'OUT'

    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        print(f"GPIO Mode set to {mode}")

    def setwarnings(self, flag):
        print(f"GPIO Warnings set to {flag}")

    def setup(self, pin, mode):
        self.pins[pin] = False
        print(f"Pin {pin} set to mode {mode}")

    def output(self, pin, state):
        self.pins[pin] = state
        print(f"Pin {pin} set to {'HIGH' if state else 'LOW'}")

GPIO = MockGPIO()

import time

# Motor driver pin configuration
LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 22
RIGHT_MOTOR_BACKWARD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]:
    GPIO.setup(pin, GPIO.OUT)

def move_forward():
    GPIO.output(LEFT_MOTOR_FORWARD, True)
    GPIO.output(RIGHT_MOTOR_FORWARD, True)
    GPIO.output(LEFT_MOTOR_BACKWARD, False)
    GPIO.output(RIGHT_MOTOR_BACKWARD, False)

def move_backward():
    GPIO.output(LEFT_MOTOR_BACKWARD, True)
    GPIO.output(RIGHT_MOTOR_BACKWARD, True)
    GPIO.output(LEFT_MOTOR_FORWARD, False)
    GPIO.output(RIGHT_MOTOR_FORWARD, False)

def turn_left():
    GPIO.output(LEFT_MOTOR_FORWARD, False)
    GPIO.output(RIGHT_MOTOR_FORWARD, True)

def turn_right():
    GPIO.output(LEFT_MOTOR_FORWARD, True)
    GPIO.output(RIGHT_MOTOR_FORWARD, False)

def stop():
    for pin in [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]:
        GPIO.output(pin, False)
