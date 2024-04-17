count = 0
product = 1
while product < 100:
    next_num = int(input('Please enter an integer: '))
    count += 1 #also means count + 1
    product *= next_num
print(f'You entered {count} numbers whose product is {product}.')

name = input(" Please enter your pet's name: ")
rev_name = ""
for ch in name:
    rev_name = ch + rev_name
print(rev_name)

upper_limit = int(input('Please enter an integer: '))
total = 0
for num in range(1, upper_limit + 1):
    total += num
print(total)

upper_limit = int(input('Please enter a number: '))
total = 0
for num in range(1, upper_limit + 1):
    if num % 2 == 1:
        total += num
print(total)

upper_limit = int(input('Please enter an number: '))
total = 0
for num in range(1, upper_limit + 1, 2):
    total += num
print(total)

user_num = int(input("Enter a number: "))
if 50 < user_num < 100:
    print("in range")
else:
    print("out of range")

user_num2 = int(input("Enter a number: "))
if user_num2 < 10:
    size = "small"
elif user_num2 >= 10 and user_num2 < 50:
    size = "medium"
elif user_num2 >= 50:
    size = "large"
print("Your dog is", size)

userint = int(input("Enter a number: "))
#write code that reads input from user. if that integer is a value from 1-5,
# your program should print out the english word for that number
if userint == 1:
    print("one")
elif userint == 2:
    print("two")
elif userint == 3:
    print("three")
elif userint == 4:
    print("four")
elif userint == 5:
    print("five")
else:
    print("out of range")

word = "apothecary"
for letter in word:  # letter is the loop variable
    print(letter)
    
