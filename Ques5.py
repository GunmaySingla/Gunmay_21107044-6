input_string=str(input("enter a hyphen separated sentence: "))
#here we use lists to organise the terms
li=list(input_string.split("-"))
#sort functions arranges the list into alphabetical order
li.sort()

print("-".join(li))