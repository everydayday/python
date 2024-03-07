# p. 247 연습문제 풀기

# class Dog:
#     """개를 표현하는 클래스"""

#     def __init__(self, name, age):  # __ 특별 의미 : 자동호출 된다 # 생성된 객체 자기 자신
#         """name과 age 속성 초기화"""
#         self.name = name    # java 의 필드에 해당 함
#         self.age = age
#         self.__price = 100


#     def sit(self):
#         """앉기"""
#         print(f"{self.name} is now sitting")
#         print(self.__price)

#     def roll_over(self):
#         """구르기"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog("Willie", 6) # 생성자 호출 > 인스턴스 생성 > __init__ 함수가 자동 호출
# my_dog.sit()


# your_dog = Dog("Lucy", 3)
# your_dog.sit()
# print(f"너의 개는 {your_dog.name}")

# 9-2
class Restaurant :
    def __init__(self, rname, rtype):
        self.restaurant_name = rname
        self.cuisine_type = rtype

    def decribe_restaurant(self):
        print(f"restaurant_name : {self.restaurant_name}")
        print(f"cuisine_type : {self.cuisine_type}")

    def open_restaurant(self):
        print("레스토랑이 문을 열었습니다.")

new_rest = Restaurant("유가네", "한식")
new_rest.decribe_restaurant()
new_rest.open_restaurant()

second_rest = Restaurant("아웃백", "양식")
second_rest.decribe_restaurant()
second_rest.open_restaurant()

third_rest = Restaurant("쿠우쿠우", "양식")
third_rest.decribe_restaurant()
third_rest.open_restaurant()

class User :

    def __init__(self, fname, lname, tel, address) :
        self.first_name = fname
        self.last_name = lname
        self.telphone = tel
        self.address = address

    def greet_user(self):
        print(f"first name : {self.first_name}")
        print(f"last_name : {self.last_name}")
        print(f"telphone : {self.telphone}")
        print(f"address : {self.address}")



us1 = User("daehee", "kim", "010-123456798","부산시")
us2 = User("Amy", "Robert", "010-456456779","U.S")
us3 = User("Andrew", "Paul", "010-446448892" ,"Mexico")

us1.greet_user()
us2.greet_user()
us3.greet_user()

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

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()  # 하위 구성 객체 사용






