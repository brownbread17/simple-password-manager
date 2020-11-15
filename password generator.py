import random
import pickle

passwords = {}

with open("pw.ppwow","rb") as rf:
    passwords = pickle.load(rf)

password_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password_len = int(input("Required number of characters: "))

password = "".join(random.sample(password_string, password_len))
print(password)

save = input("Do you want to use the password(y/n): ").lower()
if save == 'y':
    website = input("Enter website name: ")
    user_name = input("Enter username: ")
    passwords[website] = [user_name,password]
    with open("pw.ppwow","wb") as wf:
        pickle.dump(passwords, wf, protocol=2)
 
elif save == 'n':
    print("Not Saved!")
else:
    print("Incorrect Input!")