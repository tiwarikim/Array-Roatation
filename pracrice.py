#we are performing array rotation by shifting each element left by one
arr = [1,2,3,4,5,6,7]
# we are going to shift it d times
d = 2
#using 1st for loop to start the rotation
for i in range(0,d):
    temp = arr[0] #what we did here we created a space in our arr by putting it in temp variable and now we have on empty space at a[0] position
    #we are using this loop to shift elements for example arr[1] to arr[0], arr[2] to arr[1] and so on so we are going towards left
    for j in range(0, len(arr)-1):
        arr[j] = arr[j+1]# eg arr[0] = arr[1]  arr[2] = arr[3]
    arr[len(arr)-1] = temp  #after the shifting of elements we have last position empty put the temp variable there
#this final loop is to print the resulting array

for i in range(0, len(arr)):
    print(arr[i])


#time complexity of this program will be O(n*d)
#auxilary spcae will be O(n)