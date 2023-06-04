#fcfs case 1
def FCFS1stCase():
    m = int(input('number of proccess '))
    n = 2
    b=[[]]
    b=b*m

    matrix = [0]*m
    columns = [0]*n
    for i in range (0,m):
        matrix[i] =columns.copy()

    for i in range (0,m):
        for j in range (0,n):
            if(j==0):

                matrix[i][j] = input("enter name of procces ")
            elif(j==1):
                matrix[i][j] = int(input("enter number of Brust time "))

    order=[" "]*m
    for i in range(m):
        order[i]=input("enter order")

    z=0
    g=0
    arr=[0]
    arr=arr*m
    for i in range(m) :
        for t in range(m) :
            if(order[i]==matrix[t][0]):
                b[i]=matrix[t]
    print(b)
    for i in range(m):
        if(i==0):
            print("wait time:",b[i][0],"=",0)
        else:
            z=z+int(b[i-1][1])
            print("wait time:",str(b[i][0]),"=",str(z))
        arr[i]=z
    for i in arr: 
        g=g+i 
    g=g/m
    print("avg of waiting time=",g)




#FCFS CASE(2)
def FCFS2stCase():
    m = int(input('number of proccess '))
    n = 3
    matrix = [0]*m
    columns = [0]*n
    for i in range (0,m):
        matrix[i] =columns.copy()

    for i in range (0,m):
        for j in range (0,n):
            if(j==0):

                matrix[i][j] = input("enter name of procces ")
            elif(j==1):
                matrix[i][j] = int(input("enter number of Brust time "))
            else:
                matrix[i][j] = int(input("enter number of arrive time "))
    b=sorted(matrix, key=lambda e: e[2])
    print(b)
    g=0
    z=0
    arr=[0]
    arr=arr*m
    for i in range(m):
        if(i==0):
            print("wait time:",b[i][0],"=",0)
        else:
            z=z+b[i-1][1]

            print("wait time:",b[i][0],"=",z-b[i][2])
        arr[i]=z-b[i][2]
    for i in arr: 
        g=g+i 

    g=g/m
    print("avg of waiting time=",g)




#PRIORITY SCHEDULED NOT PRIMITIVE
def PrioritySheduledNotPrimitive():
    m = int(input('number of proccess '))
    n = 3
    matrix = [0]*m
    columns = [0]*n

    for i in range (0,m):
        matrix[i] =columns.copy()

    for i in range (0,m):
        for j in range (0,n):
            if(j==0):

                matrix[i][j] = input("enter name of procces ")
            elif(j==1):
                matrix[i][j] = int(input("enter number of Brust time "))
            else:
                matrix[i][j] = int(input("enter number of Priority "))
    b=sorted(matrix, key=lambda e: e[2])
    print(b)
    g=0
    z=0
    arr=[0]
    arr=arr*m
    for i in range(m):
        if(i==0):
            print("wait time:",b[i][0],"=",0)
        else:
            z=z+b[i-1][1]
            print("wait time:",b[i][0],"=",z)
        arr[i]=z
    for i in arr: 
        g=g+i 
    g=g/m

    print("avg of waiting time=",g)



#RR
def RR():
    m = int(input('number of proccess '))
    n = 3
    qun=int(input('number of quntum time '))

    matrix = [0]*m
    columns = [0]*n

    for i in range (0,m):
        matrix[i] =columns.copy()

    for i in range (0,m):
        for j in range (0,n):
            if(j==0):

                matrix[i][j] = input("enter name of procces ")
            elif(j==1):
                matrix[i][j] = int(input("enter number of Brust time "))
    ta=0
    arra=[0]*m
    c=0

    for i in range (0,m):
        c=c+matrix[i][1]
    i=0
    while(c!=ta):
        if(i==m):
            i=0
        else:
            if(matrix[i][1]!=0):

                if(matrix[i][1]-qun>0):

                    arra[i]=arra[i]+(ta-matrix[i][2])

                    matrix[i][1]=matrix[i][1]-qun
                    ta+=qun
                    matrix[i][2]=ta
                    i+=1
                    continue
                else:
                    arra[i]=arra[i]+(ta-matrix[i][2])
                    ta+=matrix[i][1]
                    matrix[i][1]=0
                i+=1
                continue
            else:
                i+=1
                continue
    g=0
    for i in range (0,m):
        print("wating time ",matrix[i][0],"=",arra[i])
        g=g+arra[i]
    
    g=g/m

    print("avg of waiting time=",g)


#SJF NON PRIMITIVE
def SJFnonprimitive():
    m = int(input('number of proccess '))
    n = 3
    matrix = [0]*m
    columns = [0]*n

    for i in range (0,m):
        matrix[i] =columns.copy()

    for i in range (0,m):
        for j in range (0,n):
            if(j==0):
                matrix[i][j] = input("enter name of procces ")
            elif(j==1):
                matrix[i][j] = int(input("enter number of Brust time "))
            else:
                matrix[i][j] = int(input("enter number of arrival time  "))
    
    ar=sorted(matrix, key=lambda e: e[2])
    b=sorted(matrix, key=lambda e: e[1])
    ta=0
    arra=[0]*m

    for i in range (0,m):
        if(i==0):
            arra[i]=ta-ar[i][2]
            ta=ta+ar[i][1]
            ar[i][1]=0
            ar[i][2]=1000000000
        else:
            for j in range (0,m):
                if(b[j][2]<=ta):
                    for k in range (0,m):
                        if(b[j]==ar[k]):
                            arra[k]=ta-ar[k][2]
                            ta=ta+ar[k][1]
                            ar[k][1]=0
                            ar[k][2]=1000000000
                elif(ar[i][2]<=ta):
                    arra[i]=ta-ar[i][2]
                    ta=ta+ar[i][1]
                    ar[i][1]=0
                    ar[i][2]=1000000000
    
    g=0
    for i in range (0,m):
        print("wating time ",ar[i][0],"=",arra[i])
        g=g+arra[i]
    g=g/m
    print("avg of waiting time=",g)


#SJF NON PRIMITIVE
def SJFprimitive():
    n = int(input('Enter no of processes: '))
    bt = [0] * (n + 1)
    at = [0] * (n + 1)
    abt = [0] * (n + 1)
    for i in range(n):
        abt[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
        at[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
        bt[i] = [abt[i], at[i], i]

    bt.pop(-1)
    i = 0
    ll = []
    for i in range(0, sum(abt)):
        l = [j for j in bt  if j[1] <= i]
        l.sort(key=lambda x: x[0])

        bt[bt.index(l[0])][0] -= 1
        for k in bt:
            if k[0] == 0:
                t = bt.pop(bt.index(k))
                ll.append([k, i + 1])

    ct = [0] * (n + 1)
    tat = [0] * (n + 1)
    wt = [0] * (n + 1)
    for i in ll:
        ct[i[0][2]] = i[1] 
    for i in range(len(ct)):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - abt[i]
    ct.pop(-1)
    wt.pop(-1)
    tat.pop(-1)
    abt.pop(-1)
    at.pop(-1)
    print('Average Waiting Time = ', sum(wt)/len(wt))
    print('Average Turnaround Time = ', sum(tat)/len(tat))





print("Enter 1 if you want FCFS \nEnter 2 if you want PRIORITY SCHEDULED NOT PRIMITIVE \nEnter 3 if you want RR \nEnter 4 if you want SJF NON PRIMITIVE \nEnter 5 if you want SJF PRIMITIVE \nWhat do you want: ")
ziad=int(input())
if ziad==1:
    print("Enter 1 if you want FCFS 1st Case \nEnter 2 if you want FCFS 2st Case \nWhat do you want: ")
    x=int(input())
    if x==1:
        FCFS1stCase()
    elif x==2:
        FCFS2stCase()
    else:
        print("input is not valid")
elif ziad==2:
    PrioritySheduledNotPrimitive()
elif ziad==3:
    RR()
elif ziad==4:    
    SJFnonprimitive()
elif ziad==5:    
    SJFprimitive()
else:
    print("input is not valid")