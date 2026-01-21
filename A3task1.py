def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
number=int(input("Enter a number: "))
ans=factorial(number)
print(f"THe factorial of {number} is : {ans}")

