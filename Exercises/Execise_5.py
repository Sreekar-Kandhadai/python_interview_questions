Write a program that will take three digits from the user and add the square of each digit.

Solution:

num=222
sum=0

for digit in str(num):
    
    sum+=(int(digit))**2
    
print(sum)
