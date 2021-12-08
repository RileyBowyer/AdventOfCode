from functools import wraps
from time import time


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"Function: {f.__name__} took {(te-ts) * 1e6:2.4f} us")
        return result
    return wrap
