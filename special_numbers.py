print("----SPECIAL NUMBERS----\n"
"1)  Buzz Number: The number is divisible by 7 or ends with 7. eg: 63 or 67\n"
"2)  Armstrong Number: For three digit number, the sum of cube of digits is equal to the number. eg: 153\n"
"3)  Perfect Number: Sum of factors (excluding the number itself) of number is equal to the number. eg: 6\n"
"4)  Spy Number: Product of digits is equal to the sum of the digits. eg: 6\n"
"5)  Niven Number: Number is divisible by the sum of digits. eg: 36\n"
"6)  Lead Number: Even digit sum is equal to the odd digit sum. eg: 2343 or 2451\n"
"7)  Duck Number: The number ends with 0 or has 0 in the middle. eg: 101 or 1000\n"
"8)  Tech Number: Number of digits should be even, then the square of the sum of left half and right half of the number equals the number. eg: 81\n"
"9)  Prime Number: Number whose only factors are 1 and the number itself. eg: 3 or 5\n"
"10) Palindrome: The number is same if the order of digit is reversed. eg: 12321 or 14141\n")


ans="y"
# variable set for loop to work.
while ans=="y":
    a=int(input("Enter the number you would like to check: "))
    const=a
    b=c=d=e=0
    # variables which we will need later.

    
    # BUZZ CHECKING
    if (a%7==0 or a%10==7):
        print("Buzz Number: Positive")
    else:
        print("Buzz Number: Negative")


    # ARMSTRONG CHECKING
    b=a
    while(a>0):
        c=a%10
        d=c*c*c
        e=e+d
        a=a//10
    if(b==e):
        print("Armstrong Number: Positive")
    else:
        print("Armstrong Number: Negative")
    a=const
    b=c=d=e=0
    # all the variables are set to their original values so that they can be reused.


    # PERFECT CHECKING
    for i in range(1,a):
        if a%i==0:
            b=b+i
    if a==b:
        print("Perfect Number: Positive")
    else:
        print("Perfect Number: Negative")
    a=const
    b=c=d=e=0


    # SPY CHECKING
    c=1
    for i in str(a):
        b=b+int(i)
        c=c*int(i)
    if b==c:
        print("Spy Number: Positive")
    else:
        print("Spy Number: Negative")
    a=const
    b=c=d=e=0


    # NIVEN CHECKING
    b=str(a)
    for i in b:
        c=c+int(i)
    if(a%c==0):
        print("Niven Number: Positive")
    else:
        print("Niven Number: Negative")
    a=const
    b=c=d=e=0


    # LEAD CHECKING
    for i in (str(a)):
        if int(i)%2==0:
            b=b+int(i)
        else:
            c=c+int(i)
    if b==c:
        print("Lead Number: Positive")
    else:
        print("Niven Number: Negative")
    a=const
    b=c=d=e=0


    # DUCK CHECKING
    a=str(a)
    x=a[0]
    x=int(x)
    b=int(a)
    while(b>0):
        if(b%10==0):
            c=c+1
        b=b//10
    if(c>0 and x!=0):
        print("Duck Number: Positive")
    else:
        print("Duck Number: Negative")
    a=const
    b=c=d=e=0


    # TECH CHECKING
    z=a
    b=str(a)
    c=len(b)
    if(c%2==0):
        m=a%(10**(c//2))
        n=a//(10**(c//2))
        if((m+n)*(m+n)==z):
            print("Tech Number: Positive")
        else:
            print("Tech Number: Negative")
    else:
        print("Tech Number: Negative")
    a=const
    b=c=d=e=0


    # PRIME CHECKING
    for i in range(1,a+1):
        if a%i==0:
            b=b+1
    if b==2:
        print("Prime Number: Positive")
    else:
        print("Prime Number: Negative")
    a=const
    b=c=d=e=0


    # PALINDROME CHECKING
    b=str(a)
    if b==b[::-1]:
        print("Palindrome: Positive")
    else:
        print("Palindrome: Negative")
    a=const
    b=c=d=e=0


    ans=input("Would you like to continue (y/n): ")
    # enquiry for loop continuation.

print("Thank you, made by PRIYANSHU ANAND, 12A (24-25) under the guidance of RAVI SIR.")
