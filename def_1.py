import collections
from collections import namedtuple
from functools import reduce
from random import randint

def minus(a, b, /):
    return a - b

print(minus(6, 10))

def send(to, /, title, *, body):
    print(f"{to=}")
    print(f"{title=}")
    print(f"{body=}")

send("sia", "welcome", body="to our site")

a = {1:'one', 2:'Two'}
a |= {1:'Yek'}
print(a)

users = ['a', 'b', 'c']
for i, u in enumerate(users,1):
    print(f"{i}- {u}")

chars = ['a','a','b','b','c']
freq = collections.Counter(chars)
print(freq)

head1, head2, *middle, tail1 = chars
print(head2)
print(tail1)
print(middle)

User = namedtuple('User',
                  ['firest_name', 'last_name', 'age', 'email'])

def user_detail(user_list):
    user = User._make(user_list)
    print(f"{user.firest_name=}")
    print(f"{user.last_name=}")
    print(f"{user.age=}")
    print(f"{user.email=}")

sample = ['ani', 'mia', 35, 'an@gmail.com']
user_detail(sample)
print("." * 30)

first = ['abi', 'sia', 'fik', 'ser', 'itr']
ages = [25, 22, 29, 27]
for f, a in zip(first, ages):
    print(f"{f} is {a} years old.")

res = (lambda x : x + 5)(7)
print(res)

res_1 = (lambda *args : sum(args) / len(args))(7,15,6)
print(res_1)

res_2 = lambda x :  True if x % 2 == 0 else False 
print(res_2(2)) 

res_3 = lambda x, y :  x if x > y  else y 
print(res_3(2,3)) 

res_4 = lambda x : len(x)
print(res_4('python'))

def pow(x):
    return x ** 2

num = [1, 2, 3, 5]
power = list(map(pow, num))
print(power)

res_5 = lambda x : x ** 2
p = list(map(res_5, num))
print(p)

even = list(filter(lambda x : x % 2 ==0, num))
print(even)

users = ['sia-35', 'mia-25', 'pey-55', 'sina-39']
def qulify(u_str: str) -> bool:
    name, age = u_str.split('-')
    age = int(age)
    return name.lower().startswith('s') and age > 30

q = list(filter(qulify, users))
print(q)

res_6 = lambda x, y : x + y
print(reduce(res_6, num))

q_1 = [i / 5 for i in range(2,9) if i % 2 == 0]
print(q_1)

def dice():
    return randint(1,6)
q_2 = [t for _ in range(10) if (t := dice()) > 3]
print(q_2)

#if (num := input("Enter number: ")):
    #print(num)

#if len(name := input("Name: ")) > 5:
    #print(name)

q_3 = {i:i ** 3 for i in range(1,11)}
print(q_3)