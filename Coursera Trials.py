"""
#basic function, requires parenthesis and can use both single and double quotes, print is only for showing
print('Hello')
#print to the console does something similar but only with values
print (22)
#the following function gives a zero exit code because it just completed its process inside and didn't show it to you
9 + 1 / 2
#python performs simple arithmetic probs. To show the output, you need the print function. To store it 'return'
print((5 + 6) / 3)
#you can assign variables using single =
name = "Green computing"
number = "pink computing"
print (name, number)
#to check if something is equal to something use ==
if 10*3 == 30:
    print ("It is thirty!")
#the following commands always use (:) at the end:
#These are all indented commands - def, if, class, elif, else, for, while, loops,
# try/except blocks, with statement and dictionary key values
# conditional statements in
#the above code (removed to Notion) didn't work because INPUT always returns STR, Python can't compare STR (a) to INT (18) so convert it
a = int(input('What is your age? '))
if a >= 18:
    print ('boring adult')
else:
    print('aww baby! ')

user_name = input("enter username: ")
if len(user_name) < 8: #len function uses to find length of strings or other objects
    print("invalid: choose another username ")
elif len(user_name) == 8:
    print("Siiiiiiiiiiiiiiiiiiiii")
else:
    print("hola senor su casa es mi casa habla punta")
"""
#WHAT IS A MODULO (%)? = Operator that returns the remainder once a num is divided by something
# '/' is division and '//' is floor division
'''
def zodic_plu(aqua , piscine):
    return round(aqua%piscine)
print(zodic_plu(12,5)

print("Hello World, Baby Py is BACK!")
user_mood = input("Enter your mood here :")
        if user_mood == '1' or user_mood == '2' or user_mood == '3':
            print("Great! Good going friend.")
        elif user_mood == '4' or user_mood =='5' or user_mood =='6':
            print('Yay! Happy for you, friend')
        else:
            While True:
                print("wrong input format. Enter a number")'''








