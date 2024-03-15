def test():
    return (10,20)

a,b = test(); # tuple 값을 리턴
print(f"a = {a}, b = {b}")

lst = ['a', 'b', 'c', 'd']
for i, value in enumerate(lst): # enumerate() 함수가 튜플을 리턴
    print(f"i = {i}, value = {value}")

# def get_formatted_name(first_name, last_name):
#     """실제 이름 반환"""
#     full_name = f"{first_name}, {last_name}"
#     return full_name.title()

# while True:
#     print("\n print your name")
#     f_name = input("first name: ")
#     if f_name == 'q':
#         break
#     l_name = input("lst name: ")
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nhello, {formatted_name}!")

def print_models(unprinted_designs, completed_models): # 리스트가 parameter이면 mutable
    """빈리스트일 때까지 출력"""
    


unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:    # 빈 리스트이면 false
    current_design = unprinted_designs.pop()    # 한 개씩 삭제
    print(f"printing : {current_design}")
    completed_models.append(current_design)
print("\n models printed")
for completed_model in completed_models:
    print(completed_model)



# immutable 객체를 함수로 전달 -> 변경 불가 확인

def modify_strings(s):  ## 스트링 값을 전달 받음
    # immutable 변수 :  튜플, 숫자, 스트링, 불리언 
    s = s + "world"     # 변수 s는 원래 변수가 가리키는 주소와 다름
    print(s)

st = "hello "
modify_strings(st)
print(st)   ## 출력 결과가 hello => 변경 안 됨





