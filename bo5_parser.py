import pandas as pd
import re

class Bo5Parser:
    df = None
    matches = []
    teams = {
        'DFM': 'DetonatioN FocusMe',
        'INT': 'INTZ e-Sports Club',
        'VEG': 'Vega Squadron',
        'MEG': 'MEGA Esports',
        'TL': 'Team Liquid',
        'FW': 'Flash Wolves'
    }

    def __init__(self, file_name):
        self.df = pd.read_excel('excel_files/' + file_name + '.xlsx', sheet_name='Respuestas de formulario 1')
        self.matches = self.get_matches()

    def parse(self):
        self.get_matches()
        return {'matches': self.matches, 'user_predicts': self.get_user_predicts()}

    def get_matches(self):
        columns = self.df.columns.values
        matches = []
        cellType = 'match'

        for column in range(2, len(columns)):
            if cellType is 'match':
                columnHeader = columns[column]
                columnHeader = re.sub('Equipo ganador: ', '', columnHeader)
                teams = columnHeader.split(' vs ')
                matches.append({'team1': teams[0], 'team2': teams[1]})
                cellType = 'score'
            else:
                cellType = 'match'
        return matches


    def get_user_predicts(self):
        user_predicts = []

        for row in range(self.df.iloc[:, 0].count()):

            cellType = 'match'
            teams = []
            scores = []

            matchIndex = 0
            for column in range(2, (len(self.matches) * 2) + 2):

                if cellType == 'match':
                    if self.df.iloc[row, column] == self.teams[self.matches[matchIndex - 2]['team1']]:
                        teams.append(1)
                    else:
                        teams.append(2)
                    cellType = 'score'
                    matchIndex += 1
                else:
                    scores.append(self.df.iloc[row, column])
                    cellType = 'match'

            user_predicts.append({
                'user_name': self.df.iloc[row, 1],
                'pts': 0,
                'states': [],
                'teams_predictions': teams,
                'score_predictions': scores
            })

        return user_predicts
