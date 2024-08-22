import pandas as pd
from datetime import datetime

excel_file = 'alunos.xlsx'

df = pd.read_excel(excel_file)

alunos_inativos_sem_assinatura = df[(df['STATUS'] == 'INATIVO') & (df['ASSINATURA'] == 'NÃO')]

print("Alunos com status inativo e que não possuem assinatura:")
print(alunos_inativos_sem_assinatura)

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    if isinstance(data_nascimento, pd.Timestamp):
        data_nascimento = data_nascimento.to_pydatetime().date()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

alunos_inativos_sem_assinatura_maior_idade = df[
    (df['STATUS'] == 'INATIVO') & (df['ASSINATURA'] == 'NÃO') &
    (df['DATA DE NASCIMENTO'].apply(calcular_idade) >= 18)
]

print("Alunos com status inativo, sem assinatura e que são maiores de idade:")
print(alunos_inativos_sem_assinatura_maior_idade)
