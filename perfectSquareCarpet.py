import math

def calculate(field): # We find the largest possible perfect squares and print them
    if(field > 0):
        i = int(math.sqrt(field))
        field = field - (i*i)
        print(i*i)
        calculate(field)


while(True):
    field = int(input("Please enter the square meter of the field:")) # We take the square meter of the field from the user
    if (field < 0 ): # The field cannot be negative
        print("The field cannot be negative!!")
        continue
    print("Output: ")
    calculate(field) # We assign the value we get from the user to the calculate function


