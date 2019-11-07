while True:
    print('Please enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for the age')

while True:
    print('Please select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print("Password can only have letters and numbers only")
