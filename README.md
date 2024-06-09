# Raspberry Pi Rod Tracker: Web-Based Hardware Control and Object Detection

## Project Overview
This project revolves around the integration of diverse hardware components with a Raspberry Pi, including a Pi camera, a stepper motor, and an ultrasonic distance-measuring sensor. The primary objective is to create an intuitive graphical user interface (GUI) in the form of a webpage for controlling the GPIO pins of the Raspberry Pi.

### Project Description
The Raspberry Pi-Rod-Tracker-Web-Based-Hardware-Control-and-Object-Detection project is a fusion of hardware and software ingenuity, focusing on establishing a seamless synergy between various components. The central components involved in this project are the Raspberry Pi, Pi camera, stepper motor, and ultrasonic distance measuring sensor.

### Key Features:

Raspberry Pi Control: The Raspberry Pi will serve as the central controller for these hardware components.

Web-Based GUI: We'll design a user-friendly web page interface as the primary control panel. It enables users to manipulate the Raspberry Pi's GPIO pins effortlessly.

Live Video Streaming: The webpage interface will also provide a live video stream from the Pi camera. This stream will display the movement of objects, detecting their color and position.

Stepper Motor Integration: An essential element of the setup, the stepper motor can be conveniently activated or deactivated through buttons on the webpage.
## Project Content

This repository contains the base folders to conduct each task, as follows:

### Tasks 1–3

You should use the files in the corresponding folders to solve each task. Each folder has a `main.py` script to test your code. The folders are:

| Task |               Folder |
|-----:|---------------------:|
|   1  | task1_opencv_control  |
|   2  | task2_motor_control |
|   3  | task3_sensor_control |

### Task 4

The root folder contains the necessary files and folders to complete Task 4. As you already know, the results of previous tasks are going to be employed by a Flask web application. Take the following information into account:

1. *requirements.txt*: This file contains the libraries that you might require for running the app. After creating your environment, you should install these libraries as follows:

```
pip install -r requirements.txt
```

Use *requirements_raspi.txt* for the Raspberry Pi.

2. *app.py*: This file is a script to run the Flask application. This application should work even if you haven't completed previous tasks. I will just do dummy things, like printing messages on the development server console.
3. *static*: This folder contains the main client-side script of this application.
4. *templates*: This folder contains the index template since this is a one-page application.

