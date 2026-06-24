from contextlib import contextmanager

@contextmanager
def file(name):
    f = open(name, 'w')
    try:
        yield f
    except:
        print("wrong!")
    finally:
        f.close()
        