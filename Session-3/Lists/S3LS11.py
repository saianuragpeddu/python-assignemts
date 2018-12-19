def MatrixProduct(m1, m2): 
    s=0     #sum
    t=[]    #temporary
    m3=[]   #final matrix
    if len(m2)!=len(m1[0]):
        print("Matrices cannot be multiplicated")        
    else:
        r1=len(m1)      #number of rows in the first matrix
        c1=len(m1[0])   #number of columns in the first matrix   
        r2=c1           #number of rows in the second matrix
        c2=len(m2[0])   #number of columns in the second matrix
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]           
    return m3



