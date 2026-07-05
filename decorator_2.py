from functools import wraps
from datetime import datetime
import time

def hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start...")
        func(*args, **kwargs)
        print("end...")
    return wrapper

@hello
def say():
    print("hello")

say()
print("-" * 30)

def dec_1(func):

    @wraps(func)
    def wrapper():
        print(f"Running function: {wrapper.__name__}")
        func()
    return wrapper

@dec_1
def hello():
    print("Hello")

hello()
print("-" * 30)

def retry(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.c += 1
        print(f"call #{wrapper.c}")
        return func(*args, **kwargs)
    wrapper.c = 0
    return wrapper

@retry
def test():
    print("test")
    
test()
test()
test()
print(test.c)
print("-" * 30)

def show(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f'Result: {func(*args, **kwargs)}')
    
    return wrapper

@show
def show_1():
    return 20

show_1()
print("-" * 30)

def divide(func):

    @wraps(func)
    def wrapper(a, b):

        if type(a) != int or type(b) != int:
            return 'Not ok'
        if a < 0 or b < 0:
            return 'Negative numbers are not allowed.'
        else:
            return func(a, b)
    
    return wrapper

@divide
def add(a, b, /):
    return a + b

print(add(5,-6))
print("-" * 30)

def dec1(n):

    def dec(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(n)
            func(*args, **kwargs)
        return wrapper
    return dec

@dec1("welcome")
def say():
    print("Hello")

say()
print("-" * 30)

def dec2(n):

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                if _ >= 3:
                    print("Execution limit reached.")
                    break
                else:
                    func(*args, **kwargs)
        return wrapper
    return dec
    
@dec2(2)
def say():
    print('test')

say()
print("-" * 30)

def dec3(s):

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'waitting for {s} second...')
            time.sleep(s)
            func(*args, **kwargs)
        return wrapper
    return dec

@dec3(1)
def say():
    print("Hello")

say()
print("-" * 30)

def dec4(s):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(s)
            if s > 2:
                print("there is a problem to launch!")
            else:
                func(*args, **kwargs)
        return wrapper
    return dec

@dec4(1)
def say():
    print("hello")

say()
print("-" * 30)

def dec5(n):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            n_1 = "ammo"
            if n != n_1:
                return "password in wrong!"
            else:
                result = func(*args, **kwargs)
                return result.upper()
        return wrapper
    return dec


@dec5(input('plese enter pass: '))
def say():
    return "hello world"

print(say())
print("-" * 30)

def dec6(d):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            if isinstance(res, float):
                return round(res, d)
        
        return wrapper
    return dec

@dec6(2)
def digit():
    return 10 / 3

print(digit())
print("-" * 30)

def dec7(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, *kwargs)
        if res is None:
            return 'No results found!'
        return res
    return wrapper


@dec7
def say():
    return None

print(say())
print("-" * 30)

def dec8(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except ZeroDivisionError:
            return 'division by zero!'

    return wrapper

@dec8
def div(a, b):
    return a / b

print(div(1,0))
print("-" * 30)
