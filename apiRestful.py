from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
BASE_URL = 'https://66eb03c355ad32cda47b5c6f.mockapi.io/iot/loTCarStatus'

# Leer todos los registros de carro
@app.route('/cars', methods=['GET'])
def get_cars():
    response = requests.get(BASE_URL)
    return jsonify(response.json())

# Leer un registro específico
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    response = requests.get(f'{BASE_URL}/{car_id}')
    return jsonify(response.json())

# Crear un nuevo registro
@app.route('/cars', methods=['POST'])
def create_car():
    new_car = request.json
    response = requests.post(BASE_URL, json=new_car)
    return jsonify(response.json()), 201

# Actualizar un registro existente
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    updated_car = request.json
    response = requests.put(f'{BASE_URL}/{car_id}', json=updated_car)
    return jsonify(response.json())

# Eliminar un registro
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    response = requests.delete(f'{BASE_URL}/{car_id}')
    return jsonify({'message': 'Car deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
