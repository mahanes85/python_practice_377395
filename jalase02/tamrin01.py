num = int(input("enter a number :"))

if num > 0:
    for i in range(-num,num+1,1):
        print(i)
elif num < 0:
    for i in range(-num,num-1,-1):
       print(i)
else:
    print(0)