
#Program to print nth prime-palindrome number
def primepal(n):
    x=2
    count=0
    prime=''
    if n>=1:
        for i in range(1,1000000000000000000000000):
            rev=str(i)[::-1]
            for j in range(2,i):    
                if i%j==0:
                    break
                elif x==(i-1) and i%j!=0:
                    prime=str(i)
                    break
                x+=1
            if prime==rev:
                count+=1
                if count==n:
                    u="The "+str(n)+"th prime pallindrome number is : "+str(prime)
                    break
        return u
                
#__main__
while True:
    print("<--Enter 1 to start/continue-->")
    print("<--Enter 2 to exit------------>")
    ch=int(input("Enter your choice: "))
    if ch==1:
        n=int(input("Enter a number: "))
        print(primepal(n))
    elif ch==2:
        print("Exit successful")
        break
    else:
        print("Invalid Input")
