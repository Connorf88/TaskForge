from flask import request, jsonify
from app import app, dynamo

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    dynamo.tables['tasks'].put_item(Item={'id': data['id'], 'task': data['task']})
    return jsonify({'message': 'Task added successfully!'})

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = dynamo.tables['tasks'].get_item(Key={'id': task_id})
    return jsonify(task.get('Item', {}))

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    dynamo.tables['tasks'].delete_item(Key={'id': task_id})
    return jsonify({'message': 'Task deleted successfully!'})
