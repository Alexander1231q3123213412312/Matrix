def add(n,a,g):
    
    for i in range(n):
        b=[]
        for j in range(n):
            b.append(int(input("Enter the number: ")))
        a.append(b)

    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()

    for i in range(n):
        gg=[]
        for j in range(n):
            gg.append(0)
        g.append(gg)

    for i in range(n):
        for j in range(n):
            g[i][j]=a[i][j]

def positive_elements(n,a):
    t=0
    for j in range(n):
        for i in range(n):
            if(a[i][j]<0):
                t+=1
        if(t==n):
            return j
    return -1

def max_elements(n,a,c=[]):
    
    d=a[0][0]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(a[i][j]>d):
                    t_1,t_2=i,j
                    d=a[i][j]
            
        c.append(d)
        a[t_1][t_2]=0
        d=a[0][0]
    return list(c)

def modified_matrix(n,g,c):
    for i in range(n):
        g[i][i]=c[i]
    return list(g)

def final_matrix(n,g,c):
    print("modified matrix: ")
    for i in range(n):
        for j in range(n):
            print(g[i][j],end=' ')
        print()

