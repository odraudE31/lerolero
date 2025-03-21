#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito comercial com sentido profundo."""

import random

parte1 = ["O sistema em desenvolvimento", "O novo protocolo de comunicação", "O algoritmo foi otimizado e"]
parte2 = ["Possui excelente desempenho", "Oferece garantias de precisão acima da média", "Preenche uma lacuna significativa"]
parte3 = ["Nas aplicações a que se destina", "Em relação às opções disponíveis no mercado", "Promovendo amplas vantagens competitivas a seus usuários"]


lingua = int(input("Escolha a lingua / Choose the language: 1-portugues; 2-english.\n"))

if(lingua == 2):
    parte1 = []
    parte2 = []
    parte3 = []


print(random.choice(parte1), random.choice(parte2), random.choice(parte3))



