for value in range(6): 
    print(value);
numbers = list(range(6))



number_set = {}
squares = []    # list 변수
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(value)

squares = [value **2 for value in range(1, 11)]
print(squares)
print(squares[-3:])

my_list = [1, 2, 3, 4, 5, 6, 7, 8]


print(my_list[::-3])

# a = [1, 2]
# b = [3, 4]
# c = a + b

# print(c)

# b = [0]
# c = b*5
# print(c)

my_food = [['pizza', 'falafel'], ['bannana', 'orange']]
friend_food = my_food[:]

friend_food.append('ice cream')

print(my_food)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
            print(player.title())

a = [[1,2,3],[4,5,6]]
b = a[:]
print(b) #[[1,2,3],[4,5,6]]
a[0][0] = 100

print(a)

my_food = ['pizza', 'falafel']
friend_food = my_food

friend_food.append('ice cream')

print(my_food)