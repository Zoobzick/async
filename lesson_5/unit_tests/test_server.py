import os
import sys
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from server import messages_handler


class TestServer(unittest.TestCase):
    error_message = {
        'RESPONSE': 400,
        'ERROR': 'Bad Request'
    }

    success_message = {
        'RESPONSE': 200,
    }

    def test_no_action(self):
        self.assertEqual(messages_handler(
            {'time': '1.1',
             'user': {'account_name': 'Guest'}}
        ), self.error_message)

    def test_wrong_action(self):
        self.assertEqual(messages_handler(
            {'time': '1.1',
             'action': 'wrong',
             'user': {'account_name': 'Guest'}}
        ), self.error_message)

    def test_no_time(self):
        self.assertEqual(messages_handler(
            {'action': 'presence',
             'user': {'account_name': 'Guest'}}
        ), self.error_message)

    def test_no_user(self):
        self.assertEqual(messages_handler(
            {'action': 'presence',
             'time': '1.1'}
        ), self.error_message)

    def test_not_guest(self):
        self.assertEqual(messages_handler(
            {'action': 'presence',
             'time': '1.1',
             'user': {'account_name': 'randomuser'}}
        ), self.error_message)

    def test_success(self):
        self.assertEqual(messages_handler(
            {'action': 'presence',
             'time': '1.1',
             'user': {'account_name': 'Guest'}}
        ), self.success_message)


if __name__ == '__main__':
    unittest.main()
