
# This function recives plain text and key from user and encrypt the plain text according to given key.
def encrypt(plain_text: str, key: int):
    # Empty variable to store the output
    result = ""

    alphabet = "abcdefghiklmnopqrsrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in plain_text:
        if letter not in alphabet:
            # Simply add the letter as it is without encrypting it
            result += letter
        else:
            # Generate new index number by adding the value of key and performing modulo by number of total alphabets 
            encrypted_letter = (alphabet.index(letter) + key) % len(alphabet)
            # Appends the letter from alphabet which is at new index 
            result += alphabet[encrypted_letter]

    return print(result) 
    

user_text = input("Enter your plain text here: ")
user_key = int(input("Enter your key: "))
encrypt(user_text, user_key)