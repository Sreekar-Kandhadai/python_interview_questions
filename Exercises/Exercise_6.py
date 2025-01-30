Write a program that will check whether the number is armstrong number or not.

Solution:

num=3711

sum=0

length=len(str(num))

for digit in str(num):
    
    sum+=(int(digit))**length
    
if num==sum:
    print(num ,"is armstrong number")
    
else:
    print(num ,"is not armstrong number")
