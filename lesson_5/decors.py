import sys
import log.server_log_config
import log.client_log_config
import logging
import traceback
import inspect

if sys.argv[0] == 'client.py':
    LOGGER = logging.getLogger('client')
else:
    LOGGER = logging.getLogger('server')


def log(func):
    def log_saver(*args, **kwargs):
        print(*args, **kwargs)
        result = func(*args, **kwargs)
        LOGGER.debug(f'Called function {func.__name__} with params:{args}, {kwargs}'
                     f'From module: {func.__module__}, '
                     f'From function: {traceback.format_stack()[0].strip().split()[-1]}')
        return result
    return log_saver
