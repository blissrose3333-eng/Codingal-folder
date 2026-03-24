def factorial(x):
    """This ia a recursive function to find the factorial of a interger """
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 0:",factorial(0))
print("The factorial of 3:",factorial(3))
print("The factorial of 6:",factorial(6))
print("The factorial of 9:",factorial(9))
print("The factorial of 12:",factorial(12))
print("The factorial of 15:",factorial(15))