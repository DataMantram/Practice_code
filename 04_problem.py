a = int(input("Enter the Number "))
for i in range(2,a):
  if(a%i)==0:
    print(f"{a} Number is not prime.")
    break
else:
    print(f"{a} Number is prime.")

