# -*- coding: utf-8 -*-
"""
@author: IdrisIbrahimERTEN
"""

v = int(input("voltaj deeğerini giriniz : "))
i = int(input("akım değerini giriniz : "))
r = int(input("direnç değerini giriniz : "))

if v == 0:
    voltaj = i*r
    print ("\n"+"Voltaj Değeri : "+str(voltaj)+" "+"v")
elif i == 0:
    akım = v/r
    print("\n"+"Akım Değeri : "+str(akım)+" "+"amper")
else:
    direnç = v/i
    print("\n"+"Direnç Değeri : "+str(direnç)+" "+"direnç")