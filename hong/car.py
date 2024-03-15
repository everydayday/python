

class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """자동차의 주행거리를 출력합니다."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")    

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery :
    """배터리"""
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")



class ElectricCar(Car): 
    """ElectricCar"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()