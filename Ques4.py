def panagrams(sentence):
    alph = 'abcdefghijklmnopqrstuvwxy'
#we define our space where we want to check the letter

    for charac in alph:
        if charac not in sentence:
            return False
      
    return True
user_str = str(input('Enter sentence to be checked: '))
if user_str==False:
    print('The given sentence is a panagram')
else:
    print('The given sentence is not a panagram')
            