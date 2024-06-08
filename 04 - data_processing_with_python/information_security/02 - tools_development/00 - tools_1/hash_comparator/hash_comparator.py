"""
    Programa que implementa um comparador de Hashes com o uso da biblioteca 'hashlib'
    para criação de Hashes com base em um algoritmo específico.
"""
import hashlib as hl

ARCHIVE1 = 'a.txt'
ARCHIVE2 = 'b.txt'

hash1 = hl.new('ripemd160')

hash1.update(open(ARCHIVE1, 'rb').read())

hash2 = hl.new('ripemd160')

hash2.update(open(ARCHIVE2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f"Archive {ARCHIVE1} is different from archive {ARCHIVE2}")
    print(f"Hash from archive {ARCHIVE2} is ", hash2.digest())
    print(f"Hash from archive {ARCHIVE1} is ", hash1.digest())
else:
    print(f"Archive {ARCHIVE1} is equal to archive {ARCHIVE2}")
    print(f"Hash from archive {ARCHIVE2} is ", hash2.digest())
    print(f"Hash from archive {ARCHIVE1} is ", hash1.digest())