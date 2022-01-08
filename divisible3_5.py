# find all numbers divisible by 3 and 5 smaller than the give number
n=int(input("enter a number: "))
for i in range(1,n):
    if ((i%3==0) & (i%5==0)):
        print("number is divisible by 3 and 5: ",i)

