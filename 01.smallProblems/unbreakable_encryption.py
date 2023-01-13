from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    print("\n(RK) - Generating Random key...")

    # create aleatory lenght bytes
    tb: bytes = token_bytes(length)
    print(f'(RK)1. token bytes: {tb}')

    # convert bytes to bits 
    return int.from_bytes(tb, 'big')

def encrypt(original: str) -> Tuple[int, int]:
    print('\n(E) Encrypting...')

    original_bytes: bytes = original.encode()
    print(f'(E)1. Original_bytes: {original_bytes}')

    dummy: int = random_key(len(original_bytes))
    print(f'\n(E)2. Dummy: {dummy}')

    original_key: int = int.from_bytes(original_bytes, 'big')
    print(f'(E)3. Original_key: {original_key}')

    encrypted: int = original_key ^ dummy #XOR
    print(f'(E)4. Encrypted: {encrypted}')

    return encrypted, dummy

def decrypt(key1: int, key2: int) -> str:
    print('\n(D) Decrypting...')
  
    decrypted: int = key1 ^ key2 #XOR
    print(f'(D)1. Decrypted (Original Key): {decrypted}')

    temp: bytes = decrypted.to_bytes(((decrypted.bit_length() + 7) // 8), 'big')
    print(f'(D)2. Temp: {temp}')

    print(f'(D)3. Temp Decode: {temp.decode()}')
    return temp.decode()


if __name__ == '__main__':
    key1, key2 = encrypt('hello world')

    print(f'\n---- Encrypted Key: {key1}')
    print(f'---- Dummy Key: {key2}')

    result: str = decrypt(key1, key2)
    print(f'\n\n---- Result: {result}')

