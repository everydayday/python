print("hello")
name = 'ada lovelace'
first_name = 'ada'
last_name = ' lovelace '
full_name = f"{first_name}\t{last_name.title()}!"

bicycle = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycle[-1])
message = f"bicycles was a {bicycle[-1].title()}!!"
print(message)

motorcycles = ['honda' , 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('GM')
print(motorcycles)

motorcycles.insert(0, 'Tesla')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop(1)
print(popped_motorcycles)

last_owned = popped_motorcycles
print(f"The last motorcycle I owned was a {last_owned}.")

motorcycles.remove('ducati')
print(motorcycles)



