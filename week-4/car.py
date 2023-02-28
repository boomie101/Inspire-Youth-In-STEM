class car:
    def __init__(self,model,make,year,):
        self.model = model
        self.make = make
        self.year = year

    def get_model(model):
        return self.model
    
    def get_make(make):
        return self.make
    
    def get_year(year):
        return self.year

car_1 = car("Demio" , "Mazda" , 2018)
car_2 = car("Skyline" , "Nissan" , 2004)
car_3 = car("LFA" , "Lexus" , 2010)

print(car_1.get_model())
print(car_1.get_make())
print(car_1.get_year())

print(car_1.get_model())
print(car_1.get_make())
print(car_1.get_year())