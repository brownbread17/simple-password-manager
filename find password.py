import pickle
m_pw = input("Enter master password: ")
if(m_pw == "master"):
    website_name = input("Enter website name: ")
    with open("pw.ppwow","rb") as rf:
        passwords = pickle.load(rf)

    if website_name in passwords:
        print("User name = ",passwords[website_name][0])
        print("Password = ",passwords[website_name][1])
    else:
        print("No saved passwprds found")