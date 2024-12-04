num=int(input("Enter a number to find factorial:"))
fact=1
for i in range(1,num+1):
fact*=i
if num&lt;0:
print("Enter number greater than zero")
else:
print(f"Factorial of {num} is {fact}")
