# This blank form for car, brand and model
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        # self.brand -> means class ke ander ke attributes or varibales ke bare me baat kar rahe hai
        # brand , model -> yeh parameters hai jo user ne diye hai
        self.model = model

my_car = Car("Tata", "Punch")
print(my_car.brand)
print(my_car.model)

my_newCar = Car("Honda", "City")
print(my_newCar.brand)
print(my_newCar.model)