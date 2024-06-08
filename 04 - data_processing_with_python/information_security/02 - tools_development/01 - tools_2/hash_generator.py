"""
    Programa que gera hashes automaticamente com base em uma string fornecida
    e de acordo com o algoritmo de hash escolhido pelo usuário. Utiliza da
    biblioteca 'hashlib' para implementação de hashes.
"""
import hashlib

while True:
    string = input("Enter text to generate the hash: ")

    menu = int(input('''### Choose the hash type ###
1) MD5
2) SHA1
3) SHA256
4) SHA512
Enter the hash number to be generated (0 to exit): '''))

    if menu == 0:
        break
    elif menu == 1:
        result = hashlib.md5(string.encode('UTF-8'))
        print(f"The MD5 hash of the string {string} is {result.hexdigest()}")
    elif menu == 2:
        result = hashlib.sha1(string.encode('UTF-8'))
        print(f"The SHA1 hash of the string {string} is {result.hexdigest()}")
    elif menu == 3:
        result = hashlib.sha256(string.encode('UTF-8'))
        print(f"The SHA256 hash of the string {string} is {result.hexdigest()}")
    elif menu == 4:
        result = hashlib.sha512(string.encode('UTF-8'))
        print(f"The SHA512 hash of the string {string} is {result.hexdigest()}")
    else:
        print("Invalid option. Try a valid option.")
