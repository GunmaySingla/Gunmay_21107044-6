import math
n = 5
#we know that pascals triangle can formed using nCr

#for the triangle to start from 4th position we used the 1st for loop
for i in range(n):
#this for loop is used to create spaces between the letters    
    for j in range(n-i-1):
        print(' ',end='')
#this loop is to print out the desired letters        
    for k in range(i+1):
        print(math.factorial(i)//(math.factorial(i-k)*math.factorial(k)) , end=' ')
    print() 


