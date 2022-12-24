"""########################################"""
#escape sequence and new line character

# print("Hello, My name is Om Jaiswal", end=",")   #end is a new line character

# print("Hello, My name is Om Jaiswal \n I am 18 \t hi")   #\n and \t are escape sequence


"""#########################################"""
#Variables, Datatypes and Typecasting

# var1 = "Hello"
# var2 = 5
# var3 = 0.2
# var4 = " World"
# var5 = "2"
# var6 = "3"

# print(type(var3))   #prints the type of variable
# print(var2 + var3)
# print(var1 + var4)
# print(var6 + var5)
# print(10*(int(var5) + int(var6)))
# print(10*"Hello Om\n")


# print("Enter your number")
# var7 = int(input())
# print((var7)+5)

"""##############################################"""
#QUIZ 1 - Make a simple calculator

# print("Enter the first number")
# var1 = int(input())
# print("Enter the second number")
# var2 = int(input())
# print("The sum of the entered numberes is", var1+var2)

"""##############################################"""
#string slicing and other functions

# mystr = "My name is Om Jaiswal"
# mystr2 = "mynameisomjaiswal"

# print(mystr[0])
# print(mystr[0:2])
# print(len(mystr))
# print(mystr[0:7:2])   #prints 0-7 and skipping every 2nd letter

# print(mystr2.isalnum())
# print(mystr2.endswith("l"))
# print(mystr2.capitalize())
# print(mystr2.count("a"))
# print(mystr2.find("is"))
# print(mystr2.upper())
# print(mystr2.replace("is", "are"))

"""#############################################"""
# python lists| list functions | touple


# mylist = ["Aloo", "Bhindi", "Vaseline", "Tomato", 54]
# mynum = [5,56,5,58,89,98,1,3,8]

# print(mylist[0:3:2])
# mynum.sort()
# mynum.reverse()
# mynum.append(7)          #adds the item to the end of the list 
# mynum.insert(1,65)       #inserts no. 65 at index no. 1
# mynum.remove(3)          #it removes the 3 number, not the location 3
# mynum.pop()              #removes the last item in list
# print(mynum.index(1))    #prints the index number of the item

# mynum[0]= 10             # a list is mutable
# print(mynum)

# tp = (1,2,3,4,5)         # a touple is immutable
# print(tp)           

# a=1
# b=2
# a,b=b,a         #interchanging variable values
# print(a,b)

"""############################################"""
#Dictionary

d1 = {"om":"kyro", "kairavi":"banana", "neeraj":"roti", "krishna":{"B":"roti", "L":"eggs"}}

# d1["Ankit"] = "Junk food"      #added items
# print(d1["krishna"]["L"])
# del d1["om"]
# d2= d1.copy()
# del d2["om"]
# print(d1)

# d1.update({"leena":"toffee"})  #also used to add items
# print(d1.items())


"""############################################"""
#Question - Create a dictionary and take input from the user and return the meaning of the word from the dictionary

# d1 = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5"}
# print("Enter any letter from a-e to know it's meaning:-")
# inp = input()
# print(d1[inp])


"""############################################"""
# Set

# s = set()                                #creates a blank set
# print(type(s))

# s_form_list = set([1, 2, 3, 4])
# print(s_form_list)

# s3 = {1,2,3,}
# print(type(s3))

# s.add(1)
# s.add(1)

# s1 = s.union({1,2,3})
# s2 = s.intersection({1,2,3})

# print(s1,s2)


"""############################################"""
# if else, elseif conditions

# var1 = int(input())
# if var1 > 100:
#     print("Greater than 100")
# else: 
#     print("lesser than 100")
#     var2 = int(input())
#     if var2 < 50:
#         print("Better luck next time")
#     else:
#         print("Congratulations")


# list = [1,2,3, 65]
# input = int(input())
# if input in list:
#     print("It is already in the list")
# else:
#     list.append(input)
#     print("The number was added to the list")
#     print(list)
"""############################################"""
#Question 2- Faulty calculator

# print("Enter the first number")
# num1 = int(input())
# print("Enter the second number")
# num2 = int(input())
# print("Enter the operator")
# operation = str(input())

# if (num1==45 or num1==3) and (num2==3 or num2==45) and operation=="*":
#     print("555")

# elif (num1==56 or num1==9) and (num2==9 or num2==56) and operation=="+":
#     print("77")

# elif num1 == 56 and num2 == 6 and operation == "/":
#     print("4")

# else:
#     if operation=="+": print(num1+num2)
#     elif operation=="-": print(num1-num2)
#     elif operation=="*": print(num1*num2)
#     elif operation=="/": print(num1/num2)

"""############################################"""
#for loops

# list = ("a", "b", "c", "d", "e", "f")
# print(list)
# for item in list:
#     print(item)

"""############################################"""
# Quiz-

# list1 = ["a", "g", "f", "2", "5", "8","79"]

# for item in list1:
#     if item.isnumeric() and int(item) > 6:
#         print(item) 
"""############################################"""
#while loops
# i=0
# while(i<45):
#     print(i)
#     i=i+1

"""############################################"""
# while(1):    
#     inp = int(input("Enter the no.- ")) 
#     if inp < 100:
#         print("Try again")
#         continue            #start the while loop again without executing the rest of the code
#     elif inp >= 100:
#         print("Congratulations the entered value is greater than 100")
#         break               #exit the while loop
"""############################################"""
# num = 54
# lives = 5
# while(1):
#     inp = int(input("Guess the integer number- "))
#     if inp>num:
#         print("Too high, decrease the number \n", (lives-1)," Lives left :(")
#         lives=lives-1
#         if lives==0:
#             print("GAME OVER :(")
#             break
#         continue
#     elif inp<num:
#         print("Too low, increase the number \n", (lives-1)," Lives left :(")
#         lives=lives-1
#         if lives==0:
#             print("GAME OVER :(")
#             break
#         continue
#     elif inp==num:
#         print("Congratulations, You have successfully guessed the number :) ")
#         break
"""############################################"""
#user defined functions and docstrings
# a = 9
# b = 8
# c = sum((a, b)) # built in function

# def function1(a, b):
#     print("Hello you are in function 1", a+b)

# def function2(a, b):
#     """This is a function which will calculate average of two numbers
#     this function doesnt work for three numbers"""
#     average = (a+b)/2
#     print(average)
#     return average

# v = function2(5, 7)
# print(v)
# print(function2.__doc__)
"""############################################"""
# #Try except 

# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print("The sum of these two numbers is", int(num1)+int(num2) )
    
# except Exception as e:
#     print(e)
#     print("This line is very important")

"""############################################"""
#Rock Paper and Scissors

# import random
# player_score = 0
# computer_score = 0
# while(1):
#     user_input = input("Choose rock, paper, scissores:- ")
#     list = ["r", "p", "s", "q"]
#     if user_input not in list:
#         print("Enter a valid command")
#         continue
#     if user_input == "q":
#         if player_score > computer_score: print("You won the game by", abs(player_score-computer_score), "points.")
#         elif player_score < computer_score: print("You lose the game by", abs(player_score-computer_score), "points.")
#         else: print("It was a tie")
#         print("Goodbye") 
#         break
#     random_num = random.randint(0,2)
#     computer_input = list[random_num]
#     if user_input == "r":
#         if computer_input == "s":
#             player_score += 1
#             print("You won")
#             print("You- ", player_score, "    Computer-", computer_score)
#         elif computer_input == "p":
#             computer_score += 1
#             print("Computer won")
#             print("You- ", player_score, "    Computer-", computer_score)
#         else:
#             print("same input")
#             continue
#     if user_input == "p":
#         if computer_input == "r":
#             player_score += 1
#             print("You won")
#             print("You- ", player_score, "    Computer-", computer_score)
#         elif computer_input == "s":
#             computer_score += 1
#             print("Computer won")
#             print("You- ", player_score, "    Computer-", computer_score)        
#         else:
#             print("same input")
#             continue
#     if user_input == "s":
#         if computer_input == "p":
#             player_score += 1
#             print("You won")
#             print("You- ", player_score, "    Computer-", computer_score)
#         elif computer_input == "r":
#             computer_score += 1
#             print("Computer won")
#             print("You- ", player_score, "    Computer-", computer_score)
#         else:
#             print("same input")
#             continue
"""############################################"""
# tic tac toe

# import random
# def board_layout():
#     print("This is the tic tac toe's board's input layout")
#     print(" 7 | 8 | 9")
#     print("---|---|---")
#     print(" 4 | 5 | 6")
#     print("---|---|---")
#     print(" 1 | 2 | 3")
# board_layout()

# def board(a,b,c,d,e,f,g,h,i):
#     print("",g,"|",h,"|",i)
#     print("---|---|---")
#     print("",d,"|",e,"|",f)
#     print("---|---|---")
#     print("",a,"|",b,"|",c)

# print("\n")

# a = " "
# b = " "
# c = " "
# d = " "
# e = " "
# f = " "
# g = " "
# h = " "
# i = " "
# board(a,b,c,d,e,f,g,h,i)
# rand = random.randint(1,9)

# while(1):
#     inp = [1,2,3,4,5,6,7,8,9]
#     O_input = int(input("O's turn"))
#     if O_input in inp:
#         if O_input == 1: a="O"
#         elif O_input == 2: b="O"
#         elif O_input == 3: c="O"
#         elif O_input == 4: d="O"
#         elif O_input == 5: e="O"
#         elif O_input == 6: f="O"
#         elif O_input == 7: g="O"
#         elif O_input == 8: h="O"
#         elif O_input == 9: i="O"
#         board(a,b,c,d,e,f,g,h,i)
#     else: print("Enter a valid command")
# #     X_input = int(input("X's turn"))
"""############################################"""
#  open and reading file

# f = open("file_read.txt", "rt")    #if opening a file like this make sur to close it
# content = f.read()
# print (content)
# f.close()

# with open("file_read.txt", "rt") as f:     #"rt" it is the default reading mode
#     content = f.read()
#     print(content)                    # opening the file this way is much better

# """############################################"""
#WRITING TO A FILE

# with open("file_write.txt", "w") as f:
#     f.write("Python is Awesome\n")
#     f.write("I love python")

"""############################################""" 
#Appending to a file

# with open("file_write.txt", "a") as f:
#     f.write("\nThis text is appended")

"""############################################""" 
#Check if a given string is a palindrome
# x = input("Enter the String:")
# if (x == x[::-1]):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

"""############################################""" 
# Write a program to check if the two input strings are an anagram of eachother or not

# x = input("Enter first string ")
# y = input("Enter second string")
# if(sorted(x)== sorted(y)):
#     print("They are anagrams")
# else:
#     print("They are not anagrams")

"""############################################""" 
# duplicate characters in a string

# string = "Electronics and Robotics club"

# for i in range(0, len(string)):  
#     count = 1
#     for j in range(i+1, len(string)):  
#         if(string[i] == string[j] and string[i] != ' '):  
#             count = count + 1;  
#             string = string[:j] + '0' + string[j+1:];  
#     if(count > 1 and string[i] != '0'):  
#         print(string[i]);  

"""############################################""" ,
# my_list=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"7"}
#     ]
# c=[]
# for i in my_list:
#     c.extend(list(i.values()))
# c=list(set(c))
# print (str(c))

"""############################################""" 
# matplotlib

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,2,8]

# plt.plot(x,y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("The Graph")
# plt.legend()
# plt.show()

"""############################################""" 
#open CV

import cv2 as cv

img = cv.imread("Photos/shell.jpg")

cv.imshow("Shell", img)
cv.waitKey(0)

"""############################################""" 
"""############################################""" 
"""############################################""" 

