import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from client import presence_handler, response_handler


class ClientTest(unittest.TestCase):

    def test_presence(self):
        presence = presence_handler()
        presence['time'] = '1.1'

        self.assertEqual(presence, {
            'action': 'presence',
            'time': '1.1',
            'user': {'account_name': 'Guest'}
        })

    def test_200_answer(self):
        self.assertEqual(response_handler({'RESPONSE': 200}), '200 : OK')

    def test_400_naswer(self):
        self.assertEqual(response_handler({'RESPONSE': 400, 'ERROR': 'Bad Request'}), '400: Bad Request')


if __name__ == '__main__':
    unittest.main()
