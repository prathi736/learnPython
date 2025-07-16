# This blank form for car, brand and model
class Car:
    # Class variable
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand # __brand -> this becomes private
        # self.brand -> means class ke ander ke attributes or varibales ke bare me baat kar rahe hai
        # brand , model -> yeh parameters hai jo user ne diye hai
        self.__model = model
        # Accessing Class Variable
        Car.total_car += 1
    
    # getter for brand to access private brand
    def get_brand(self):
        return self.__brand + "!"

    # Functionality in class 
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    # Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Decorators -> enhances the functionality of the method
    @staticmethod #static method
    def general_description():
        return "Every Car has 4 Wheels."
    
    @property # this decorator converted method into property
    def model(self):
        return self.__model

# Inheriting from above class car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super -> access karega upar vali class ke attributes or variables ko
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Polymorphism: same method but different behaviors
    def fuel_type(self):
        return "Electric charge"

my_ev = ElectricCar("Tata", "NexonEV", "50kWh")

print(isinstance(my_ev, Car))
print(isinstance(my_ev, ElectricCar))


# print(my_ev.brand)
# print(my_ev.get_brand())
# print(my_ev.fuel_type())
# print(my_ev.model)
# print(my_ev.battery_size)
# print(my_ev.full_name())

# my_car = Car("Tata", "Punch")
# my_car.model = "Hexa"
# print(my_car.general_description())
# print(Car.general_description())
# print(my_car.model)



# Car("Tata", "Punch")
# Car("Honda", "WR-V")
# print(Car.total_car)
# print(my_car.fuel_type())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_newCar = Car("Honda", "City")
# print(my_newCar.brand)
# print(my_newCar.model)


# Multiple Inheritance

class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"
    
class EVCar(Engine, Battery, Car):
    pass

my_new_ev = EVCar("MG", "Windsor")

print(my_new_ev.battery_info())
print(my_new_ev.engine_info())