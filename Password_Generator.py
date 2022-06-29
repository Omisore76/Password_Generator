# A Program that will generate passwords for a user based on the number of password needed and the length of password required

import random as rand

Username = input("Enter your name: ")
print(f"Hello {Username}, welcome To Your Password Generator!")

Password_Characters = "0123456789ABCDEFGHIJKLMNabcdefghijklmnopq/#$!@"

No_Of_Password_Needed = int(input("How many password(s) would you like to generate? "))

Length_Of_Password = int(input("How long do you want your password to be? "))

print("These are your password(s): ")

for number in range(No_Of_Password_Needed):
    Passwords = " "
    for values in range(Length_Of_Password):
        Passwords = Passwords + rand.choice(Password_Characters)
    print(Passwords)
