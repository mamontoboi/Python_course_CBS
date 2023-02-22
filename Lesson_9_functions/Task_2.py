# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

def palindrome(phrase):
    """
    The function checks if the phrase is palindrome
    """
    print(f"The phrase \"{phrase}\" is palindrome.") if phrase[::-1] == phrase \
        else print(f"The phrase \"{phrase}\" is not palindrome")


palindrome(input("Write your phrase here: \n"))
