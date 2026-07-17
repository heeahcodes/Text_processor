





#variable names can not start with digits
"""
print("This is world's most expensive two values calculator ")
num1 = int(input("What is your age? ")) #changing type is called 'casting'
#variable names are case-sensitive num1 =/= Num1
#in python equal sign is variable assignment not 'equivalence'
num2 = int(input("What is your gremlin's age? "))
#storing info in a variable makes it a 'python object', value is what's is stored in it

variables are only visible inside the function in which they were created 
- SCOPE of a function. e.g if main() has a function boom_boom() 
boom_boom() is limited to main() only

total_age = num1 + num2
#adding strings is called 'concatenation'
print("You and your gremlin add up to " + str(total_age) + ".") #we are adding strings together, is why we converted to int(total)
#print(f"You and your gremlin add up to {total_age}")
#subsequent assignment to a variable, say 'a' changes it's value to the newer value

TYPE of values in Python
int = integer (can be negative)
float = real numbers aka Decimals [from IEEE - floating point standard] can be negative
str = text {str(10) =/= int(10}
Bool = boolean [True or False]
"""
#Why are INTs and FLoats Diff
"""
To differentiate how much from how many: int = how many (has next number) 25kg, 26,kg etc. 
float = how much (no next number) e.g 25.56 -> 25.561 or 25.57? 
How many children do you have? Int , How much do you weigh? float. 
We don't count in real numbers 

#we can print multiple items separated by a comma
#print("my bmw", x, "grapefruit", capy_bara, y)
#CONSTANTS - used to represent a number that will not change, e.g '9.5' in CGPA
#Constants are written in ALL_CAPS
#RANDOM numbers

import random
random.randint(1,144) #returns a random integer between the limits, inclusive
random.random() #returns a random float between 0 and 1
random.uniform(3,144) #returns a random float between the limits
#random.seed(x) #sets the 'seed' of the random number generator to X = some value
from ai import call_gpt

a = float(input("elskjfl "))
blue=6
plum=9
plant = input("enter plant ")
if plant==blue:
    print("azul")

import random #imports random library
py_guess = random.randint(1,100) #random.randint imports integers only, limits inclusive
print (" Guess a number game")
user_guess = int(input(" Guess a number!")) #first assignation of the user input variable
while user_guess != py_guess: #while loop will run as long as user input does not equal machine number
    if user_guess < py_guess:
        print("too low, try again:")
    else:
        print("too high, try again: ")
    user_guess = int(input("enter new guess")) #notice how user_guess is reassigned inside the loop!
print(f"you won! The number was {py_guess}") #post_condition after the break of while loop

curr_value = int(input("Enter a number: "))
while curr_value < 100:
    curr_value = curr_value * 2
    if curr_value <= 100:
        print(curr_value)
    else:
        print('greater than hundred')
    curr_value = int(input('enter another number: '))

for i in range (0,30,2):
    print(i)

for i in range(30):
    numkilloo = i * 2
    print(f" {numkilloo} {i}"

import tkinter
p = tkinter.Canvas(height = '500', width = '500')
p.pack()
p.create_line(0,0,500,500)
p.create_oval(30,67,80,97, fill = "#675fb6")
p.create_rectangle(78,189,112,295, fill = "#49bf08")
p.mainloop()

#takes user input on how many numbers to add
n = int(input("enter n: "))
#asks for list elements
for i in range(n):
    li_st = [(int(input(f" enter an number ")))]
    list.append()
def average(n):
    for 
#finds the average of the list element
average(li_st)
    av_1 = average(144, 345, 983)
    av_2 = average(609, 672, 122)
    av_3 = 0
    av_4 = round(average(av_1, av_2, av_3), 3)
    print(f" grand average is {av_4}")

def average(x, y, z):
    summ = x + y + z
    return summ/3

import tkinter
def main():
p = tkinter.Canvas(height = '500', width = '500')
p.pack()
p.create_line(0,0,500,500)
p.create_oval(30,67,80,97, fill = "#675fb6")
p.create_rectangle(78,189,112,295, fill = "#49bf08")
p.mainloop()

if __name__ == '__main__':
    main()

def main():
    for i in range(1, 21):
        if is_odd (i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

def is_odd(i): #my early version
    if i%2 == 0:
        return False
    return True

#what Chris did
def is_odd(i):
    return i%2 == 0

#checkerboard drawing.
import tkinter
Canvas_length = 400
Canvas_breath = 400
n = 64
box_size = Canvas_breath / n
def main():
#draw canvas
    #checkerboard 64 squares, alternate black and white
    p = tkinter.Canvas(height = '500', width = '500')
    p.pack()
    for i in range (n):
        draw_square(p, r, c)
    p.mainloop()
def draw_square(p, r, c):
    top_x = n * box_size
    top_y = n + box_size
    bottom_x = top_x + box_size
    bottom_y = top_x + box_size
    square = p.create_rectangle ( p, top_x, top_y,bottom_x,bottom_y,fill = 'white', outline = 'black')

if __name__ == '__main__':  # boilerplate
    main()

my_list = []
n = int(input("enter how many numbers "))
for i in range(n):
    elem = int(input("enter a number"))
    my_list.append(elem)
avg = round(sum(my_list)/len(my_list),3)
print(f" avg is {avg}")


candy_number = 0
while candy_number < 6:
    print(f"you have {candy_number} candies.")
    candy_number =+ 1
    if candy_number == 6:
        print(f"{candy_number} is enough candies! ")
print ("come again another day")

with open('E:\\python file reading practique.docx') as f:
    for line in f:
        print (line)
print('finished')
"""