# def printHello():
#     print("hey there! i'm in a function!!")

# def helloName(name):
#     print(f"Welcome to python, {name}!!! You're a true pythonian now!")

# def power(base, exponent):
#     number = 1
#     for i in range(0, exponent):
#         number = number * base
#     return number

# printHello()
# for i in range(0,101):
#     printHello()
# helloName("Davina")
# print(power(2,8))

def madlib1(adj1, adj2, bird, verb1, verb2, verb3, verb4, houseRoom, name, noun1, noun2, noun3, liquid, bodyPart):
    return f"It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {houseRoom} downstairs. I {verb1}ed down the stairs to see if I could help {verb2} the dinner. My mom said 'See if {name} needs a fresh {noun1}' So I carried a tray of glasses full of {liquid} into the {verb3}ing room. WHen I got there, I couldn't believe my {bodyPart}! There were {noun3}s {verb4}ing on the {noun2}!" 

print(madlib1("brown", "scary","dodo", "run","sit","code","repeat", "foyer", "Billy", "baseball glove","hat","kitchen knife","mercury","nose"))