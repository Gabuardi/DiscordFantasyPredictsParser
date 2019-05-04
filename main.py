from bo3_parser import Bo3Parser


# BO3 PARSER ------------------------------------------------------------------

matches = [
    {'team1': 'DFM', 'team2': 'INT'},
    {'team1': 'VEG', 'team2': 'MEG'},
    {'team1': 'DFM', 'team2': 'MEG'},
    {'team1': 'INT', 'team2': 'VEG'},
    {'team1': 'INT', 'team2': 'MEG'},
    {'team1': 'DFM', 'team2': 'VEG'},
    {'team1': 'INT', 'team2': 'DFM'},
    {'team1': 'MEG', 'team2': 'VEG'},
]

predicts = Bo3Parser('MSI 2019  - Play-In Día 3 (respuestas)', matches)

print(predicts.parse())
