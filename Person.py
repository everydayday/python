from typing import Any


class Person:
    count = 0 ### 클래스 변수
    def __init__(self,name,age,address): # 생성자
        self.name = name ### 인스턴스 변수
        self.age = age
        self.address = address
        self.weight = [1,2,3,4]    # 공개 속성
        self.height = 170
        self.__vision = 1.0 # private 속성
        self._number = [n for n in range(1, 11)]
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1
        print("클래스 변수 {}".format(self.count))

    @classmethod ### decorator - 자바 용어 : annotation
    def printing(cls):  ### cls : class  
        print("객체수는 {}".format(cls.count))


    def __call__(self, height, weight,g):
        print(weight / height **2 )    

    def __len__(self):
        return len(self.weight) 

    # 호출하는 방식이 다름
    def __str__(self): # Person은 객체,  출력시 필요한 것은 스트링
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    
    def __eq__(self,other):
        return self.age == other.age
    
    def show_person_vision(self):
        print(self.__vision)

    def __getitem__(self, index):
        return self.weight[index]
    
    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))


Person("guest", 11, "jeju")



new_person = Person('kim', 20,'busan')
other_person = Person('Lee', 20, 'busan')
Person.printing() ## 클래스 메소드 호출
new_person.printing()

print(f"person 객체의 나이는 {new_person.age:4}")
print("객체의 타입은 {}".format(isinstance(new_person, Person)))
print(new_person[2])

new_person(1.7,60.0,5)


print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
#print("시력은 {}".format(new_person.__vision))
new_person.show_person_vision()

print(str(new_person))
print(new_person.__str__())
print(new_person)

print(len(new_person))

print(f"count의 개수 : {new_person.count}")




