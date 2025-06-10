import random
import re

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)
print(starWars[len(starWars) -14])

print(re.sub("[a-zA-Z: -]","",starWars))
print(re.sub("[^0-9]","",starWars))
# print(re.sub("[^\d]","",starWars))


num = 20
#       0  1  2   3   4   5
nums = [1, 5, 10, 20, 80, 3] # vienos dimensijos masyvas
print(nums)
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[5])
# print(nums[6])

nums[0] = 50

print(nums)

# nums[6] = 40
# print(nums)
nums.append(40)
print(nums)
nums.sort(reverse=True)
print(nums)
print(nums.count(50))

print("---------------------")
for skaicius in nums:
    print(skaicius)

print("zemiau ciklo")


rng = range(5,10)
print(rng)

for x in rng:
    print(x)

for x in range(0,10):
    print("labas")

print("----------------")

i = 0

while i < 10:
    i+=1
    print(i)

# i = 0
# while True:
#     if i % 1000000 == 0:
#         print(i)
#     i+=1

i = 0
while True:
    i +=1
    print(i)
    if i > 5:
        break

i = 0
while True:
    i +=1
    if i % 3 == 0:
        continue
    print(i)
    if i >= 50:
        break

print("----------------")

while True:
    rnd_num = random.randint(0,1);
    print(rnd_num)
    if(rnd_num == 1):
        break

my_numbers = []

for i in range(5):
    my_numbers.append(random.randint(5,25))
print(my_numbers)

count = 0
index_counter = 0
for num in my_numbers:
    index_counter +=1
    if num > 10:
        count += 1
print("didesniu uz 10 " + str(count))

for index, num in enumerate(my_numbers):
    print(index, num)

#           0   1   2   3
letters = ["A","B","C","D"]
letters[0]
for i in range(20):
    print( letters[ random.randint(0,3)  ] )

for i in range(10):
    print(i)

for i in range(len(letters)):
    print(str(i) + " " + letters[i])

for i in range(len(letters)):
    print('i = ' + str(i) + ', letters['+str(i)+'] = ' + letters[i])

ingridientai = ["Kaliarope", "artisokas", "patisonas", "humusas"]

for fui in ingridientai:
    print(fui)

for y in range(1, 11):
    for x in range(1, 11):
        print(str(x * y) + " ", end="")
    print()

new_array = ["labas","vakaras","studentai"]

num_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("nu ka, pavyko?:) dabar jau???")

print("labas ir ate")
