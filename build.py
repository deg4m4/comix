#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Generates the Comix font files based on Comic Shanns font.
Required files:
- vendor/comic-shanns.ttf
- vendor/Cousine-Regular.ttf
Based on:
- monospacifier: https://github.com/cpitclaudel/monospacifier/blob/master/monospacifier.py
- YosemiteAndElCapitanSystemFontPatcher: https://github.com/dtinth/YosemiteAndElCapitanSystemFontPatcher/blob/master/bin/patch
"""

import os
import re
import sys

print(sys.stdout.encoding)

import fontforge
import psMat
import unicodedata
import numpy as np

def height(font):
    return float(font.capHeight)

def adjust_height(source, template, scale):
    source.selection.all()
    source.transform(psMat.scale(height(template) / height(source)))
    for attr in ['ascent', 'descent',
                'hhea_ascent', 'hhea_ascent_add',
                'hhea_linegap',
                'hhea_descent', 'hhea_descent_add',
                'os2_winascent', 'os2_winascent_add',
                'os2_windescent', 'os2_windescent_add',
                'os2_typoascent', 'os2_typoascent_add',
                'os2_typodescent', 'os2_typodescent_add',
                ]:
        setattr(source, attr, getattr(template, attr))
    source.transform(psMat.scale(scale))

font = fontforge.open('vendor/comic-shanns.ttf')
ref = fontforge.open('vendor/Cousine-Regular.ttf')

font.familyname = 'Comix'
font.version = '0.1.1'
font.comment = 'https://github.com/dparthka/comix'
font.copyright = 'https://github.com/dparthka/comix/blob/master/LICENSE'

adjust_height(font, ref, 0.875)
font.sfnt_names = [] # Get rid of 'Prefered Name' etc.
font.fontname = 'Comix'
font.fullname = 'Comix'
font.generate('Comicx.ttf')

font.selection.all()
font.fontname = 'Comix-Bold'
font.fullname = 'Comix Bold'
font.weight = 'Bold'
font.changeWeight(32, "LCG", 0, 0, "squish")
font.generate('Comix-Bold.ttf')
