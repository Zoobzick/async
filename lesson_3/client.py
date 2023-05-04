import sys
import time
from socket import *

from variables.utils import send_message, get_message


def presence_handler():
    msg = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': 'Guest'
        }
    }
    return msg


def response_handler(message):
    if 'RESPONSE' in message:
        if message['RESPONSE'] == 200:
            return '200 : OK'
        return f'400: {message["ERROR"]}'


def client():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = '127.0.0.1'
        server_port = 7777
    except ValueError:
        print('Ports range must be in 1024-65535')
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_address, server_port))
    message_to_send = presence_handler()
    send_message(s, message_to_send)

    try:
        response = response_handler(get_message(s))
        print(response)
    except ValueError:
        print('Не удалось распознать сообщение сервера')


if __name__ == '__main__':
    client()
