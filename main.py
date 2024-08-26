#Bubble sort
arr = [5,4,2,3,1,4,6]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            swap(arr,i,j)

def swap(arr,first,second):
    temp=arr[first]
    arr[first]=arr[second]
    arr[second]=temp

print(arr)