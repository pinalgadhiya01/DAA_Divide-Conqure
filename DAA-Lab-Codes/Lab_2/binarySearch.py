def binarysearch(arr,low,high,key):
     if(low > high): 
         return -1
     mid=(low+high)//2
     if(arr[mid]==key):
         return mid
     elif(key>arr[mid]):
         return binarysearch(arr,low,mid-1,key)
     else:
         return binarysearch(arr,low,mid-1,key)
           
    
arr=[1,3,5,7,9,11,12,15,18]
key=17
result=binarysearch(arr,0,len(arr)-1,key)
if(result==-1):
    print("element not found")
else:
    print("Element found at:",result)







