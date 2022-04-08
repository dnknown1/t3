import time

def curried(n: int=0):
    '''Utility decorator: Curry functions return: decorator: callable'''
    def decrtr(f, *b, **h):
        if n == len(b): return f(*b, **h)
        def solver(*a, **d):
            return decrtr(f, *b, *a, **h, **d)
        return solver
    return decrtr

def timer(f:callable) -> callable:
    '''Utility decorator: Timer function: return: (time, result)'''
    def _(*args, **kwargs):
        t1 = time.time()
        r = f(*args, **kwargs)
        out = round(abs(time.time() - t1), 5)
        return f'{out} sec(s)', r
    return _

def looper(n: int=1):
    def decorator(f):
        def solver(*a, **d):
            for i in range(n-1): f(*a, **d)
            return f(*a, **d)
        return solver
    return decorator
