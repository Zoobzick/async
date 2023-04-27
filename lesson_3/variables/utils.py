import json

def get_message(client):
    message = client.recv(1024)
    if isinstance(message, bytes):
        json_response = message.decode('utf-8')
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(socket, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode('utf-8')
    socket.send(encoded_message)