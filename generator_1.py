from random import randint
import os
import string

def counter():
    num = 10
    while True:
        i = yield num
        if i is not None:
            num = i
            continue
        num -= 1

c = counter()
print(next(c))
c_1 = c.send(5)
print(c_1)
print(next(c))

def number():
    for i in range(1,10):
        yield i

c_2 = number()
print(next(c_2))
print(next(c_2))
print(next(c_2))
print("+" * 30)

def dice():
    while True:
        yield randint(1,6)

d = dice()
for i in d:
    print(i)
    if i == 6:
        try:
            d.throw(ValueError("you got a 6!"))
        except ValueError as e:
            print(e)

def numbmer():
    num = 0
    while True:
        yield num
        num += 1

d_1 = number()
for i in d_1:
    print(i)
    if i == 5:
        d_1.close()
print("-" * 30)

def even():
    num = 0
    while True:
        yield num
        num += 1

d_2 = even()
for i in d_2:
    if i % 2 == 0:
        print(i)
    if i == 50:
        d_2.close()    
print("-" * 30)

def odd_numbers():
    for number in range(1, 51):
        if number % 2 != 0:
            yield number


for num in odd_numbers():
    print(num)

print("-" * 30)

def numb(n):
    for i in n:
        yield i
numbers = [-5,3,-1,7,10]

n_1 = numb(numbers)
print(next(n_1))
print(next(n_1))
print("-" * 30)

def num_1(nu):
    for i in nu:
        if i > 0:
            yield i


n_2 = num_1(numbers)
print(next(n_2))
print("-" * 30)

def student(s):
    for name, score in s:
        if score >= 10:
            yield name

students = [
    ("Ali",18),
    ("Sara",20),
    ("Reza",8)
]

n_3 = student(students)
print(next(n_3))
print("-" * 30)

def even_1():
    for i in range(1,101):
        yield i

n_4 = even_1()
for i_1 in n_4:
    print(i_1)
    if i_1 != 0:
        try:
            n_4.throw(ValueError("is odd"))
        except ValueError as e:
            print(e)

print("-" * 30)

even_numbers = (number for number in range(1,101) 
                if number % 2 == 0)

for e_1 in even_numbers:
    print(e_1)

print("-" * 30)

def fibinachi(f):
    a, b = 0, 1
    for _ in range(f):
        a, b = b, a + b
        yield a

n_5 = fibinachi(10)
for i in n_5:
    print(i)

print("-" * 30)

def prime():
    add = 2

    while True:
        is_prime = True
        for i in range(2, int(add ** 0.5) + 1):
            if add % i == 0:
                is_prime = False
                break
        if is_prime:
            yield add
        add += 1

n_6 = prime()
for _ in range(10):
    print(next(n_6))

print("-" * 30)

def read(fname):

    with open (fname, 'r') as f:
        for line in f:
            yield line.strip()

file_1 = "Documents/python/advanced/s.txt"
n_7 = read(file_1)
for l in n_7:
    print(l)
print("-" * 30)

def get_file(folder):
    for file in os.listdir(folder):
        yield file

file_2 = "Documents/python/"
n_8 = get_file(file_2)
for f in n_8:
    print(f)
print("-" * 30)

def get_files(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            yield path

n_9 = get_files(file_2)
print(next(n_9))