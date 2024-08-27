##  Python script to check the password strength
 
import re   # Importing re, regex to use it to match with password.

def check_password_strength(password):
        # Checks if lenth of password is less than 8 chars.
        if len(password)<=8:
            print("the password strenth is low, less than 8 characters")
        else:
            # Checks pattern to have atleast 1 upper & lower case, 1 digit and 1 special characters in password using regex pattern.
            if re.match(r'((?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).+$)', password):
                if (8<=len(password)<=10):
                    print("Strenth of the password is medium only!")
                    return True
                elif len(password)>10:
                    print("Password looks strong")
                    return True
                else:
                    print("password doesn't meets the criteria...try again")
            else:
                print('''Password criteria doesn't meet...
                    Criteria
                    The password should be at least 8 characters.
                    Contains both uppercase and lowercase letters.
                    Contains at least one digit (0-9).
                    Contains at least one special character (e.g., !, @, #, $, %)
                    ''')

# Takes user input for password, from line 22 script kicks in..

if __name__ == "__main__":
    print("\nPlease refrain from using name/DateOfBirth and family name in your password: \n")
    usr_psswd = input("Enter your password :")
    if check_password_strength(usr_psswd):
        print("password meets the criteria...its'a success")
