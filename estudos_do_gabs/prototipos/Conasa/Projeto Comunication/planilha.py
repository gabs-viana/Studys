import pandas as pd
from tabulate import tabulate

# Função para ler planilhas do Excel
def read_excel_file(file_path, sheet_name=None):
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    if sheet_name is None:
        data = list(data.values())[0]
    # Limpeza de colunas desnecessárias
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    return data

# Função para comparar as planilhas X e A e encontrar novos admitidos e demitidos
def compare_planilhas(planilha_x, planilha_a):
    # Removendo espaços em branco das colunas
    planilha_x.columns = planilha_x.columns.str.strip()
    planilha_a.columns = planilha_a.columns.str.strip()

    # Assumindo que a coluna "Nome" existe nas duas planilhas
    nomes_x = set(planilha_x['Nome'])
    nomes_a = set(planilha_a['Nome'])
    
    # Encontrar novos admitidos e demitidos
    novos_admitidos = planilha_a[planilha_a['Nome'].isin(nomes_a - nomes_x)]
    novos_demitidos = planilha_x[planilha_x['Nome'].isin(nomes_x - nomes_a)]

    # Listas para armazenar os dados
    admitidos_list = []
    demitidos_list = []

    for _, row in planilha_a.iterrows():
        if row['Nome'] in nomes_a - nomes_x:
            if row['Status'] == 'Admitido':
                admitidos_list.append(row)
            elif row['Status'] == 'Demitido':
                demitidos_list.append(row)

    # Convertendo listas em DataFrames
    admitidos_df = pd.DataFrame(admitidos_list).dropna(axis=1, how='all')
    demitidos_df = pd.DataFrame(demitidos_list).dropna(axis=1, how='all')

    return admitidos_df, demitidos_df

# Função para exibir tabelas formatadas no terminal
def print_table(df, status):
    print(f"\nNovos {status}:")
    if not df.empty:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
    else:
        print(f"Nenhum novo {status.lower()}.")

# Função principal
def main():
    # Lendo as planilhas
    planilha_x = read_excel_file('pX.xlsx')
    planilha_a = read_excel_file('pA.xlsx')
    
    # Comparando planilhas X e A
    novos_admitidos, novos_demitidos = compare_planilhas(planilha_x, planilha_a)
    
    # Exibindo resultados
    print_table(novos_admitidos, "Admitidos")
    print_table(novos_demitidos, "Demitidos")

if __name__ == "__main__":
    main()
