short_msgs = ["잘 지내?", "식사 하셨어요?", "잘자"]

def show_messages(msgs):
    for msg in msgs:
        print(msg)

############# 2번 ################
sent_messages = []
def send_message(msgs):
    for msg in msgs:
        sent_messages.append(msg)

'''
send_message(short_msgs)


show_messages(short_msgs)
show_messages(sent_messages)
'''
############## 3번 ################


send_message(short_msgs[:])

show_messages(short_msgs)
show_messages(sent_messages)


# def make_pizza(size, *toppings):  # tuple로 받은 것
#     """요청받은 리스트"""
#     print(f"size = {size}::")
#     for topping in toppings:
#         print(f" -{topping}")
    

# make_pizza(16, 'pepperoni')
# make_pizza(17, 'mushrooms','green peppers','extra cheese')

def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton', 
                             field = 'physics')
print(user_profile)







