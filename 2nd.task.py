import random
def roll_dice(sides):
    return random.randint(1, sides)
# Main program
max_sides = int(input("enter the number of sides on dice: "))
result = 0
while result != max_sides:
    result =roll_dice(max_sides)
    print(result)
