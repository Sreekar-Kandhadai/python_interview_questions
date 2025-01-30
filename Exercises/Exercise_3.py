Write a program that will give you the sum of 3 digits

Solution:

num=123

sum=0

for digit in str(num):
    
    sum+=int(digit)
    
print(sum)
