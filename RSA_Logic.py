import math
from typing import Tuple, List, Dict


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0 and number > 2:
        return False
    else:
        for i in range(3, int(math.sqrt(number)+1), 2):
            if number % i == 0:
                return False
        return True


def extended_gcd(a, b) -> Tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m) -> int:
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def coprimes(phi, n) -> List[int]:
    coprime_phi = set()
    coprime_n = set()
    for i in range(2, phi):
        if extended_gcd(phi, i)[0] == 1:
            coprime_phi.add(i)
    for j in range(2, n):
        if extended_gcd(n, j)[0] == 1:
            coprime_n.add(j)

    filtered = filter(lambda x: 1 < x < phi, list(coprime_phi.intersection(coprime_n)))
    return list(filtered)


def encrypt_block(m: int, e: int, n: int) -> int:
    return m**e % n


def decrypt_block(c: int, d: int, n: int) -> int:
    return c**d % n


def encrypt_message(message: str, e: int, n: int, table: Dict[str, int]) -> str:
    return "".join(list(table.keys())[list(table.values()).index(encrypt_block(table[x], e, n))] for x in message)
    # return [list(table.keys())[list(table.values()).index(encrypt_block(table[x], e, n))] for x in message]


def decrypt_message(message: str, d: int, n: int, table: Dict[str, int]) -> str:
    return "".join(list(table.keys())[list(table.values()).index(decrypt_block(table[x], d, n))] for x in message)






