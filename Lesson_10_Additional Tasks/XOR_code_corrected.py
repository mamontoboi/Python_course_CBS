# Написати функцію XOR_cipher, яка приймає два аргументи: рядок, який потрібно зашифрувати, і ключ шифрування,
# який повертає рядок, зашифрований шляхом застосування функції XOR (^) над символами рядка з ключем.
# Написати також функцію XOR_uncipher, яка по зашифрованому рядку та ключу відновлює вихідний рядок.

def enigma_in(key):
    """
    Serves to cipher the phrase.
    Args:
        key: The text, that is going to be used as a key.

    Returns: Coded version of initial phrase.

    """
    while True:
        phrase_to_cipher = input("Write your phrase to cipher: \n")
        if len(phrase_to_cipher) != len(key):
            print("Your phrase is not of the same length as your key. Try again.")
            continue
        return ''.join([chr(ord(a) ^ ord(b)) for (a, b) in zip(phrase_to_cipher, key)])


def enigma_out(value, key):
    """
    Serves to encipher the ciphered phrase.
    Args: value -- returned from encoding
        key: The key, that was used to cipher the phrase.

    Returns: Initial phrase.

    """
    return ''.join([chr(ord(a) ^ ord(b)) for (a, b) in zip(value, key)])


key = input("Please enter key: \n")

x = enigma_in(key)
print(f'Encoded phrase is {x}')

y = enigma_out(x, key)
print(f'Decoded phrase is {y}')

