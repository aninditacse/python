# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:23:37 2021

@author: Anindita
"""

def rsa_algo(p: int,q: int, msg: str):
    n = p * q
    z = (p-1)*(q-1)
    e = find_e(z)
    d = find_d(e, z)
    cypher_text = ''
    
    for ch in msg:
        ch = ord(ch)
        cypher_text += chr((ch ** e) % n)

    plain_text = ''
    for ch in cypher_text:
        ch = ord(ch)
        plain_text += chr((ch ** d) % n)
    return cypher_text, plain_text

def find_e(z: int):
    e = 2
    while e < z:
        if gcd(e, z)==1:
            return e
        e += 1

def find_d(e: int, z: int):
    d = 2
    while d < z:
        if ((d*e) % z)==1:
            return d
        d += 1

def gcd(x: int, y: int):
    small,large = (x,y) if x<y else (y,x)
    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large

if __name__ == "__main__":
    p,q = map(int, input("Enter inputs: ").split())
    msg = input("Enter the message: ")
    cypher_text, plain_text = rsa_algo(p, q, msg)
    print("\nEncrypted (Cypher text) : ", cypher_text)
    print("Decrypted (Plain text) : ", plain_text)