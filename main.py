######   EMAIL/DOMAIN CHECK AND UPDATE   ######
# Project 1, version 1
# Ideas and TO DO:
# Import data from a spreadsheet.
# User input with GUI?
# Change checks with string.format() and {}

new_email = input("Please enter a new email to add: ")


def email_change(email):
    old_domain = "helloworld.net"
    new_domain = "hello_world.com"

    if "@" not in email:  # Checks if the email is missing the "@" char, and prints an invalid message.
        print("[INVALID ADDRESS]  " + email)

    elif old_domain in email:  # Checks if the email contains the old_domain.
        print("[UPDATE NEEDED!]  " + email)
        print("New address: " + str(email[:(email.index(
            "@"))]) + "@" + new_domain + "\n" + "Updated!")  # prints up to "@" and adds new_domain to the end:

    elif new_domain in email:  # Checks if the email contains the specified new_domain.
        print("[NO CHANGE]  " + email)

    else:  # If email contains neither old_domain or new_domain, it changes the email to match new_domain.
        print("[DOMAIN DOESN'T MATCH]:  " + email)  # TO-DO: Add interface to ask if user wants to change to new domain.
        print("New address: " + str(email[:(email.index("@"))]) + "@" + new_domain)
        update_email = input("Would you like to update your domain? Y/N: ")
        input(update_email)
        if update_email == str("Y"):
            print("We can do that.")
        elif update_email == str("N"):
            print("We can keep the original.")
    return ("")


# Print updated list of changed emails.
# Compare old emails on left, to new on right, using format.()


print(email_change("1.jody@helloworld.net"))
print(email_change("2.ron@helloworld.net"))
print(email_change("3.paul@helloworld.net"))
print(email_change("jessica@helloworld.net"))
print(email_change("5.p.halpert1@helloglobe.net"))
print(email_change("6.test@helloworld.net"))
print(email_change("7.administrator@helloworld.net"))
print(email_change("administrator.exception@hello_world.com"))
print(email_change("missing_character#helloworld.net"))
# New user input:
print(email_change(new_email))