upper_limit=int(input("enter the upperlimit:"))
for num in range (1,upper_limit+1):
  sum=0
  for digit in str(num):
    sum+=int(digit)
  if sum>1:
    is_prime=True
    for i in range (2,int(sum**0.5)+1):
      if sum % i==0:
        is_prime=False
        break
    if is_prime:
    print("the sum of digit of{num}:{sum},is a prime")
