def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check
    x = number 
    if x % 15 == 0 :
        x = "Fizz Buzz"
    elif x % 5 == 0 :
        x = "Buzz"
    elif x % 3 == 0 : 
        x = "Fizz"
    else :
        x = str(x)
# replace this for solution
    return x
