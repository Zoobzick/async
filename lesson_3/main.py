import sys
from socket import *

from variables.utils import get_message, send_message


def messages_handler(message):
    if 'action' in message and message['action'] == 'presence' and 'time' in message \
            and 'user' in message and message['user']['account_name'] == 'Guest':
        return {'RESPONSE': 200}
    return {
        'RESPONSE': 400,
        'ERROR': 'Bad Request'
    }


def server():
    if '--help' in sys.argv:
        print('-p - Specify the port number in range 1024-65535 \n'
              '-a - Specify the address to listen')
    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = 7777
        if port < 1024 or port > 65535:
            raise ValueError
    except ValueError:
        print('Ports range must be in 1024-65535')
        sys.exit(1)
    except IndexError:
        print('Specify the port option after -p')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            address = sys.argv[sys.argv.index('-a') + 1]
        else:
            address = '127.0.0.1'
    except IndexError:
        print('Specify the address option after -a')
        sys.exit(1)
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))

    s.listen(5)

    while True:
        client, client_address = s.accept()
        message_from_client = get_message(client)
        print(message_from_client)
        response = messages_handler(message_from_client)
        send_message(client, response)
        client.close()


if __name__ == '__main__':
    server()
