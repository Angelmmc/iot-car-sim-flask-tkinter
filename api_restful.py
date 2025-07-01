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

# Leer los últimos 10 registros de carro ordenados por ID
@app.route('/cars/latest', methods=['GET'])
def get_latest_cars_manual():
    # Hacer una solicitud para obtener todos los registros
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        cars = response.json()

        # Asegurarse de que los registros estén ordenados por 'id' de forma ascendente
        # Si ya están en orden ascendente, simplemente seleccionamos los últimos 10
        latest_cars = cars[-10:]  # Obtiene los últimos 10 registros

        return jsonify(latest_cars)
    else:
        return jsonify({'error': 'No se pudo obtener los datos'}), response.status_code



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
