#!/usr/bin/python3

def otwieranie_i_wczytywanie():
    
    plik = open('tekst.txt', 'r')

    tekst = plik.read()

    return tekst


