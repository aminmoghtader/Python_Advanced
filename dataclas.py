from dataclasses import dataclass, field, fields
from typing import List

@dataclass(order=True)  
class Car:
    name : str
    model : str
    max_speed : float
    price: int = field(repr=False, compare=False)

def max_speed_in_mph(self):
    return self.max_speed * 0.62

bmw = Car('bmw', '328i', 220, 2200)
print(bmw)

##################
@dataclass
class Email:
    sender:str
    title:str
    body:str

def get_new_inbox():
    return [Email("Admin", "Welcome", "Welcome to website")]

@dataclass
class UserInbox:
    user_id: int = 1
    address: str = field(default="test@am.com", compare=False)
    inbox: List[Email] = field(default_factory=get_new_inbox)

##################
@dataclass
class Object2D:
    width: float = field(metadata={'unit':'cm'})
    height: float = field(metadata={'unit':'cm'})

print(fields(Object2D))

@dataclass
class Rectangle:
    w: float = field(metadata={'unit':'m'})
    h: float = field(metadata={'unit':'m'})

    def area(self):
        return self.w * self.h

    def show_metadata(self):
        for f in fields(self):
            print(f"{f.name} -> {f.metadata}")

a = Rectangle(5, 6)
print("Area:", a.area())
a.show_metadata()

@dataclass
class Product:
    name: str
    weight: float = field(metadata={'unit': 'kg'})
    price: float = field(metadata={'currency': 'USD'})

    def generate_report(self):
        for f in fields(self):
            if f.name == 'weight':
                unit = f.metadata.get('unit','')
                print(f"weight: {getattr(self, f.name)} {unit}")
            elif f.name == 'price':
                unit = f.metadata.get('currency','')
                print(f"price: {getattr(self, f.name)} {unit}")

p = Product('weight',10, 20)
p.generate_report()

@dataclass
class Person:
    name: str
    age: int
    email: str 

    def get_new(self):
        return f"name: {self.name} ,age: {self.age}, Email: {self.email} "

pr = Person('q', 15, '@ap.ir')
print(pr.get_new())

@dataclass
class Employee:
    name: str
    salary: int
    id: int = field(init=False)

    c = 0
    def __post_init__(self):
        Employee.c += 1
        self.id = Employee.c
        if self.id > 3:
            print("ok")

e1 = Employee("Ali", 2000)
e2 = Employee("Reza", 3000)
e3 = Employee("a", 3000)
print(e1.id)
print(e2.id)
print(e3.id)
e3.__post_init__()

"""
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

p = Person("Ali", -5)
"""

@dataclass
class Product:
    name: str
    price: float


@dataclass
class Customer:
    name: str
    email: str = field(init=False)


@dataclass
class Order:
    customer: Customer
    products: list = field(default_factory=list)

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

    def show_invoice(self):

        print(f"Customer: {self.customer.name}")
        print("-" * 30)

        for product in self.products:
            print(f"{product.name}: {product.price}")

        print("-" * 30)
        print(f"Total: {self.total_price()}")


c = Customer("Ali")

laptop = Product("Laptop", 50000)
mouse = Product("Mouse", 500)

order = Order(c)

order.add_product(laptop)
order.add_product(mouse)

order.show_invoice()

#####################
@dataclass
class User:
    __slots__ = ['username','password']
    username: str
    password: str
