#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle
import unicodedata
import codecs
import re

def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

glyphs = [u'a',
 u'b',
 u'c',
 u'd',
 u'e',
 u'f',
 u'g',
 u'h',
 u'i',
 u'j',
 u'k',
 u'l',
 u'm',
 u'n',
 u'o',
 u'p',
 u'q',
 u'r',
 u's',
 u't',
 u'u',
 u'v',
 u'w',
 u'x',
 u'y',
 u'z',
 u'exclam',
 u'ampersand',
 u'question',
 u'Euro',
 u'percent',
 u'germandbls']

student_names = [u'Stefania-Lea Antoniadou',
 u'Burcin Araz',
 u'Peer Viktor Guba',
 u'Matthias Mann',
 u'Jennifer Mantas',
 u'Erel Özdemir',
 u'Joana von Fuchs',
 u'Judika Zerrer',
 u'Elisabeth Mross',
 u'Anna-Lena Preinfalk',
 u'Felix Marvin Vetter',
 u'Patrick Wellmann',
 u'Avalon Leonetti',
 u'Matthias Braun',
 u'Alina Kadlubsky',
 u'Jasmin Rathfelder',
 u'Dino Alexander Carasso',
 u'Constantina Di Leo',
 u'Lisa-Sarah Efeoglu',
 u'Jonas Michael Glück',
 u'Tobias Hahn',
 u'Michela Albertini',
 u'Sandra Gentner',
 u'Madlen Göhring',
 u'Jule Hartmann',
 u'Tamara Hell',
 u'Beatrice Straile',
 u'Eva Maria Strecker',
 u'Raymin Chen',
 u'Oliver Kosic',
 u'David Lindner',
 u'Yasmin Abouharia']

shuffle(glyphs)

script = """#!/usr/bin/env python

# Script to generate the %s, by %s
from robofab.world import RFont
font = RFont('Morphologic.ufo')

glyph = font.newGlyph('%s')

pen = glyph.getPen()

# ! Drawing instructions here !
# ! Otherwise nothing happens !

font.save()

"""

for i, student in enumerate(student_names):
    #f = codecs.open(slugify(student) + '.py','UTF-8')
    #f.write(script % (glyphs[i], student))
    #f.close()
    print slugify(student) + '.py', student, glyphs[i]
    print script % (glyphs[i], student)