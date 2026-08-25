#T.C=O(logN); S.C=O(N)...T(N)=2T(N/2)+1
def power(x,n):
    if(n==0):
        return 1
    TEMP=power(x,n//2)
    if(n%2==0):
        return(TEMP*TEMP)
    else:
        return(TEMP*TEMP*x)

x,n=2,7
print(power(x,n))