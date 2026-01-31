value=input("enter  list of number:")
# list1=(value.split()) #list banisakcha kinaki split le values lai space ko basis ma split garera list maa rakhcha 
# tara list bhitra ko value ajhai string nai huncha
myList=list(map(int,value.split()))
# print(type(list1[0]))

print(f"The unsorted list is:\n{myList}")

#----------BUBBLE SORT-----------
def bubbleSort(myList,n):
    for i in range(n):
        for j in range(n-i-1):
            if myList[j]>myList[j+1]:
                temp=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp
    return myList

print(f"The sorted list is:\n{bubbleSort(myList,len(myList))}")

#-----------INSERTION SORT-------------
def insertionSort(myList,n):
    for i in range(1,n):
        minkey=myList[i]
        j=i-1
        while(j>=0 and myList[j]>minkey):
            myList[j]=myList[j+1]
            j-=1
        myList[j+1]=minkey
    return myList

print(f"The sorted list is:\n{insertionSort(myList,len(myList))}")

#--------------SELECTION SORT---------
def selectionSort(myList,n):
    for i in range(n-1):
        minkey=myList[i]
        p=i
        for j in range(i+1, n):
            if(myList[j]<minkey):
                minkey=myList[j]
                p=j
        temp=myList[p]
        myList[p]=myList[i]
        myList[i]=temp
    return myList

print(f"The sorted list is:\n{selectionSort(myList,len(myList))}")