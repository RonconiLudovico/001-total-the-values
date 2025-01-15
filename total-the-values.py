# First we'll start by defining a function in which we state the variable sum to be starting at 0
# Then we ask the user to input a number
def values_total(sum=float(0)):
    value = input("Please enter a value: ")

    if value == "": # Here we'll state a condition for which if the input is equal to a blank line the total should be outputted
        print(sum)
        return
    
    else: # Otherwise the number inputted should be added to the variable sum and the function recursed
        sum += float(value)
        values_total(sum)



if __name__ == "__main__":
    values_total()