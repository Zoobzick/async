import sys
from socket import *
import logging
import log.server_log_config

from common.utils import get_message, send_message

SERVER_LOGGER = logging.getLogger('server')


def messages_handler(message):
    SERVER_LOGGER.debug(f'Parsing message from client: {message}')
    if 'action' in message and message['action'] == 'presence' and 'time' in message \
            and 'user' in message and message['user']['account_name'] == 'Guest':
        return {'RESPONSE': 200}
    return {
        'RESPONSE': 400,
        'ERROR': 'Bad Request'
    }


def server():
    if '-p' in sys.argv:
        port = int(sys.argv[sys.argv.index('-p') + 1])
        if 1024 > port > 65535:
            SERVER_LOGGER.critical(f'Port must be in range 1024-65535. Wrong input port: {port}')
            sys.exit(1)
    else:
        port = 7777

    if '-a' in sys.argv:
        address = sys.argv[sys.argv.index('-a') + 1]
    else:
        address = '127.0.0.1'
    SERVER_LOGGER.info(f'Starting server: {address}:{port}')

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))

    s.listen(5)

    while True:
        client, client_address = s.accept()
        SERVER_LOGGER.info(f'Connection established with {client_address}')
        message_from_client = get_message(client)
        SERVER_LOGGER.debug(f'Received message {message_from_client}')
        response = messages_handler(message_from_client)
        SERVER_LOGGER.debug(f'Created response to the client: {response}')
        send_message(client, response)
        client.close()
        SERVER_LOGGER.debug(f'Connection closed {client_address}')


if __name__ == '__main__':
    if '--help' in sys.argv:
        print('-p - Specify the port number in range 1024-65535 \n'
              '-a - Specify the address to listen')
    else:
        server()
