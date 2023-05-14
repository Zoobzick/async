import json
import sys
import time
from socket import *
import logging
import log.client_log_config
import errors
from decors import log
from common.utils import send_message, get_message

CLIENT_LOGGER = logging.getLogger('client')


@log
def presence_handler():
    msg = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': 'Guest'
        }
    }
    CLIENT_LOGGER.debug('Creating PRESENCE message for Guest')
    return msg


@log
def response_handler(message):
    CLIENT_LOGGER.debug(f'Parsing message from server: {message}')
    if 'RESPONSE' in message:
        if message['RESPONSE'] == 200:
            return '200 : OK'
        return f'400: {message["ERROR"]}'
    raise errors.RequiredFieldsMissingError('RESPONSE')


def client():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            CLIENT_LOGGER.critical(f'Trying to run client with wrong port number:{server_port}')
    except IndexError:
        server_address = '127.0.0.1'
        server_port = 7777
        CLIENT_LOGGER.info(f'Running client with standard IP & PORT. IP: {server_address}, PORT: {server_port} ')
    except ValueError:
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((server_address, server_port))
    message_to_send = presence_handler()
    send_message(s, message_to_send)

    try:
        response = response_handler(get_message(s))

    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Could not decode received JSON string')
    except ConnectionRefusedError:
        CLIENT_LOGGER.error('Connection is not established, because the destination computer '
                            'rejected the connection request.')


if __name__ == '__main__':
    client()
