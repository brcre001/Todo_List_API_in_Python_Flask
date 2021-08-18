from flask import Flask, jsonify, request
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

todos = []

@app.route('/todos', methods=['GET'])
def grab_information():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todo_text = request.data
    todo = json.loads(todo_text)
    todos.append(todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['PUT'])
def change_done(position):
    todo_text = request.data
    todo = json.loads(todo_text)
    if todo['label'] == None or todo['done'] == None:
        return "This doesn't have a label", 400
    todos[position] = todo
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)