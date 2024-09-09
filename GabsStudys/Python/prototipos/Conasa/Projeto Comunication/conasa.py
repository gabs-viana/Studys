import pandas as pd

# Carregar as planilhas A e B, ignorando as 3 primeiras linhas
planilha_a = pd.read_excel('A.xlsx', skiprows=3)
planilha_b = pd.read_excel('B.xlsx', skiprows=3)

# Selecionar as colunas de interesse, incluindo 'Date (Data de nascimento do funcionário)'
colunas_interesse = ['Nome', 'Matrícula', 'CPF do funcionário', 'Date (Data de nascimento do funcionário)', 'Data', 'Centro de custo', 'Função', '# Evento']

# Filtrar as colunas de interesse nas duas planilhas
planilha_a = planilha_a[colunas_interesse]
planilha_b = planilha_b[colunas_interesse]

# Renomear as colunas para melhor entendimento
planilha_a.columns = ['Nome', 'Matrícula', 'CPF', 'Data de Nascimento', 'Data', 'Centro de Custo', 'Função', 'Evento']
planilha_b.columns = ['Nome', 'Matrícula', 'CPF', 'Data de Nascimento', 'Data', 'Centro de Custo', 'Função', 'Evento']

# Converter os eventos 1 e 3 em "Admitido" e "Demitido"
planilha_a['Evento'] = planilha_a['Evento'].replace({1: 'Admitido', 3: 'Demitido'})
planilha_b['Evento'] = planilha_b['Evento'].replace({1: 'Admitido', 3: 'Demitido'})

# Garantir que a coluna 'CPF' seja tratada como string
planilha_a['CPF'] = planilha_a['CPF'].astype(str).str.zfill(11)
planilha_b['CPF'] = planilha_b['CPF'].astype(str).str.zfill(11)

# Garantir que a coluna 'Data de Nascimento' seja tratada como string no formato correto
planilha_a['Data de Nascimento'] = pd.to_datetime(planilha_a['Data de Nascimento'], errors='coerce').dt.date
planilha_b['Data de Nascimento'] = pd.to_datetime(planilha_b['Data de Nascimento'], errors='coerce').dt.date

# Função para preencher a Data de Admissão
def preencher_data_admissao(df):
    data_admissao = ''
    for index, row in df.iterrows():
        if pd.notna(row['Data']) and row['Data'] != data_admissao:
            data_admissao = row['Data']
        df.at[index, 'Data de Admissão'] = data_admissao
    return df

# Aplicar a função para preencher a Data de Admissão
planilha_a = preencher_data_admissao(planilha_a)
planilha_b = preencher_data_admissao(planilha_b)

# Converter 'Data de Admissão' para formato de data sem horário
planilha_a['Data de Admissão'] = pd.to_datetime(planilha_a['Data de Admissão']).dt.date
planilha_b['Data de Admissão'] = pd.to_datetime(planilha_b['Data de Admissão']).dt.date

# Filtrar funcionários que estão na planilha B, mas não estão na planilha A
novos_funcionarios = planilha_b[~planilha_b['Matrícula'].isin(planilha_a['Matrícula'])].copy()

# Adicionar colunas adicionais com valores em branco
novos_funcionarios['Cidade'] = ''
novos_funcionarios['Estado'] = ''
novos_funcionarios['Empresa'] = ''
novos_funcionarios['Segmento'] = ''

# Mapeamento de empresas e segmentos
mapeamento = {
    '07': ('CONASA INFRAESTRUTURA', 'LONDRINA', 'PR', 'HOLDING'),
    '23': ('CONASA ÁGUAS DE ITAPEMA', 'ITAPEMA', 'SC', 'SANEAMENTO'),
    '27': ('CONASA SANESALTO', 'SALTO', 'SP', 'SANEAMENTO'),
    '28': ('CONASA SANETRAT', 'SALTO', 'SP', 'SANEAMENTO'),
    '37': ('VIA BRASIL MT 100', 'CUIABÁ', 'MT', 'RODOVIAS'),
    '42': ('VIA BRASIL MT 246', 'CUIABÁ', 'MT', 'RODOVIAS'),
    '40': ('VIA BRASIL MT 320', 'CUIABÁ', 'MT', 'RODOVIAS'),
    '43': ('VIA BRASIL BR-163', 'SINOP', 'MT', 'RODOVIAS'),
    '44': ('ÁGUAS DO SERTÃO', 'MACEIÓ', 'AL', 'SANEAMENTO'),
    '31': ('URBELUZ', 'RIO DAS OSTRAS', 'RJ', 'ILUMINAÇÃO'),
    '33': ('CARAGUALUZ', 'CARAGUATATUBA', 'SP', 'ILUMINAÇÃO'),
    '26': ('LUZ DE BELÉM', 'BELÉM', 'PA', 'ILUMINAÇÃO'),
    '32': ('ALEGRETE', 'SÃO JOÃO DE MERITI', 'RJ', 'ILUMINAÇÃO')
}

# Função para preencher informações da empresa e segmento
def preencher_empresa_segmento(df):
    df['Empresa'] = df['Matrícula'].str[:2].map(lambda x: mapeamento.get(x, ('', '', ''))[0])
    df['Cidade'] = df['Matrícula'].str[:2].map(lambda x: mapeamento.get(x, ('', '', ''))[1])
    df['Segmento'] = df['Matrícula'].str[:2].map(lambda x: mapeamento.get(x, ('', '', ''))[2])
    df['Estado'] = df['Matrícula'].str[:2].map(lambda x: mapeamento.get(x, ('', '', ''))[3])
    return df

# Aplicar a função para preencher a empresa e segmento
novos_funcionarios = preencher_empresa_segmento(novos_funcionarios)

# Renomear colunas conforme a sequência desejada
novos_funcionarios = novos_funcionarios[['Nome', 'Matrícula', 'CPF', 'Função', 'Data de Admissão', 
                                        'Centro de Custo', 'Centro de Custo', 'Cidade', 'Estado', 
                                        'Data de Nascimento', 'Empresa', 'Segmento', 'Evento']]

# Renomear colunas para correspondência final
novos_funcionarios.columns = ['Nome', 'Matrícula', 'CPF', 'Cargo', 'Data de Admissão', 
                              'Departamento', 'Grupo Hierárquico', 'Cidade', 'Estado', 
                              'Data de Nascimento', 'Empresa', 'Segmento', 'Evento']

# Exportar para uma nova planilha Excel
novos_funcionarios.to_excel('novos_funcionarios_atualizado.xlsx', index=False)

print("Exportação concluída. Novos funcionários exportados para 'novos_funcionarios_atualizado.xlsx'.")
