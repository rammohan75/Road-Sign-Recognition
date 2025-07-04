# 🚦 Road Sign Recognition and Vehicle Control using Raspberry Pi

This project enhances road safety by enabling real-time road sign recognition and automatic vehicle control using image processing and sensor data.

## 🎯 Features
- Real-time road sign detection using OpenCV
- Sobel filters + Gabor Wavelets for image processing
- Obstacle distance measurement using ultrasonic sensors
- Motor control via L293D and servo drivers
- Runs entirely on Raspberry Pi 3 with USB camera

## 🧰 Hardware Used
- Raspberry Pi 3
- Logitech USB Camera
- L293D Motor Driver
- Ultrasonic Sensor (HC-SR04)
- DC Motors
- Servo Motors

## 🧪 Software Stack
- Python 3
- OpenCV
- NumPy
- RPi.GPIO
- imutils

##  Folder Structure
road-sign-recognition-raspberrypi/
│
├──  backend/
│   ├── control.py               
│   ├── detect_signs.py          
│   ├── motor_driver.py         
│   └── sensor_module.py         
│
├──  images/
│   ├── blockdiagram.png              
│   ├── Rasberrypie_pin_diagram.png     
│
│  
├── requirements.txt            
├── README.md                    
└── run.sh  
## ⚙️ Setup Instructions
1. Clone this repository onto your Raspberry Pi.
2. Connect all sensors and modules as per the circuit design.
3. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
