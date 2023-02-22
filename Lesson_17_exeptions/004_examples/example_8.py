def validate_email(address):
    if not "@" in address:
        raise ValueError("Email Addresses must contain @ sign")  # to call an Exception


try:
    validate_email("test.com")
except ValueError as ex:
    print("We can do some special invalid input handling here")
finally:
    print("Finally always runs whether we succeed or not.")
