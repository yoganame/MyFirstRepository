from functools import wraps
import inspect
import time
def advance_logger(loglevel):
    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno
    def _basic_log(fn, result, *args, **kwargs):
        print('function = ' + fn.__name__)
        print('    arguments = {0}{1}'.format(args, kwargs))
        print('    return = {0}'.format(result))
    def info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            _basic_log(fn, result, args, kwargs)
        return wrapper
    def debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            _basic_log(fn, result, args, kwargs)
            print('    time = %.6f sec'%(te-ts))
            print('    called_from_line:' + str(get_line_number))
        return wrapper
    if loglevel is 'debug':
        return debug_log_decorator
    else:
        return info_log_decorator
