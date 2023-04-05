#day 2 assignment
#1
M=int(input("enter M="))
N=int(input("enter N="))

for num in range(M,N+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)
