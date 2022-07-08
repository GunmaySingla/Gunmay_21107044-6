def palindrome(string):
    
    rev_string=string[::-1]
# we know that ::-1 is the expression to reverse a string
    
    if string==rev_string:
        print("entered string is a palindrome")
    else:
        print("entered string is not a palindrome")

user_string=str(input("enter value that has to be checked: "))
palindrome(user_string)