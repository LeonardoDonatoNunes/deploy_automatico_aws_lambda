import pandas as pd

def lambda_handler(evend, context):
    x = {'x': [1,2], 'x': [3,4]}
    dados = pd.DataFrame(x)
    print(dados)
