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
- Rest client software (Postman, Thunder Client)

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
Use the route http://localhost:5000/saludo in your REST client software. Test the different responses by switching the HTTP method between GET, POST, PUT and DELETE. For POST and PUT requests, make sure to include a JSON body with the key "name" to properly test the response.

## License
Distributed under the MIT License. See LICENSE for more information.
