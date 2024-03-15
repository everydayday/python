# p. 257

# 9 - 13

from random import randint
class Die:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print("주사위 눈 : {}".format(randint(1, self.sides)))

dice = Die()
for i in range(10):
    dice.roll_die()

print("#" * 20)

dice10 = Die(10)
dice20 = Die(20)

print("10면체 출력")
dice10.roll_die()

print("20면체 출력")
dice20.roll_die()

print("#" * 20)
# 9-14
from random import choice

lott = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]
p1 = choice(lott)
p2 = choice(lott)
p3 = choice(lott)
p4 = choice(lott)

print("{}, {}, {}, {}와 만족하는 티켓에 상금을 지급합니다.".format(p1,p2,p3,p4))

# 9-15
my_list = [4,6,"a","b"]

count = 0
while True:
    count += 1
    p1 = choice(lott)
    p2 = choice(lott)
    p3 = choice(lott)
    p4 = choice(lott)

    if p1 == my_list[0] and p2 == my_list[1] and p3 == my_list[2] and p4 == my_list[3]:
        break

print("{}번 실행했습니다.".format(count))

