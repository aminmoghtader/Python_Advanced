from functools import wraps
from datetime import datetime

def get(name):

    def add(a, b, /):
        return a + b
    
    def sub(a, b, /):
        return a - b
    
    if name == "add":
        return add
    
    elif name == "sub":
        return sub
    
    else:
        Exception("Not found")

r = get("add")(9,5)
print(r)
print("-" * 30)

def hello(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper

def sample():
    print("sample")

sample = hello(sample)
sample()
print("-" * 30)

def hello(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper

@hello
def sample():
    print("s") 

sample()   
print("-" * 30)

def tree(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@tree
def say(name):
    print(f"am {name}")

say('hi')
print("-" * 30)

def broder(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'{result:*^10}'
    return wrapper

@broder
def add(a, b, /):
    return a + b

print(add(4,5))
print("-" * 30)

def retry(n):

    def dec(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return dec

@retry(3)
def test():
    print("test")

test()
print("-" * 30)

def last(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.last = datetime.now()
        return func(*args, *kwargs)
    wrapper.last = None
    return wrapper

@last
def test():
    print("test")

test()
print(test.last)
print("-" * 30)

def modify(cls):

    @wraps(cls)
    def wrapper(*args, **kwargs):
        class child(cls):
            def __repr__(self):
                return f'{cls.__name__.title()} object'
        return child(*args, **kwargs)
    return wrapper

@modify
class Sia:
    pass

@modify
class Am:
    pass

print(Sia())