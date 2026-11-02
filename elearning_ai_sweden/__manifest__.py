# -*- coding: utf-8 -*-
##############################################################################
#
#    Vertel Sverige AB, AI Sweden eLearning seed
#    Copyright (C) 2025- Vertel Sverige AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
##############################################################################

{
    'name': 'eLearning: AI Sweden Digital Workshop',
    'version': '18.0.1.0.0',
    'summary': 'Självstudiekurs i metodkritik, riskklassning och drift av AI-system',
    'category': 'eLearning',
    'author': 'Vertel Sverige AB',
    'website': 'https://vertel.se',
    'license': 'AGPL-3',
    'description': """
eLearning: AI Sweden Digital Workshop
=====================================

Installerar en färdig självstudiekurs i eLearning — fem sektioner, eget
tempo, ingen lärarledd workshop.

Kursen vänder Vertels befintliga Digitaliseringsworkshop från nybörjarnivå
till metodkritik, riskklassning och drift. Målgruppen är personer med över
medelkunskap om IT och AI.

Sektioner:

1. Vad det här är och varför — metodkritik, falsk trygghet
2. Så läser du AI Canvas kritiskt — granskningsövning med facit
3. Från canvas till drift — EU AI Act nämnd, ISO 42001 i urval
4. Plattformen som bärare — spårbarhet uppgift → plan → use case
5. Manuellt test — läsaren verifierar sitt eget flöde

Kursen skapas som data vid installation och är sedan redigerbar i
eLearning-appen som vilken kurs som helst.
    """,
    'depends': [
        'website_slides',
    ],
    'data': [
        'data/slide_channel_ai_sweden.xml',
        'data/slide_channel_ai_sweden_2.xml',
        'data/slide_channel_ai_sweden_3.xml',
        'data/slide_channel_ai_sweden_4.xml',
    ],
    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False,
}
