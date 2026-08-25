def linearsearch(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return i
        return -1
    
    arr=[3,2,5,78,5,2,5,7,2,1,8]
    key=100
    result=linearsearch(arr,key)
    if(result==1):
        print("element not found")
    else:
        print("element found at:",result)