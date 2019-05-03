import pandas as pd

df = pd.read_excel('excel_files/MSI 2019  - Play-In Día 3 (respuestas).xlsx', sheet_name='Respuestas de formulario 1')

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

teams = {
    'DFM': 'DetonatioN FocusMe',
    'INT': 'INTZ e-Sports Club',
    'VEG': 'Vega Squadron',
    'MEG': 'MEGA Esports',
}

user_predicts = []

for row in range(df.iloc[:, 0].count() - 1):

    teams_predictions = []
    for column in range(2, len(matches) + 1):
        if df.iloc[row, column] == teams[matches[column - 2]['team1']]:
            teams_predictions.append(1)
        else:
            teams_predictions.append(2)

    user_predicts.append({
        'user_name': df.iloc[row, 1],
        'pts': 0,
        'states': [],
        'team_predictions': teams_predictions
    })

print(user_predicts)
