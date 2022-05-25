from flask import Flask, request, jsonify
from app.backend import services
import config 
import asyncio

app = Flask(__name__)

@app.route('/execute-pipeline', methods=['POST'])
def execute_pipeline():
    data = request.json
    message = services.execute_pipeline(data)
    return message

@app.route('/connector-schema', methods=['POST'])
def connector_schema():
    data = request.json
    message = services.get_schema(data)
    return message

@app.route('/connection-connector', methods=['POST'])
def connection_connector():
    data = request.json
    message = services.run_connector(data)
    return message

@app.route('/end-trigger')
def trigger_end():
    services.reboot_trigger()
    return "Trigger has stopped"

@app.route('/start-trigger')
def trigger_start():
    services.run()
    return "Trigger has started"

@app.route('/change-trigger', methods=['POST'])
def trigger_change():
    data = request.json
    services.modify_trigger(data)
    return jsonify(data)

@app.route('/')
def API():
    return "TEST"

if __name__ == '__main__':
    services.build()
    services.run()
    app.run(port=7820,debug=True)
    