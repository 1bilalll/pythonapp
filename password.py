import string
import random 
letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(string.digits)
passwords=[]
l=int(input("how many letters would you like in your password: "))
for i in range(l):
    passwords.append(random.choice(letters))
s=int(input("how many sembols would you like in your password: "))
for i in range(s):
    passwords.append(random.choice(symbols))
n=int(input("how many numbers would you like in your password: "))
for i in range(n):
    passwords.append(random.choice(numbers))
random.shuffle(passwords)
print("".join(passwords))
