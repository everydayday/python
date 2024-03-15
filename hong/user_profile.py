def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('albert', 'einstein', lacation = 'princeton', field = 'physics')
print(user_info)

my_info = build_profile('daehee', 'kim',location = 'busan', field = 'programmer', hobby = 'neflix')
print(my_info)

def make_car(comp, model, **cars):
    cars['comp_name'] = comp
    cars['model_name'] = model
    return cars

car = make_car('subaru', 'outback', color = 'blue', tow_pacakge = True)
print(car)