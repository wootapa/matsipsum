#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, random

SUBS = ['funktionaliteten', 'bitarna', 'sakerna', 'funktionaliteterna']
VERB = ['arbetar', 'kör', 'arbetar', 'rekommenderar']
PROP = ['i', 'på', 'till', 'framför', 'vid', 'om', 'mot', 'av', 'för', 'före', 'genom', 'utan', 'efter', 'över', 'bakom', 'under', 'från', 'bredvid', 'mellan']
PRON = ['jag', 'vi', 'jag', 'en kompis', 'docker', 'microsoft']
KNJS = ['och', 'eller', 'utan', 'men', 'men utan', 'samt', 'dels', 'såväl som', 'precis som']
KNJU = ['för att', 'medan då', 'fastän', 'därför att', 'innan', 'eftersom']

antal = 5
if len(sys.argv) > 1:
    antal = int(sys.argv[1])

rappakalja = []
i = 1
while i <= antal:
    rappakalja.append(random.choice(SUBS).capitalize())
    rappakalja.append(random.choice(VERB))
    rappakalja.append(random.choice(KNJS))
    rappakalja.append(random.choice(SUBS))
    rappakalja.append(random.choice(KNJU))
    rappakalja.append(random.choice(SUBS))
    rappakalja.append(random.choice(VERB))
    rappakalja.append(random.choice(SUBS) + '.')
    i = i + 1

    if i < antal:
        if random.randint(1,2) == 1:
            rappakalja.append(random.choice(PRON).capitalize())
            rappakalja.append(random.choice(KNJS))
            rappakalja.append(random.choice(PRON))
            rappakalja.append(random.choice(VERB))
            rappakalja.append(random.choice(PROP))
            rappakalja.append(random.choice(SUBS) + '.')
            i = i + 1

print(' '.join(rappakalja))
