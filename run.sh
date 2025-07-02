#!/bin/bash

echo "Starting Road Sign Detection System..."

# Run ultrasonic sensor in background
python3 sensor_module.py &

# Run motor controller
python3 control.py &

# Start detection pipeline
python3 detect_signs.py

wait
