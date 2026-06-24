"""
def send(to, /, title, *,body):
    print(f"to={to}")
    print(f"title={title}")
    print(f"body={body}")

send("sia","wel",body="wel")

users = {
    1:'sia',
    2:'ali',
    3:'er',
    4:'rea'
}
max = max(users.values(), key=lambda name : len(name))
print(max)

from collections import namedtuple

user = namedtuple('user', 
                  ['f_name', 'l_name', 'age', 'email'])

def user_detail(user_list):
    User = user._make(user_list)
    print(f"{User.f_name=}\n{User.l_name=}\n{User.age=}\n{User.email=}")

sample = ['am', 'so', 35, 'sh.com']
user_detail(sample)
"""
avg = (lambda *args: sum(args) / len(args))(12,15,21)
print(avg)

sum_num = lambda x, /, y=0, *, z=0, **kwargs: \
x + y + z + kwargs.get('k',0)
print(sum_num(1, 2, z=3, k=5))

x = [1, 2, 3]
def pow(y):
    return y ** 2
p = list(map(pow, x))
for s in p:print(s)

users = ["shayan-35", "sia-29", "pey-50"]
def qua(user: str) -> bool:
    name, age = user.split('-')
    age = int(age)
    return name.lower().startswith('s') and age > 30
qual = list(filter(qua, users))
print(qual)

a = [i**2 for i in range(3,7) if i > 4]
print(a)

from random import randint
def dict():
    return randint(1,6)
lis = [temp for _ in range(10) if (temp:=dict()) > 3] 
print(lis)