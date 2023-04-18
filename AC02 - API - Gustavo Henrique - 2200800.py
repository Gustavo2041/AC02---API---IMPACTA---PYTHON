from flask import Flask
import json
app = Flask(__name__)

tasks = [
    {
        "id": 10,
        "name": "Gustavo",
        "idade":19
    },
    {
        "id": 20,
        "name": "Victor",
        "idade": 22
    },
    {
        "id": 30,
        "name": "Hitalo",
        "idade":25
    }
]

tasksJSON = json.dumps(tasks)

@app.route('/teste', methods=['GET'])
def hello_world():
    return tasksJSON, 401

if __name__ == '__main__':
    app.run()