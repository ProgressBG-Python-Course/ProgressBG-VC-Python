while True:
    user_name = input("Enter your user name (at least 3 symbols): ")
    if len(user_name) >= 3:
        break
    else:
        print("*** At least 3 symbols, please! Try again.\n")

print("Nice, your user_name is: ", user_name)
