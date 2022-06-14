def prime(num):
    num = int(num)
    count =0
    for i in range(2,num):
        if(num%i==0):
            count+=1
    if(count==0):print("prime")
    else:print("not prime")        
    
number = input("Enter number to check")
prime(number)

