def naturalspline(x,y):
    import numpy as np
    N=np.size(x)-2
    
    b=np.zeros(N)
    Mat=np.zeros((N,N))
    for i in range(N):
        Mat[i,i]=(x[i+2]-x[i])/0.5
        b[i]=((y[i+2]-y[i+1])/(x[i+2]-x[i+1])-(y[i+1]-y[i])/(x[i+1]-x[i]))*6
        
    for i in range(N-1):
        Mat[i,i+1]=(x[i+1]-x[i])
        #Mat[i+1,i]=(x[i+1]-x[i])
    
    for i in range(1,N):
        Mat[i,i-1]=(x[i]-x[i-1])
    
    M=np.zeros(N+2)
    M[1:N+1]=np.linalg.solve(Mat,b)
    
    ans=np.zeros((3,N+2))
    ans[0]=x
    ans[1]=y
    ans[2]=M
    
    return ans

def splineinterp(x,M):
    import numpy as np
    
    xx=M[0]
    yy=M[1]
    mm=M[2]
    
    N=np.size(x)
    y=np.zeros(N)
    
    for i in range(N):
        j=1
        while(xx[j]<x[i]):
            j+=1
        y[i]=(((xx[j]-x[i])**3*mm[j-1])-mm[j]*(xx[j-1]-x[i])**3)/(6*(xx[j]-xx[j-1]))+((xx[j]-x[i])*yy[j-1]-(xx[j-1]-x[i])*yy[j])/(xx[j]-xx[j-1])-(1/6)*(xx[j]-xx[j-1])*(mm[j-1]*(xx[j]-x[i])-mm[j]*(xx[j-1]-x[i]))
        
    
    return y

        