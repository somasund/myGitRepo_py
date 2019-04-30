# 1) For the string "Monty Python's Flying Circus", replace the 'y' with 'i' from typing import List

print("Question 1")
var = "Monty Python's Flying Circus"
a = list(var)

for temp in range(len(a)):
    if a[temp] == 'y':
        a[temp] = 'i'

print(''.join(a))

# 2) For the string "Sea shells on the sea shore", find how many times 's' occurs

print("Question 2")
var = "Sea shells on the sea shore"
a = list(var)

c = 0

for i in range(len(a)):
    if a[i] == 's':
        c = c + 1
print("the number of s occurs are:", c)

# 3) For the string "Monty Python's Flying Circus", tokenise the string on words
print("Question 3")
mystr = " Bucky is awesome"
x = mystr.split()
print(x)

# 4) Define the string that contains "I am writing the python code" - Split the sentence based on 'space character'
print("Question 4")
stringIp = "I am writing the python code"
splitOp = stringIp.split(" ")

print(splitOp)

for x in splitOp:
    print(x)


# 5) Input a String from the user and print the string in reverse order.
# Eg: If the user is entering "Python", then print the output as "nohtyP"

print("Question 5")
x = input("Enter a string to reverse: ")
y = list(x)
y.reverse()
print(''.join(y))
