#age=input("How old are you? ") #Ask for a user's age and comment on it using an if else conditional statement.
#age=int(age)

#if age>21:
#   print("Wow, you're old!")
#else:
#    print("You are actually young!")

name=input('what is your name?\n')
length = len(name)
print('Your name is {} letters long.'.format(length))
if len(name)<5:
    print("Short and sweet. I love it!\n")
elif len(name)>=5 and len(name)<10:
    print("Something out of a fairlytale, aye?\n")
else:
    print("write me a story. LOL!\n")