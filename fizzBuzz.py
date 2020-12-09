x = 1
while(x <= 100):
    if(x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif(x % 3 == 0):
        print("Fizz")
    elif(x % 5 == 0):
        print("Buzz")
    else:
        print(x)
    x += 1

# One liner
# x = 100
# print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1, x)))