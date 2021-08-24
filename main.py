import re

# The first option
def verify_number(number):
    print(bool(re.search(r'^([\+][7]\s[\(]\d{3,3}[\)]\s\d{3,3}\s\d{2,2}[-]\d{2,2})$', number)))


verify_number("+7 (111) 111 11-11")

# The second option
# def verify_number(number):
#     num = (re.search(r'^([\+][7]\s[\(]\d{3,3}[\)]\s\d{3,3}\s\d{2,2}[-]\d{2,2})$', number) and True)
#     print(bool(num))
#
#
# verify_number("+7 (111) 111 11-11")
