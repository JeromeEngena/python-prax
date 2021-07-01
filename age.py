age = input('How old are you?\n')
age = int(age)
if age >12 and age <20:
    print("Teenager")
elif age >=20:
    print("Adult")
else: 
    print("Infant")