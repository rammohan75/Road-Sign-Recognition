# control.py
import time

# Mock motor_driver module with basic functions
class motor_driver:
    @staticmethod
    def stop():
        print("Motor stopped")

    @staticmethod
    def turn_left():
        print("Turning left")

    @staticmethod
    def turn_right():
        print("Turning right")

    @staticmethod
    def move_forward():
        print("Moving forward")

    @staticmethod
    def move_backward():
        print("Moving backward")

def execute_command(command):
    if command == "stop":
        motor_driver.stop()
    elif command == "left":
        motor_driver.turn_left()
    elif command == "right":
        motor_driver.turn_right()
    elif command == "forward":
        motor_driver.move_forward()
    elif command == "backward":
        motor_driver.move_backward()
    else:
        print("Unknown command")

# Example usage
if __name__ == "__main__":
    execute_command("forward")
    time.sleep(2)
    execute_command("stop")
