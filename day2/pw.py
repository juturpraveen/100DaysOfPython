#!
"""
This is password mananger program, although insecure.
"""
password = { 'email': 'kjuy6t5redfgyuio',
             'blog': 'gty6789iuhbn',
             'safe': 'u789iuyhghj9'
            }

import pyperclip as pp
import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py[account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in password.keys():
    pp.copy(password[account])
else:
    print('There is no account named: ' +account )

# def copyPwd(passwords):
#     print("What account's password you want on clipboard:")
#     account = input()
#     if account in passwords.keys():
#         pp.copy(passwords[account])
#     else:
#         print('That account doest not exist in password manager.')

# copyPwd(password)