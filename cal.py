#Practice Program By 20031A0550

print(" 1) 1-1 \n 2) 1-2 \n 3) 2-1 \n 4) 2-2 ")
Sem=int(input("Select YourSemister"))

print("Score the grades as below \n A+ as 10 \n A  as 9 \n B  as 8 \n C  as 7\n D  as 6 \n E  as 5\n F  as 0")
print('Enter your score')

if Sem==1:
    A=int(input("Communicative English"))
    B=int(input("M-1"))
    C=int(input("Applied Physics"))
    D=int(input("PPSUC"))
    E=int(input("Computer Engineering Workshop"))

    P=int(input("English Lab"))
    Q=int(input("Physics Lab"))
    R=int(input("PPSUC Lab"))

    Raw=(3*(A+B+C+D+E)+1.5*(P+Q+R))
    Sem1=(Raw/19.5)
    print("Final Grade =",Sem1)

if Sem==2:
    A=int(input("M-2"))
    B=int(input("Chemistry"))
    C=int(input("CO"))
    D=int(input("Python"))
    E=int(input("DS"))

    P=int(input("Chemistry Lab"))
    Q=int(input("Python Lab"))
    R=int(input("DS Lab"))
    

    Raw=(3*(A+B+C+D+E)+1.5*(P+Q+R))
    Raw1=(Raw/19.5)
    print("Final Grade =",Raw1)

if Sem==3:
    A=int(input("M3"))
    B=int(input("OPP's through C++"))
    C=int(input("OS"))
    D=int(input("SE"))
    E=int(input("MFCS"))

    P=int(input("OPP's through C++ Lab"))
    Q=int(input("OS Lab"))
    R=int(input("SE Lab"))
    S=int(input("Numpy lab "))

    Raw=(3*(A+B+C+D+E)+1.5*(P+Q+R)+2*(s))
    Raw1=(Raw/21.5)
    print("Final Grade =",Raw1)
    


if Sem==4:
    A=int(input("P & S"))
    B=int(input("DBMS"))
    C=int(input("FLAT"))
    D=int(input("Java"))
    E=int(input("MEFA"))

    P=int(input("DBMS Lab"))
    Q=int(input("Java Lab"))
    R=int(input("R Lab"))
    S=int(input("Pandas lab "))

    Raw=(3*(A+B+C+D+E)+P+2*(R+S)+1.5*(Q))
    Raw1=(Raw/21.5)
    print("Final Grade =",Raw1)

else :
    print("Enter the correct Semister(Enter B/W 1-4")


