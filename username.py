#simple string processing program to generate usernames.

def main():
    print("This program generates computer usernames.\n")

    #gets the users first and last name
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with the 7 chars of the last name
    uname = first[0] + last[:7]

    #output the username
    print("Your username is: ", uname)

main()
