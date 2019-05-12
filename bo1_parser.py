import pandas as pd
import re


class Bo1Parser:
    df = None
    matches = []
    teams = {
        'DFM': 'DetonatioN FocusMe',
        'INT': 'INTZ e-Sports Club',
        'VEG': 'Vega Squadron',
        'MEG': 'MEGA Esports',
        'G2': 'G2 Esports',
        'SKT': 'SK telecom T1',
        'FW': 'Flash Wolves',
        'TL': 'Team Liquid',
        'IG': 'Invictus Gaming',
        'PVB': 'Phong Vũ Buffalo'

    }

    def __init__(self, file_name):
        self.df = pd.read_excel('excel_files/' + file_name + '.xlsx', sheet_name='Respuestas de formulario 1')
        self.matches = self.get_matches()

    def parse(self):
        print('PARSED :)')
        return {'matches': self.get_matches(), 'user_predicts': self.get_user_predicts()}

    def get_matches(self):
        columns = self.df.columns.values
        matches = []

        for column in range(2, len(columns)):
            columnHeader = columns[column]
            columnHeader = re.sub('Partido #[0-9]: ', '', columnHeader)
            teams = columnHeader.split(' vs ')
            matches.append({'team1': teams[0], 'team2': teams[1]})
        return matches

    def get_user_predicts(self):
        user_predicts = []
        for row in range(self.df.iloc[:, 0].count()):

            teams_predictions = []
            for column in range(2, len(self.matches) + 2):
                if self.df.iloc[row, column] == self.teams[self.matches[column - 2]['team1']]:
                    teams_predictions.append(1)
                else:
                    teams_predictions.append(2)

            user_predicts.append({
                'user_name': self.df.iloc[row, 1],
                'pts': 0,
                'states': [],
                'teams_predictions': teams_predictions
            })
        return user_predicts
