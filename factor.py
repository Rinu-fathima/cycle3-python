number=int(input("Enter a number to find its factors:"))
i=1
factor=[]
while i &lt;= number:
  if number % i == 0:
    factor.append(i)
  i += 1
print(f"The factors of {number} are:{factor}")
