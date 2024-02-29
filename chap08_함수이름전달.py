# 함수의 매개변수로 함수 전달하기
def ten_times(func):
    for i in range(5):
        func()



def print_hello():
    print("hello")

ten_times(print_hello)