import re


def valid_number():
    print("Valid number pattern\n+7 (111) 111 11-11\nВведите номер: ")
    number = str(input())
    check_num = re.search(r'(\+7\s[\(]\d\d\d[\)]\s\d\d\d\s\d\d[-]\d\d)', number)
    if check_num is None:
        print(False)
    else:
        print(True)


valid_number()



#
# valid number pattern
# +7 (111) 111 11-11
#
