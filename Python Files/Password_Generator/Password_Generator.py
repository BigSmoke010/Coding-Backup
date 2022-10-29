import random
import bcrypt
from colorama import Fore
import os  # imports the modules

homedir = os.getenv("HOME")  # gets the homedir (only works in linux)
password_path = homedir + "/Coding/Python Files/Password_Generator/TXT files/encrypted_pass.txt"
number_of_inputs = 0
correct = False

if os.stat(password_path).st_size == 0:
    new_pass = input("\nwhat is your new password : ")

    encoded_pass = new_pass.encode("utf-8")

    encrypted_pass = bcrypt.hashpw(bytes(encoded_pass), bcrypt.gensalt())

    with open(password_path, "w") as a:
        a.write(encrypted_pass.decode("utf-8"))

    print("created password succesfully!")

    exit()

else:
    while number_of_inputs < 4 and not correct:
        given_pass = input("\nwhat is your password : ")

        given_encoded = given_pass.encode("utf-8")

        with open(password_path, "r") as z:

            if bcrypt.checkpw(bytes(given_encoded),
                              bytes(z.read().encode("utf-8"))):
                print("\nCorrect password\n")
                correct = True
            else:
                print("\nIncorrect password\n")
                number_of_inputs += 1

    if number_of_inputs == 4:
        reset = input(
            "it seems like you forgot your password, do you want to reset it ? [y/n] :"
        )
        if reset == "y":
            with open(password_path, "w") as create:
                pass
            with open(
                    homedir +
                    "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
                    "w") as crete:
                pass
            exit()
        else:
            print("ok")
            exit()

everything = list(
    "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&²()*+,-./:;<=>?@[]^_`{|}~"
)  # list of ASCII letters and numbers and symbols
a = input(
    f"do you want to make a {Fore.BLUE}new password or {Fore.GREEN}show the current ones or {Fore.RED}remove a password ?[1,2,3] :{Fore.RESET} "
)
if a == "1":
    try:
        user = int(input("how many letters do you want : "))
    except ValueError:
        print(f"{Fore.RED}Invalid Input!")
        exit(1)

    randomly = random.choices(
        everything, k=user
    )  # chooses the amount of ASCII letters provided by the user randomly from the list

    print(f"\nyour password is : {''.join(randomly)}")

    save = input("\ndo you want to save it? : ")

    if save == "yes":

        name = input("what website or what should we name the file? : ")

        with open(
                homedir +
                "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
                "r") as p:  # opens the file to read it

            file = p.read()

            with open(
                    homedir +
                    "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
                    "w") as k:  # opens the file to write in it
                if file == "":
                    k.write("".join(randomly) + " - " + name)
                    print(
                        f"{Fore.GREEN}Saved the password Succesfully!{Fore.RESET}"
                    )

                else:
                    k.write(file)  # writes the file again to not overwrite it
                    k.write("\n")  # opens a new line
                    k.write(
                        "".join(randomly) + " - " +
                        name)  # writes the new password with the website name
                    print("Saved the password Succesfully!")

    else:
        print("ok")

elif a == "2":
    with open(
            homedir +
            "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
            "r") as r:
        print(r.read())
    wait_for_exit = input("")
    if wait_for_exit == "exit":
        exit()
elif a == "3":
    with open(
            homedir +
            "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
            "r") as file_input:
        lines = file_input.read()
        print(lines)
        selected = input(
            "please input the name of the website to be deleted (c to clear all):"
        )
        if selected == "c":
            with open(
                    homedir +
                    "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
                    "w") as cler:
                pass
            print("cleared passwords successfully")
        with open(
                homedir +
                "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
                "r") as input:
            with open(
                    homedir +
                    "/Coding/Python Files/Password_Generator/TXT files/temp.txt",
                    "w") as output:
                # iterate all lines from file
                for line in input:
                    # if substring contain in a line then don't write it
                    if selected not in line.strip("\n"):
                        output.write(line)

        # replace file with original name
        os.replace(
            homedir +
            "/Coding/Python Files/Password_Generator/TXT files/temp.txt",
            homedir +
            "/Coding/Python Files/Password_Generator/TXT files/passwords.txt",
        )

    print("removed password successfully")
