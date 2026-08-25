def bubblesort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-1):
            if(arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
                
arr=[3,5,1,6,8,9,4,3,0,2]
bubblesort(arr)
print(arr)