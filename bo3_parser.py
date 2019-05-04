import pandas as pd


class Bo3Parser:
    df = None
    matches = []
    teams = {
        'DFM': 'DetonatioN FocusMe',
        'INT': 'INTZ e-Sports Club',
        'VEG': 'Vega Squadron',
        'MEG': 'MEGA Esports',
    }

    def __init__(self, file_name, matches):
        self.df = pd.read_excel('excel_files/' + file_name + '.xlsx', sheet_name='Respuestas de formulario 1')
        self.matches = matches

    def parse(self):
        return {'matches': self.matches, 'user_predicts': self.get_user_predicts()}

    def get_user_predicts(self):
        user_predicts = []
        for row in range(self.df.iloc[:, 0].count() - 1):

            teams_predictions = []
            for column in range(2, len(self.matches) + 1):
                if self.df.iloc[row, column] == self.teams[self.matches[column - 2]['team1']]:
                    teams_predictions.append(1)
                else:
                    teams_predictions.append(2)

            user_predicts.append({
                'user_name': self.df.iloc[row, 1],
                'pts': 0,
                'states': [],
                'team_predictions': teams_predictions
            })
        return user_predicts
