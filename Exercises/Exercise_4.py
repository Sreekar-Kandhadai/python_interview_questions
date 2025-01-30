Write a program that will reverse a four digit number.

Solution:

num=1732864

res=""

length=len(str(num))
    
for i in range(length):
        
    num1=num%10
    res+=str(num1)
    num=num//10
        
print(int(res))
