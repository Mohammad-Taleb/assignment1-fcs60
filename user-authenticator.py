user_name = input("Enter your username: ").lower()
user_password = int(input("Enter your password: "))

if user_name == 'admin' and user_password == 1234:
  print("Access granted")
else:
  print("Access denied")