#submitted by Keren Or Hadad 208025205

# Python Program to Find the Perfect Number between 1 to a Specific Range
# Take the input from the user

MinValue = int(input("Enter any Minimum Value: "))
MaxValue = int(input("Enter any Maximum Value: "))

# initialise sum
print("\nPerfect Number Between {0} to {1}".format(MinValue,MaxValue))
# Checking the Perfect Number
for Number in range(MinValue, MaxValue - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n
    # display the result
    if(Sum == Number):
        print("%d " %Number)