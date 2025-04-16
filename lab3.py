#program to find the numbers multiple of 5 and 7 between 1500 and 2700 inclusive

for i in range (1499,2701):
    if i%5==0:
        print(i,"is a multiple of 5")
    elif i%7==0:
        print(i,"is a multiple of 7")    
    else:
        pass






#program to convert celsius into farenheit and farenheit into celsius

temp=float(input("Enter a temperature value in farenheit:"))

temp=((temp-32)/9)*5

print(temp)

temp=float(input("Enter a temperature value in celsius:"))

temp=temp/5*9+32

print(temp)








#wap to guess a number between 1 to 9

num=int(input("enter a number between 1 to 9:"))

if(num>=1 and num<=9):
    print("Well guessed!")
else:
    while  not( num>=1 and num<=9):
        num=int(input("enter a number between 1 to 9:"))
    else:
        print("Well guessed!")    






#wap to print the following pattern using nested for loop
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

k=0
for i in range(9):
    if(i<=4):
        for j in range(i+1):
            print("*" ,end="")
        print("")
    else:    
        for j in range(i+1-(k+2)):
            print("*",end="")
        print("") 
        k=k+2







#write a program that takes a word from user and reverse it

word=input("Enter a word:")

word=word[::-1]
print(word)






#write a program to tell no of odd and even numbers in the given series

num=(1,2,3,4,5,6,7,8,9)      
c1,c2=0,0
for item in num:
      if(item%2==0):
            c1+=1
      else:
            c2+=1
print("number of even digits is ",c1 ,"number of odd digits is ",c2)







#print each item and its type in list

data=[1,2.3,1+2j,True,'w3resource',(0,-1),[5,12],{"class":"Six"}]

for i in range(len(data)):
      print(data[i]," of datatype ",type(data[i]))







#write a program that prints all numbers from 0 to 6 except 3 and 6

for i in range(7):
    if(i==3 or i==6):
        continue
    else:
        print(i,end=" ")







#write a program to print fibonacci series between 0 to 50 
# 0 1 1 2 3 5 8 13 21 ...

n1=0
n2=1

print(n1,n2,end=" ")

while (n1+n2<=50):
    temp=n2
    n2=n1+n2
    n1=temp
    print(n2,end=" ") 








# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output : fizzbuzz

# 1
# 2
# fizz
# 4
# buzz and so on upto 50


for i in range (51):
    if(i==0):
        continue
    elif(i%3==0 and i%5!=0):
        print("fizz")
    elif (i%5==0 and i%3!=0):
        print("Buzz") 
    elif (i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)









#Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note:
# i = 0,1.., m-1
# j = 0,1.., n-1

# Test Data: Rows = 3, Columns = 4
# Expected Result: [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]



m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns:"))

nested_list = [[0] * n for _ in range(m)]  

for i in range(m):
    for j in range(n):
        nested_list[i][j]=i*j

print(nested_list)










#Write a Python program that accepts a sequence of lines as input, where a blank line indicates the end of input. The program should then print the lines as output, converting all characters to lowercase.

str1=""
str2=input("Enter a line:")
while (str2!=""):
    str1=str1+str2
    str2=input("Enter a line:")

print(str1.lower())    






#Write a Python program which accepts a sequence of comma separated 4 digit 
#binary numbers as its input and print the numbers that are divisible by 5 in a 
#comma separated sequence.

#Sample Data : 0100,0011,1010,1001,1100,1001  
#Expected Output : 1010

binary_numbers = input("Enter comma-separated 4 digit binary numbers: ").split(",")

divisible_by_5=[]

for binary in binary_numbers:
    decimal=int(binary,2)
    if (decimal % 5 == 0):
        divisible_by_5.append(binary)
    else:
        pass

print(",".join(divisible_by_5))        







# Write a Python program that accepts a string and calculate the number of digits and letters.
#Sample Data : Python 3.2 
#Expected Output :  
#Letters 6  
#Digits 2


#  Take user input
text = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

#Loop through each character in the string
for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

# Step 4: Print the results
print("Letters:", letters)
print("Digits:",digits)





# Password Validation
"""
Password Rules:

1. At least one uppercase letter (A-Z).
2. At least one lowercase letter (a-z).
3. At least one digit (0-9).
4. At least one special character ($#@).
5. Length must be between 6 and 16 characters.
"""




pswd=input("Enter your password:")

if len(pswd) < 6 :
    print("minimum length is 6")



if(len(pswd) > 16) :
   print("maximum length is 16")



for char in pswd:
    if char.isdigit()==True:
        break
else:
    print("at least one digit is required")    




for char in pswd:
    if char.isalpha()==True:
        if char.isupper()==True:
            break
else:
    print("at least one uppercase letter is required")    

   


for char in pswd:
    if char.isalpha()==True:
        if char.islower()==True:
            break
else:
    print("at least one lowercase letter is required")    

      


for char in pswd:
    if char=='$' or char=='#' or char =='@':
        break
else:
    print("at least one  special character (  $  or  #   or   @) is required")