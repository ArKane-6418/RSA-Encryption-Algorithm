import json
from RSA_Logic import is_prime, modinv, coprimes, encrypt_message, \
    decrypt_message


with open("table.json", "r") as file:
    table = json.load(file)

# Encryption
p = int(input("Input your first prime number: "))
q = int(input("Input your second prime number: "))
while not is_prime(p) or not is_prime(q):
    try:
        print("Please make sure p and q are prime.")
        p = int(input("Input your first prime number: "))
        q = int(input("Input your second prime number: "))
    except ValueError:
        print("Please input valid integers.")

n = p*q
phi = (p-1)*(q-1)

# Determine the encryption exponent

possible_e = coprimes(phi, n)

e = 0
invalid = True

while invalid:
    e = int(input(f"Select your encryption exponent from the list of possible "
                  f"encryption exponents \n{possible_e} \n"))
    if e not in possible_e:
        print("That value is invalid.")
    else:
        invalid = False

d = modinv(e, phi)

print(f"Your public key is: {(e, n)}")
print(f"Your private key is: {(d, n)}")

s = input("Please enter the message you want to encrypt: ")
encrypted = encrypt_message(s, e, n, table)
print(f"This is your encrypted message: \'{encrypted}\'")

yes_no = input("Would you like to decrypt your message? (y/n): ")

while yes_no.lower() != "y" and yes_no.lower() != "n":
    print("Please only use \'y\' or \'n\'.")
    yes_no = input("Would you like to decrypt your message? (y/n): ")

if yes_no.lower() == "y":
    decrypted = decrypt_message(encrypted, d, n, table)
    print(f"Your decrypted message is \'{decrypted}\'")
else:
    pass











