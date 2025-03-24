# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 18:12:27 2025

@author: Berkay
"""

def cozulmus_mesaj(sifreli_mesaj):
    cozulmus = []
    for char in sifreli_mesaj:
        if char.isalpha():
            if char.islower():
                cozulmus_char = chr(((ord(char) - ord('a') - 5) % 26 + ord('a')))
            else:
                cozulmus_char = chr(((ord(char) - ord('A') - 5) % 26 + ord('A')))
            cozulmus.append(cozulmus_char)
        elif char.isdigit():
            cozulmus.append(char) 
        else:
            cozulmus.append(char)
    return ''.join(cozulmus)

sifreli_mesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
cozulen_mesaj = cozulmus_mesaj(sifreli_mesaj)
print("Çözülmüş Mesaj:", cozulen_mesaj)