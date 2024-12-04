num=int(input("Enter a number of terms:"))
a,b=0,1
if(num&lt;=0):
print("Enter a positive number")
else:
print("Fibanocci series:")
for i in range(1,num+1):
print(a)
c=a+b
a,b=b,c
