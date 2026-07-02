from dataclasses import dataclass, field, fields

@dataclass
class SensorStream:
    """ Model a satelite sesnsor """
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

    def show_data(self):
        
        for f in fields(self):
            if f.name == 'name':
                continue
        
            value = getattr(self, f.name)
            unit = f.metadata.get("unit", "")

            yield f"{f.name}: {value} {unit}"
    
    def validate(self):

        for f in fields(self):
            if f.name == 'name':
                continue

            value = getattr(self, f.name)
            unit = f.metadata.get("unit", "")
            unit_1 = f.metadata.get("min", "")
            unit_2 = f.metadata.get("max", "") 

            try:
                if unit_1 < value < unit_2:
                    yield f"{f.name}: {value} {unit}"
            except ValueError:
                pass

                
s = SensorStream('',90, 1.2, 20, 20)
s_3 = SensorStream('','','','','')
s_1 = s.show_data()
#print(next(s_1))
#print(next(s_1))
#print(next(s_1))
s_2 = s.validate()
for i in s_2:
    print(i)
