from dataclasses import dataclass, field, fields
from typing import List
from pprint import pprint
import json

@dataclass
class SensorData:
    """ کلاس داده برای سنجش سنسور های ماهواره"""

    name : str
    temperature : float = field(metadata={
        "unit" : "c",
        "min" : -50,
        "max" : 100,
        "description" : "Temperature sensor",
        "required": True
    })
    peresure : float = field(metadata={
        "unit" : "bar",
        "min" : 0,
        "max" : 20,
        "description" : "peresure sensor",
        "required": True
    })
    voltage : float = field(metadata={
        "unit" : "V",
        "min" : 0,
        "max" : 10,
        "description" : "voltage sensor",
        "required": True
    })
    current : float = field(metadata={
        "unit" : "A",
        "min" : 0,
        "max" : 20,
        "description" : "current sensor",
        "required": True
    })

    #متد نمایش سنسور ها و مقادیر
    def show_data(self):
        for f in fields(self):

            if f.name == "name":
                continue

            value = getattr(self, f.name)
            unit = f.metadata.get("unit", "")
            
            print(f"{f.name}: {value} {unit}")  
        print("\n" + "-" * 30)

    #متد برسی سلامت سنسور
    def validate(self):
        for f in fields(self):
            if f.name == "name":
                continue
            value = getattr(self, f.name)
            unit = f.metadata.get("unit", "")
            unit_1 = f.metadata.get('min', '')
            unit_2 = f.metadata.get('max', '')
           
            if unit_1 <= value <= unit_2:
                print(f"{f.name}: {value} {unit} -> {f.name} is good")
            else:
                print(f"{f.name}: {value} {unit} -> {f.name} is out of range!!!")
        print("-" * 30)

    #متد نمایش حرفه ای مشخصات کامل 
    def show_specifications(self):
        for f in fields(self):
            if f.name == "name":
                continue
            unit = f.metadata.get("unit", "")
            description = f.metadata.get("description", "")
            unit_1 = f.metadata.get('min', '')
            unit_2 = f.metadata.get('max', '')
            print(
                f"{f.name}\n"
                f"Description: {description}\n"
                f"Range: {unit_1} to {unit_2}\n"
                f"Unit: {unit}\n"
            )
        print("-" * 30)

    #متد ساخت دیکشنری از سنسور ها
    def to_dict(self):
        info = {}
        for f in fields(self):
            if f.name == "name":
                continue
            
            info[f.name] = {
                "valu" : getattr(self, f.name),
                "unit" :  f.metadata.get("unit", "")
            }
        return f"{json.dumps(info, indent=4)}\n{'-' * 30} "

    #متد ساخت گزارش خودکار
    def generate_report(self):
        #
        print("Sensor Report:\n")
        return f"{self.show_data()}" 

    def check_required(self):
        #
        for f in fields(self):
            required = f.metadata.get("required", False)

            if not required:
                continue
            value = getattr(self, f.name)

            if value is None or value == '':
                raise ValueError(
                    f"Field '{f.name}' is required."
                ) 
            return True

    #متد بررسی خالی نبودن فیلد های شی کلاس
    def check_required_1(self):
        #
        errors = []
        for f in fields(self):
            

            if not f.metadata.get("required", False):
                continue
            value = getattr(self, f.name)

            if value is None or value == '':
                errors.append(f.name)

        if errors:
            raise ValueError(
                f"Required fields missing: {', '.join(errors)}"
            )
        return True


s = SensorData('',200, 1.2, 20, 20)
s_1 = SensorData('','','','','')
s.show_data()
s.validate()
s_1.show_specifications()
print(s.to_dict())
s.generate_report()
#print(s_1.check_required())
print(s_1.check_required_1())