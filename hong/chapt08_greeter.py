def greet_user(username): # 스트링은 immutable 
    """인사말"""
    
    print(f"hello, {username.title()}!")
    # username = 'kim'

inputname = 'jesse'
greet_user(inputname)
input_name = 'kim' # 값의 변경이 아니라 변수를 다시 설정
print(inputname)

# help(greet_user.__doc__)

def describe_pet(animal_type, pet_name = 'ohgett'): # default parameter
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

def get_formatted_name(first_name, last_name, middle_name = ''):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    if middle_name : 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
         full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix','lee' )
print(musician)


### map(), filter() 함수 사용
# def apply_func(func, x, y):
#     return func(x,y)



# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

power = lambda x : x * x    
under_three = lambda x : x < 3

lst = [1, 2, 3, 4, 5]

map_list = map(power, lst)
print(f"map() 함수 적용결과: {list(map_list)}")

#filter_list = filter(under_three, lst)






