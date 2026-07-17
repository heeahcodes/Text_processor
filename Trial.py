print('hello Heeah, welcome to Python. Your journey starts here')
age = 20
print(age)
age = 6.987
print(age/2)
price=19.95
first_name = "Mosh"
is_online =False
age = 20
print(price)
first_name = "John Smith"
status = "unregistered patient"
print(age,first_name,status)
name = input('Comment vous appelle? ')
print("Hello" + name)
Dob = input('Enter Date of Birth ')
print("Your DoB is" + Dob)
query = input(' Is it your Birthday today? ')
#print is a function now and requires parentheses even if they are empty
def greetings (name):
    print("welcome" + name + "!")
    print ("your python is showing")
    #funciton arguments are written in parenthesis
greetings ("Heeah")
def area_triangle (base, height):
    return base * height / 2
#to calculate area of two triangles
area_a = area_triangle(5,4)
area_b = area_triangle(7, 3)
total_area = area_a + area_b
def get_seconds(hours, minutes, seconds):
    total_seconds = 3600*hours + 60*minutes + seconds
    return total_seconds
get_seconds (16, 45, 20)
