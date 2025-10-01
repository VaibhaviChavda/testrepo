#que-1
# a = int(input("enter number"))
# if a > 0 :
#     print("number is positive",a)
# else :
#     print("not positive")-8

#que-2
# marks = int(input("enter marks: "))
# if marks >= 35:
#     print("you are pass!")

#que-3
# num1 = int(input("enter number: "))
# if num1 % 2 == 0 :
#     print("number is Even")
# else:
#     print("number is odd")

#que-4
# num1 = int(input("enter number :"))
# if num1 % 5 == 0:
#     print(num1, "is divisible by 5")
# else:
#     print(num1,"not divisible by 5")

#que-5
# marks = int(input("enter marks : "))
# if marks < 40:
#     print("you are pass")
# elif marks <= 60:
#     print("your grade is 'c'")
# elif marks <= 75 :
#     print("your grade is 'B'")
# elif  marks <= 85:
#     print("your grade is 'A'")
# elif marks <= 99:
#     print("your grade is 'A'")
# else:
#     print("enter valid marks!!!")
    
#que-6
# number = int(input("enter number: "))
# if number == 0:
#     print("ZERO")
# elif number > 0:
#     print("POSITIVE")
# else:
#     print("NEGETIVE")

#que-7
# num = int(input("enter number(mnonth 1-12): "))
# match num:
#     case 11|12|1|2:
#         print("Hello winter")
        
#     case 3|4|5|6:
#         print("Hello Summer")
        
#     case 7|8|9|10:
#         print("Hello monsoon")

#     case _: 
#         print("not valid!!")

#que-8

# age = int(input("enter your age"))
# weight = int(input("enter your weight"))

# if age < 20 & weight <45:
#     print("you are fit")
# elif age < 40 & weight < 55:
#     print("you are fit")
# else:
#     print("you need somre imporvemetnt")
    
# #que-9
# day = int(input("enter day(1-7): "))
# match day :
#     case 1:
#         print("monday")

#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("Invalid")

#que-10
year = int(input("enter year"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("this is leap year")
else:
    print("this is not leap year")