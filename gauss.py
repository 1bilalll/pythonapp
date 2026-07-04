
n=int(input("until which number to do: "))
for number in range(1,n+1):
    if number%3==0:
     print("Fizz")
    elif number%5==0:
       print("Buzz")
    else :   
        print(number)
