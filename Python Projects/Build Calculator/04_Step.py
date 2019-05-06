# Building a calculator

import re

print("Our Magical Calculator")
print("      S H A D I\n")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, human.")
        run=False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()


# Our Magical Calculator
#       S H A D I
# Type 'quit' to exit

# Enter equation: 5+1
# 6*3
# 18+11
# 29-23
# 6*12
# 72%12
# Enter equation: quit
# Goodbye, human.