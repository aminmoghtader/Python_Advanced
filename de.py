from functools import wraps
from datetime import datetime

def modify(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        class Child(cls):
            def __repr__(self):
                return f'{cls.__name__.upper()} object'
        return Child(*args, **kwargs)
    return wrapper

@modify
class Sia:
    pass
@modify
class Am:
    pass
print(Am())

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.logger = datetime.now()
        return func(*args, **kwargs)
    wrapper.logger = None
    return wrapper

@logger
def test():
    print(test.__name__)
test()
print(test.logger)

def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _ = 0
            for _ in range(n):
                _ += 1
                func(*args, **kwargs)
                print(f'{_}')
        return wrapper
    return decorator

@retry(5)
def test():
    print('test')
 
test()

def block_night(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_hour = datetime.now().hour

        if 2 <= current_hour < 5:
            print("⛔ اجرای تابع بین ساعت ۲ تا ۵ صبح مجاز نیست")
            return None

        return func(*args, **kwargs)

    return wrapper

@block_night
def test():
    print("تابع اجرا شد")

test()

class Exc(Exception):
    pass

def retry(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exc:
                    print(f"Retry {attempt}/{n} failed")

            raise Exc
                
        return wrapper
    return decorator

counter = 0

@retry(3)
def test():
    global counter
    counter += 1
    print("trying...")
    if counter < 3:
        raise Exc("error")
    print("success")

test()
"""
from functools import wraps
from threading import Thread
import time

class TimeoutError(Exception):
    pass


def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = {}
            error = {}

            def target():
                try:
                    result['value'] = func(*args, **kwargs)
                except Exception as e:
                    error['exception'] = e

            t = Thread(target=target)
            t.start()
            t.join(seconds)

            if t.is_alive():
                raise TimeoutError(
                    f"تابع بیش از {seconds} ثانیه اجرا شد"
                )

            if 'exception' in error:
                raise error['exception']

            return result.get('value')

        return wrapper
    return decorator

@timeout(2)
def long_task():
    time.sleep(2)

long_task()


class TimeoutError(Exception):
    pass


def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            if end - start > seconds:
                raise TimeoutError(
                    f"تابع بیشتر از {seconds} ثانیه طول کشید"
                )

            return result
        return wrapper
    return decorator


@timeout(2)
def long_task():
    time.sleep(3)

long_task()
"""
def cache(func):
    _cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = func(args, tuple(sorted(kwargs.items())))
        if key in _cache:
            return f'in cache'
        result = func(*args, **kwargs)
        _cache[key] = result
        return result
    return wrapper

@cache
def ab(a, b):
    return a + b

print(ab(2, 6))
print(ab(2, 6))


