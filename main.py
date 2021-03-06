import json
from bo1_parser import Bo1Parser
from bo5_parser import Bo5Parser


# BO1 PARSER ------------------------------------------------------------------


# bo1predicts = Bo1Parser('MSI 2019 - Grupos_ Día 5 (respuestas)')


# BO5 PARSER ------------------------------------------------------------------

bo5predicts = Bo5Parser('MSI 2019 - Semifinales Día 2 (respuestas)')


# EXPORT JSON FILE --------------------------------------------------------------

with open('result.json', 'w') as fp:
    json.dump(bo5predicts.parse(), fp)
