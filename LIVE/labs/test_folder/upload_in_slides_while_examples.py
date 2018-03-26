while True:
  user_name = input("Enter a name (at least 3 symbols): ")
  user_name_length = len(user_name)

  if user_name_length >=3:
    break



print("Thank you, {}!".format(user_name))