#Bubble sort
#To test workflow

def swap(arr,first,second):
    temp=arr[first]
    arr[first]=arr[second]
    arr[second]=temp

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                swap(arr,i,j)
    return arr