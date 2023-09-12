print("hello , i am anant and you have to learn python  ")
# print ("hello anant")
# # there are modules varoius modules in python_branch
# # built-in module
# # external module
# # comments # for single line comments
# #          ''' for multi line comments'''
# # REPL (read evaluate print loop )

# # datatypes 
# # strings    = print ("anant")
# # integers   = 98
# # booleans   = it prints either true or false 
# # none       = it returns nothing (none)
# # float      = 8.90 , 7.65 , 574.08

# # identifing the datatypes
# a = ("anant")
# print(type(a))

# b = 89
# print(type(b))

# c = (8>9)
# print (type(c))

# d = 89.7
# print(type(d))

# # opereators in python
# # arithematic operators

# # addition 
# print("the value of 4+9 is", 4+9) 

# # subtraction
# print("the value of 5-2 is", 5-2)

# # multiplication
# print("the value of 7*8 is", 7*8)

# # divide
# print("the value of 10/5 is", 10/5)

# assigment oprators 
# a = 10

# a-= 5
# print (a)

# a+= 50
# print (a)

# a/= 15
# print (a)

# a*= 2
# print (a)

# comparison operators 
# r = (0>6)
# print(r) # as it compares wheather the given statment is right or wrong


# type casting 

# a =("4546")
# print(type(a)) #as it will print the type string
# # now we will typecast the string datatype into integer type.(if possible)
# a = int(a)
# print(a+2)

# f = input("enter your name")
# print("have a nice day,"+f)# this in results gives the compliment of having a nice day by entering your name.


# # write a program to add two numbers

# a = input("give me a number")
# b = input("give me a number")
# a = int(a) # you have to change the type of data from (string to integer).
# b = int(b)
# print( "the value of a+b is",(a+b) )


# write a program to find the remainder of a number
# a = input(" enter the no.")
# b = input(" enter the sec no.")
# a = int(a)
# b = int(b)
# print("the reaminder comes after dividing is", a%b)
# a=101
# b=50
# print(a%b)


# write a program to find the avrage no. enterd by the user
# g =input("enter the no.")
# j =input("enter the no.")
# g = int (g)
# j = int (j)
# av = ((g+j)/2)
# print( av)

# print(type(av))
# av = int(av)

# # changing the float type outcome to integer type.
# print(type(av))
# print(av)

# calculate the python program to write the square of a number entered by the number

# a = input("enter")
# b = input("enter")
# a = int(a)
# b = int(b)
# sq = a*b
# print("the square fo the number is", sq)

# name =("car")
# print(name(0))

# story = "once upon a time there was a youtuber named anant who eats a lot"
# print(len(story)) # this function will print how many characters you have in the stored variable

# print(story.endswith("lot"))# this will state how the story ends

# print(story.count("a"))# this will state how many given charecters the story contain.

# print(story.capitalize()) # ths function will capitalize the first letter.

# print(story.find("eats")) # this function will find the given word in its designated place

# print(story.replace("eats","runs")) #this function will replace the given word with the first word.



# input("enter your name")
# name = ("niharika") 
# print("anant loves",  name) 


# This is a letter template it can be used to print various date and name types with a give format.

# letter = ''' dear <|NAME|>,
# you are selected !
# i hope you are well
# date : <|DATE|>'''

# name = input("enter your name\n")
# date = input("enter date\n")

# letter =letter.replace("<|NAME|>", name)
# letter =letter.replace("<|DATE|>", date)
# print(letter)



# this program will detect double spaces 

# sg = ("this a string with double spaces  ") 
# doublespaces = sg.find("  ") #this function will detect the double spaces
# print(doublespaces)
# doublespaces =sg.replace("   "," ") # this function will replace double spaces with single spaces
# print(sg)



# lists
# a =[7,8,5,2,1,6]
# print(type(a))
# print(a[3])
# a[3]=12       # you can lo change the value of the list by doing this..
# print(a)
# print(a[0:4]) # you can also slice a list {{{first value is included and last value will be excluded}}}


# # list slicing 

# anant=("a","n","a","n","t")
# print(anant[0]) # this will print the 0th value of the list 
# print(anant[3]) # this will print the 3rd value of the list ( as starting from 0 ,1,2,3,4,5) 
# print(anant[0:5])

# # list sorting
# alist=[8,5,4,6,54,94,51,20,57,63,554,97,8,52,45,5,5,5,5555]
# print(alist[10])

# alist.sort()# this function will (update) the list in ascending order.
# print(alist)
# print(alist[9])

# alist.reverse()# this function will (update) te list in decseding order.
# print(alist)

# alist.append(100)# this function will (update & add) at the last of the list.
# print(alist)

# alist.insert(4,696969)
# print(alist)

# alist.pop()# this function will automatically delete the last number from the list
# alist.pop()# this function will automatically delete the last number from the list
# alist.pop()# this function will automatically delete the last number from the list
# alist.pop()# this function will automatically delete the last number from the list
# alist.pop()# this function will automatically delete the last number from the list
# alist.pop(0)# this function will automatically delete the given index number from the list
# alist.remove(696969)# this function will autmatically delete the (first) given item in the braces.
# print(alist)


# # tuples
# # tuples cann never be changed they can be created only once and can be created by ( )and , also.


# tuple =(7,8,9) # if you use ( )  and , then it will be of the tuples datatypes.
# container=[78,8,9,97] # if you use [ ] braces then it will be the list datatypes.  
# print(type(tuple))
# print(type(container))


# # tuple methods
# a =(1,2,587,65,2,5,2,4,45,5)
# print(type(a))
# print(a.count(2))# this function will count the provided number in the tuple
# print(a.index(2))# this function will count the number place of the given number


# write a program in a list to enter the fruit name entered by the user

# f1 =input("enter fruit 1")
# f2 =input("enter fruit 2")
# f3 =input("enter fruit 3")
# f4 =input("enter fruit 4")
# f5 =input("enter fruit 5")
# f6 =input("enter fruit 6")
# myfruitlist =[f1,f2,f3,f4,f5,f6]
# print(myfruitlist)



# write a program to align the given marks in ascending order.
  
# marks0 =input("enter student marks 1: ")
# marks1 =input("enter student marks 2: ")
# marks2 =input("enter student marks 3: ")
# marks3 =input("enter student marks 4: ")
# marks4 =input("enter student marks 5: ")
# marks5 =input("enter student marks 6: ")
# mysstudentmarkslist =[marks0,marks1,marks2,marks3,marks4,marks5]
# mysstudentmarkslist.sort() #this will arrange the list in ascending order.
# mysstudentmarkslist.reverse() # this will arrange the list in descending order.
# print(mysstudentmarkslist)



# mylist =[1,2,8,5,2,7,7,5,9,6,]
# sum =0
# sum +=mylist[0]
# sum +=mylist[1]
# sum +=mylist[2]
# sum +=mylist[3]
# sum +=mylist[4]
# sum +=mylist[5]
# sum +=mylist[5]
# sum +=mylist[6]
# sum +=mylist[7]
# sum +=mylist[8]
# sum -=mylist[9]
# print("the value of sum is", sum)


ji = (input("enter you name"))
print("good afternoon", ji)




 