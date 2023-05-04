import sys
import os
import unittest
import json

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.utils import send_message, get_message


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        test_message = json.dumps(self.test_dict)
        self.encoded_message = test_message.encode('utf-8')
        self.received_message = message_to_send

    def receive(self, max_len):
        test_message = json.dumps(self.test_dict)
        return test_message.encode('utf-8')


class UtilsTest(unittest.TestCase):
    test_dict = {
        'action': 'presence',
        'time': '1.1',
        'user': {'account_name': 'Guest'}
    }
    test_dict_receive_ok = {'RESPONSE': 200}
    test_dict_receive_err = {'RESPONSE': 400, 'ERROR': 'Bad Request'}

    def test_send_message(self):
        test_socket = TestSocket(self.test_dict)
        send_message(test_socket, self.test_dict)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_get_message(self):
        test_socket_ok = TestSocket(self.test_dict_receive_ok)
        test_socket_err = TestSocket(self.test_dict_receive_err)
        self.assertEqual(get_message(test_socket_ok), self.test_dict_receive_ok)
        self.assertEqual(get_message(test_socket_err), self.test_dict_receive_err)


if __name__ == "__main__":
    unittest.main()
