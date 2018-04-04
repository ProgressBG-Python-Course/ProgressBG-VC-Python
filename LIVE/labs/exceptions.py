# define custom exception
class UserNameError(Exception):
  pass

# do the potential dangerous stuff in try:
try:
  user_name = input("Enter your name: ")
  if len(user_name)<3:
    raise UserNameError
except UserNameError:
  print("User name must be at least 3 symbols long")
except:
    print('Oops! Something went wrong!')