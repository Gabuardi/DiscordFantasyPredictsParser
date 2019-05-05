import json
from bo1_parser import Bo1Parser
from bo5_parser import Bo5Parser


# BO1 PARSER ------------------------------------------------------------------

matches = [
    {'team1': 'DFM', 'team2': 'ITZ'},
    {'team1': 'VEG', 'team2': 'MEG'},
    {'team1': 'DFM', 'team2': 'MEG'},
    {'team1': 'INT', 'team2': 'VEG'},
    {'team1': 'INT', 'team2': 'MEG'},
    {'team1': 'DFM', 'team2': 'VEG'},
    {'team1': 'INT', 'team2': 'DFM'},
    {'team1': 'MEG', 'team2': 'VEG'},
]

bo1predicts = Bo1Parser('MSI 2019  - Play-In Día 3 (respuestas)', matches)


# BO5 PARSER ------------------------------------------------------------------

bo5predicts = Bo5Parser('MSI 2019 - Eliminatorias Play-In Día 1 (respuestas)')
bo5predicts.parse()


# EXPORT JSON FILE --------------------------------------------------------------

with open('result.json', 'w') as fp:
    json.dump(bo5predicts.parse(), fp)