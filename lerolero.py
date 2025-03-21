#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito comercial com sentido profundo."""

import random

parte1 = []
parte2 = []
parte3 = []

lingua = int(input("Escolha a lingua / Choose the language: 1-portugues; 2-english.\n"))

if(lingua == 2):
    parte1 = []
    parte2 = []
    parte3 = []


print(random.choice(parte1), random.choice(parte2), random.choice(parte3))

