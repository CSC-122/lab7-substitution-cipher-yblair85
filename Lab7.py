# CSC 122
# Substitution Cipher
# By <Yulia Blair>

"""
Inputs, Processes, Outputs (IOP)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s):
"""

def main():
    cipher = []
    message = input("Enter the message to be encrypted: ")
    for letter in message:
        cipher.append(chr(ord(letter) + 3))
    print(f"Encrypted message = {''.join(cipher)}\n")

    plaintext = []
    message = input("Enter the cipher to be decrypted: ")
    for letter in message:
        plaintext.append(chr(ord(letter) - 3))
    print(f"Decrypted message = {''.join(plaintext)}\n")




if __name__ == '__main__':
    main()
