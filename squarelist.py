import math
start=int(input("Enter the starting range of a four digit number:"))
end=int(input("Enter the ending range of a four digit number:"))
squareevenlist=[]
for i in range(start,end+1):
  if 1000<=i<=9999:
    sqrtno=math.isqrt(i)
    if sqrtno*sqrtno==i:
      isalleven=True
      temp=i
      while temp>0:
        digit=temp%10
        if digit%2!=0:
          isalleven=False
          break
        temp//=10
      if isalleven:
        squareevenlist.append(i)
      else:
        print("Enter four digit no range")
        break
if squareevenlist!=[]:
print(f"Four digit perect square with all even digits:{squareevenlist}")
