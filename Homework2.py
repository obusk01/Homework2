#Olivia Busk
#Homework 2

#Problem 1

def print_name(name):
    print("The name is", name)

print_name("Olivia")
print_name("Henry")


#Problem 2
# (a+b+c+d)/4=90

def ninety(a,b,c):
    d= 360-(a+b+c)
    return d
print(ninety(34,76,23))

#Problem 3
# 3600 seconds in an hour

def miles_per_hour(miles,hours,minutes,seconds):
    total_hours= hours+(minutes/60)+(seconds/3600)
    mph=miles/total_hours
    return mph
print(miles_per_hour(20,2,21,16))


#Problem 4

def name(x):
    if x=="Chris":
        print("Hello Chris!")
    else:
        print("Goodbye!")

name("Olivia")
name("Chris")

#Problem 5
def convert_temperature(temp,units):
    if units=="celsius":
        new_temp=(temp*(9/5))+32
        return new_temp
    if units=="farenheit":
        new_temp2=(temp-32)*5/9
        return new_temp2
print(convert_temperature(45,"celsius"))
print(convert_temperature(45,"farenheit"))

#Problem 6
def calculate_grade(score):
    if score>90:
        print("Your grade is an A")
    if 80<score<90:
        print("Your grade is a B")
    if 70<score<80:
        print("Your grade is a C")
    if 60<score<70:
        print("Your grade is a D")
    if score<60:
        print("Your grade is an F")
calculate_grade(45)
calculate_grade(78)
calculate_grade(99)
calculate_grade(85)

        
