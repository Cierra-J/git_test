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


user_int = int(input("How many integers would you like to enter?: "))
total_num_letters = 0
print("Please enter the names of your three favorite animals.")
for val in range(1,4):
    animal = input()
    for letter in animal:
        total_num_letters += 1
    print("Those names contained a total of", total_num_letters, "characters")

totalint = int(input("Please enter an integer:"))
total = 0
for num in range(1, totalint+1):
    total += num
print(total)
total_ch = 0
user_str = (input("Enter a sentence: "))
for ch in user_str:
    total_ch += 1
if total_ch % 2 ==0:
    print("even")
else:
        print("odd")
while True:
    user_input = input('enter a quote. type quit to exit: ')
    if "quit" in user_input:
        break
    print(user_input)
