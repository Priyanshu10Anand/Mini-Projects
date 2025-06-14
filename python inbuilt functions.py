name=input("Enter your name: ")

print("  Choice 1= To use string functions")
print("  Choice 2= To use list functions")
print("  Choice 3= To use tuple functions")
print("  Choice 4= To use dictionary functions")
while True:
    ch1=int(input("Enter your CHOICE number with which function you want to continue: "))
    
    if(ch1==1):
        print("ENJOY STRING FUNCTIONS")
        a=input("Enter the string: ")
        print("        choice 1=len()")
        print("        choice 2=capitalize()")
        print("        choice 3=count()")
        print("        choice 4=find()")
        print("        choice 5=index()")
        print("        choice 6=isalnum()")
        print("        choice 7=isalpha()")
        print("        choice 8=isdigit()")
        print("        choice 9=islower()")
        print("        choice 10=isupper()")
        print("        choice 11=isspace()")
        print("        choice 12=upper()")
        print("        choice 13=lower()")
        print("        choice 14=lstrip()")
        print("        choice 15=rstrip()")
        print("        choice 16=strip()")
        print("        choice 17=startswith()")
        print("        choice 18=endswith()")
        print("        choice 19=istitle()")
        print("        choice 20=title()")
        print("        choice 21=replace()")
        print("        choice 22=join()")
        print("        choice 23=split()")
        print("        choice 24=partition()")
        print("        choice 25=swapcase()")
        print("        choice 26=concatenation")
        print("        choice 27=repetition")
        ch=int(input("Enter the choice you want to continue: "))
        if (ch==1):
            print(len(a))
        if (ch==2):
            print(a.capitalize())
        if (ch==3):
            b=input("enter the sub-string you want to count the occurance")
            print(a.count(b))
        if (ch==4):
            c=input("enter the sub-string you want to find")
            print(a.find(c))
        if (ch==5):
            d=input("enter the string you want to find the index of")
            print(a.index(d))
        if (ch==6):
            print(a.isalnum())
        if (ch==7):
            print(a.isalpha())
        if (ch==8):
            print(a.isdigit())
        if (ch==9):
            print(a.islower())
        if (ch==10):
            print(a.isupper())
        if (ch==11):
            print(a.isspace())
        if (ch==12):
           print(a.upper())
        if (ch==13):
           print(a.lower())
        if (ch==14):
           print(a.lstrip())
        if (ch==15):
           print(a.rstrip())
        if (ch==16):
           print(a.strip())
        if (ch==17):
           e=input("enter the string you want to check the string starts with")
           print(a.startswith(e))
        if (ch==18):
           f=input("enter the string you want to check the string ends with")
           print(a.endswith(f))
        if (ch==19):
           print(a.istitle())
        if (ch==20):
           print(a.title())
        if (ch==21):
           g=input("enter the string with which you want to replace the old string")
           print(a.replace(a,g))
        if (ch==22):
           h=input("enter the symbol with which you want to join with the string")
           i=int(input("enter the number of terms of symbol you want to join with the string"))
           j=h*i
           print(j.join(a))
        if (ch==23):
           k=input("enter the string with which you want to split the old string")
           print(a.split(k))
        if (ch==24):
           l=input("enter the string with which you want to separate from the old string")
           print(a.partition(l))
        if (ch==25):
           print(a.swapcase())
        if (ch==26):
            m=input("enter the string with which you want concatanation")
            print(a+m)
        if (ch==27):
            n=int(input("enter the number of times you want the repetition of the string"))
            print(a*n)
    
    if(ch1==2):
        print("ENJOY LIST FUNCTIONS")
        a=eval(input("enter the list"))
        print("      choice 1=len()")
        print("      choice 2=list()")
        print("      choice 3=index()")
        print("      choice 4=append()")
        print("      choice 5=extend()")
        print("      choice 6=insert()")
        print("      choice 7=pop()")
        print("      choice 8=clear()")
        print("      choice 9=count()")
        print("      choice 10=reverse()")
        print("      choice 11=sort()")
        print("      choice 12=sorted()")
        print("      choice 13=min()")
        print("      choice 14=max()")
        print("      choice 15=sum()")
        print("      choice 16=remove()")
        print("      choice 17=concatenation")
        print("      choice 18=repetition")
        ch=int(input("enter your CHOICE with which you want to continue"))
        if(ch==1):
            print(len(a))
        if(ch==2):
            b=input("enter something which you want to change to list")
            print(list(b))
        if(ch==3):
            c=input("enter the list you want to find the index of if integer please enter in quotes ")
            print(a.index(c))
        if(ch==4):
            d=input("enter the list you want to add ")
            print(a.append(d))
        if(ch==5):
            e=input("enter the list you want to add ")
            print(a.extend(e))
        if(ch==6):
            f=input("enter the list you want to add \nif integer please enter in quotes")
            g=input("enter the index of list ")
            a.insert(g,f)
            print(a)
        if(ch==7):
            h=int(input("enter the list you want to find the index of if string please enter in []   "))
            j=a.pop(a.index(h))
            print(j)
            print(a)
        if(ch==8):
            print(a.clear())
        if(ch==9):
            k=int(input("enter the item of list of which you want to count the occurance if string enter in[]   "))
            print(a.count(k))
            print(a)
        if(ch==10):
            l=a.reverse()
            print(a)
        if(ch==11):
            a.sort()
            print(a)
        if(ch==12):
            print(sorted(a))
        if(ch==13):
            print(min(a))
        if(ch==14):
            print(max(a))
        if(ch==15):
            print(sum(a))
        if(ch==16):
            l=int(input("enter the value of list to be removed"))
            a.remove(l)
            print(a)
        if (ch==17):
            m=eval(input("enter the list with which you want concatanation  "))
            print(a+m)
        if (ch==18):
            n=int(input("enter the number of times you want the repetition of the list"))
            print(a*n)
    
    if(ch1==3):
        print("ENJOY TUPLE FUNCTIONS")
        a=eval(input("enter the tuple"))
        print("      choice 1=len()")
        print("      choice 2=tuple()")
        print("      choice 3=index()")
        print("      choice 4=count()")
        print("      choice 5=sorted()")
        print("      choice 6=min()")
        print("      choice 7=max()")
        print("      choice 8=sum()")
        print("      choice 9=concatenation")
        print("      choice 10=repetition")
        ch=int(input("enter your CHOICE with which you want to continue"))
        if(ch==1):
            print(len(a))
        if(ch==2):
            b=input("enter which you want to convert into tuple")
            print(tuple(b))
        if(ch==3):
            print("       choice 1= if wanted to know the index of a string value")
            print("       choice 2= if wanted to know the index of a numeric value")
            ch2=int(input("enter your choice for knowing the index"))
            if(ch2==1):
                b1=input("enter the item whose index you want to know")
                print(a.index(b1))
            if(ch2==2):
                b2=input("enter the item whose index you want to know")
                print(a.index(b2))
        if(ch==4):
            d=int(input("enter the item of the tuple you want to count the occurances"))
            print(a.count(d))
        if(ch==5):
            print(sorted(a))
        if(ch==6):
            print(min(a))
        if(ch==7):
            print(max(a))
        if(ch==8):
            print(sum(a))
        if (ch==9):
            e=eval(input("enter the tuple with which you want concatanation"))
            print(a+e)
        if (ch==10):
            f=int(input("enter the number of times you want the repetition of the tuple"))
            print(a*f)
    
    if(ch1==4):
        print("ENJOY DICTIONARY FUNCTIONS")
        a={}
        b=int(input("how many students?"))
        for i in range(b):
            c,d=eval(input("enter ROLL NUMBER and MARKS of students"))
            a[c]=d
        print("dictionary created")
        print(a)
        print("        choice 1=len()")
        print("        choice 2=get()")
        print("        choice 3=items()")
        print("        choice 4=keys()")
        print("        choice 5=values()")
        print("        choice 6=min()")
        print("        choice 7=max()")
        print("        choice 8=sum()")
        print("        choice 9=sorted()")
        print("        choice 10=clear()")
        print("        choice 11=pop()")
        print("        choice 12=popitem()")
        print("        choice 13=copy()")
        print("        choice 14=update()")
        print("        choice 15=setdefault()")
        print("        choice 16=fromkeys()")
        ch=int(input("enter your CHOICE with which you want to continue"))
        if(ch==1):
            print(len(a))
        if(ch==2):
            e=input("enter the key of which you want to get the value")
            a.get(e)
            print(a)
        if(ch==3):
            print(a.items())
        if(ch==4):
            print(a.keys())
        if(ch==5):
            print(a.values())
        if(ch==6):
            print(min(a))
        if(ch==7):
            print(max(a))
        if(ch==8):
            print(sum(a))
        if(ch==9):
            print(sorted(a))
        if(ch==10):
            a.clear()
            print(a)
        if(ch==11):
            f=int(input("enter the index of list "))
            a.pop(f)
            print(a)
        if(ch==12):
            print(a.popitem())
        if(ch==13):
            print(a.copy())
        if(ch==14):
            g={}
            h=int(input("how many students?"))
            for i in range(h):
                j=eval(input("enter ADMISSION NUMBER of students"))
                k=input("enter the name")
                g[j]=k
            print("dictionary created")
            print(g)
            print(a.update(g))
        if(ch==15):
            l=int(input("enter the key if in string please enter it in bracket()   "))
            m=int(input("enter the key if in string please enter it in bracket()   "))
            print(a.setdefault(l,m))
        if(ch==16):
            n=[]
            o=int(input("how many students? "))
            for i in range(o):
                p=eval(input("enter ROLL NUMBER"))
                n.append(p)
            q=eval(input("enter the AMOUNT deposited by the students and AGE"))  
            print(a.fromkeys(n,q))
    dy=input("do you want to continue ? [y/n]: ")
    if dy=="n":
        break
    else:
        pass
print("THANK YOU",name,"powered by PRIYANSHU ANAND ", "under the guidance of MR.RAVI KUMAR SINGH")