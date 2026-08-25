def selectionsort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i,n):
            if(arr[j]<arr[min_index]):  
                min_index=j          
        arr[i],arr[min_index]=arr[min_index],arr[i] 
             
arr=[3,5,1,6,8,9,4,3,0,2]
selectionsort(arr)
print(arr)