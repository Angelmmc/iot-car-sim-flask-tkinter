# iot-car-sim-flask-tkinter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Angelmmc/iot-car-sim-flask-tkinter.svg)](https://github.com/Angelmmc/iot-car-sim-flask-tkinter/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/Angelmmc/iot-car-sim-flask-tkinter.svg)](https://github.com/Angelmmc/iot-car-sim-flask-tkinter/issues)

## About 
This project is a simulation of remote control for an IoT-based car. It features a Flask-based backend that exposes a mock API, and a Python desktop GUI built with Tkinter to interact with the API.

## Built with
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/tkinter-FFFFFF?style=for-the-badge&logo=python&logoColor=blue"/>

##  Getting Started

### Prerequisites
- Git
- Python 3.x

###  Installation

1. Clone the repository
```bash
git clone https://github.com/Angelmmc/iot-car-sim-flask-tkinter.git
```
2. Navigate to the project folder
```bash
cd iot-car-sim-flask-tkinter
```

3. Create and activate a virtual enviroment
```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

4. Open a second terminal in the same directory and activate the virtual enviroment
```bash
venv\Scripts\activate
```

5. Run the api_restful.py program on the first terminal
```bash
python api_restful.py
```

6. Run the desktop_app.py program on the second terminal
```bash
python desktop_app.py
```

## Usage

Main options
- **Control Panel**: Use directional buttons to send actions — forward, backward, left, and right — at different angles, and stop, the executed action will be print on the bottom of the screen.
- **History**: Clic the history button to open another window that displays the actions history ordered from the oldest to the newest.

## Screenshot

<img src="https://github.com/Angelmmc/iot-car-sim-flask-tkinter/blob/master/assets/img/tkinter_windows.png" alt="App Screen" width="500"/>

## License
Distributed under the MIT License. See LICENSE for more information.

## Related

This was a test practice to develop my iot-car project, check out the related repositories.

[![iot-car-arduino](https://img.shields.io/badge/iot__car-arduino-D68FD6?logo=github)](https://github.com/Angelmmc/iot-car-arduino)
[![iot-car-frontend-mobile](https://img.shields.io/badge/iot__car-frontend--mobile-E76F51?logo=github)](https://github.com/Angelmmc/iot-car-frontend-mobile)
[![iot-car-webapp](https://img.shields.io/badge/iot__car-webapp-05F140?logo=github)](https://github.com/Angelmmc/iot-car-webapp)
