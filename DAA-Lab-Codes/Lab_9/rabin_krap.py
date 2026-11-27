string="python"
pattern="th"
#length
X=len(string)
Y=len(pattern)
d=256

#Hashcode of pattern
sumP=0
for i in range(Y):
    sumP+=ord(pattern[i])*(d**(Y-i-1))
    
sumS=0
for i in range(Y):
    sumS+=ord(string[i])*(d**(Y-i-1))
    
if(sumS==sumP):
    print("Pattern found at index 0")
for i in range(Y,X):
    sumS=((sumS-(ord(string[i-Y])*(d**(Y-1))))*d)+ord(string[i])
    if(sumS==sumP):
     print("Pattern found at index",i-Y+1)