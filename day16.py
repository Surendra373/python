# class and object - inheritance

class Vehicle:
    wheel = 1 
    
class bike(Vehicle):
        vecicle_type = None
        
        
class car(Vehicle):
            vehicle_type = None
            
@staticmethod # ALSO KNOWN AS DECURATOR

def check_car_wheel():
    pass 
        
def get_vehicle_type(self):
    self.check_car_wheel()
    return self.vehicle_type
            
c1 = car()
b1 = bike()
print(b1.wheel)
print(c1.wheel)
print(c1.get_vehicle_type())




