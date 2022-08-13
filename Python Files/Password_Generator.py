import random
import bcrypt
import os    # imports the modules

password_path = 'TXT files/encrypted_pass.txt'

if os.stat(password_path).st_size == 0:
    new_pass = input("\nwhat is your new password : ")

    encoded_pass = new_pass.encode('utf-8')

    encrypted_pass = bcrypt.hashpw(bytes(encoded_pass), bcrypt.gensalt())
    
    with open("TXT files/encrypted_pass.txt", "w") as a:
        a.write(encrypted_pass.decode('utf-8'))
        
    print("created password succesfully!")

    exit()

else:
    given_pass = input("\nwhat is your password : ")
    
    given_encoded = given_pass.encode('utf-8')
        
    with open("TXT files/encrypted_pass.txt", "r") as z:
        if(bcrypt.checkpw(bytes(given_encoded), bytes(z.read().encode('utf-8')))):
            print('\nCorrect password\n')
        
        else:
            print('\nIncorrect password\n')
            exit()

everything = list(
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&²()*+,-./:;<=>?@[]^_`{|}~"
)  # list of ASCII letters and numbers and symbols
a = input("do you want to make a new password or show the current ones?[1,2] : ")
if a == "1":
    try:
        user = int(input("how many letters do you want : "))
    except ValueError:
        print("Invalid Input!")
        exit(1)
        
    randomly = random.choices(
        everything, k=user
    )  # chooses the amount of ASCII letters provided by the user randomly from the list

    print(f"\nyour password is : {''.join(randomly)}")

    save = input("\ndo you want to save it? : ")

    if save == "yes":

        name = input("what website or what should we name the file? : ")
        
        with open("TXT files/passwords.txt", "r") as p:  # opens the file to read it
            
            file = p.read()

            with open("TXT files/passwords.txt", "w") as k:  # opens the file to write in it
                if file == "":
                    k.write("".join(randomly) + " - " + name)
                    print("Saved the password Succesfully!")
                    
                else:
                    k.write(file)  # writes the file again to not overwrite it
                    k.write("\n")  # opens a new line
                    k.write(
                        "".join(randomly) + " - " + name
                    )  # writes the new password with the website name
                    print("Saved the password Succesfully!")

    else:
        print("ok")
else:
    with open ("TXT files/passwords.txt", "r") as r:
        print(r.read())
    wait_for_exit = input("")
    if wait_for_exit == "exit":
        exit()
