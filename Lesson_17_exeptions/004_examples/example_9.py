def validate_email(address):
    assert "@" in address, "Email Addresses must contain @ sign"  # if not -- raise Assertion Error


try:
    validate_email("test@com")
except Exception as e:
    print(f'{e.__class__}: {e}')
else:  # gets printed only after successful try
    print("Here we go!")
finally:  # gets printed anyway
    print("Finally always runs whether we succeed or not.")


try:
    validate_email("test.com")
except Exception as e:
    print(f'{e.__class__}: {e}')  # <class 'AssertionError'>: Email Addresses must contain @ sign
else:  # gets printed only after successful try
    print("Here we go!")
finally:  # gets printed anyway
    print("Finally always runs whether we succeed or not.")