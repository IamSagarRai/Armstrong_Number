while True:
    num = int(input("Enter a number:"))
    temp=num
    a=num
    r=0
    c=0
    while a>0:
        c=c+1
        a=a//10
    
    while(temp>0):
        s=temp%10
        r=r+s**c
        temp//=10

    if(r==num):
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")
