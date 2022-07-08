def perfect_number(n):
    sum = 0
#to find sum of positive divisors we divide the number input by the user by every number and add the numbers which give remainder zero
#and if the number gives 0 we add that number to the sum
#and if the sum of all the divisible numbers equals the number input by user it is a perfect number    
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(int(input('Enter number to check:'))))
