from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path

# Caminho do arquivo para salvar os dados
arquivo_banco = Path("/mnt/data/banco_horas.csv")

# Verifica se já existe um arquivo e carrega, senão cria novo
if arquivo_banco.exists():
    banco = pd.read_csv(arquivo_banco)
    banco["Data"] = pd.to_datetime(banco["Data"])
else:
    banco = pd.DataFrame(columns=["Data", "1E", "1S", "2E", "2S", "Horas Trabalhadas", "Saldo Acumulado"])

# Função para converter string HH:MM em timedelta
def to_timedelta(hora_str):
    h, m = map(int, hora_str.split(":"))
    return timedelta(hours=h, minutes=m)

# Função principal de controle de banco de horas
def banco_horas_interativo(proxima_etapa=None):
    carga_dia = timedelta(hours=8)
    hoje = datetime.today().date()

    entrada1 = None
    saida1 = None
    entrada2 = None
    saida2 = None

    print(f"Registrando banco de horas para: {hoje}")
    
    if proxima_etapa:
        # Recupera o último registro incompleto
        ultimo = banco.iloc[-1]
        entrada1 = ultimo["1E"]
        saida1 = ultimo["1S"]
        entrada2 = ultimo["2E"]
        saida2 = ultimo["2S"]
        print(f"Retomando de onde parou: 1E={entrada1}, 1S={saida1}, 2E={entrada2}, 2S={saida2}")
    
    def solicitar_entrada(nome, valor_atual):
        if valor_atual:
            return valor_atual
        opcao = input(f"{nome}: (hh:mm ou ENTER para armazenar e sair) ").strip()
        if opcao == "":
            return None
        return opcao

    entrada1 = solicitar_entrada("1E", entrada1)
    if entrada1 is None:
        salvar_parcial(hoje, entrada1, saida1, entrada2, saida2)
        return "Sessão interrompida na 1E"
    
    saida1 = solicitar_entrada("1S", saida1)
    if saida1 is None:
        salvar_parcial(hoje, entrada1, saida1, entrada2, saida2)
        return "Sessão interrompida na 1S"
    
    entrada2 = solicitar_entrada("2E", entrada2)
    if entrada2 is None:
        salvar_parcial(hoje, entrada1, saida1, entrada2, saida2)
        return "Sessão interrompida na 2E"
    
    saida2 = solicitar_entrada("2S", saida2)
    if saida2 is None:
        salvar_parcial(hoje, entrada1, saida1, entrada2, saida2)
        return "Sessão interrompida na 2S"

    # Tudo preenchido, calcular horas trabalhadas
    total = (to_timedelta(saida1) - to_timedelta(entrada1)) + (to_timedelta(saida2) - to_timedelta(entrada2))
    saldo = total - carga_dia
    saldo_acumulado = banco["Saldo Acumulado"].iloc[-1] if not banco.empty else timedelta()

    saldo_acumulado = pd.to_timedelta(saldo_acumulado) + saldo

    novo_registro = pd.DataFrame([{
        "Data": hoje,
        "1E": entrada1,
        "1S": saida1,
        "2E": entrada2,
        "2S": saida2,
        "Horas Trabalhadas": str(total),
        "Saldo Acumulado": str(saldo_acumulado)
    }])

    banco_final = pd.concat([banco, novo_registro], ignore_index=True)
    banco_final.to_csv(arquivo_banco, index=False)
    
    return f"Registro salvo com sucesso. Horas do dia: {total}, saldo do dia: {saldo}, acumulado: {saldo_acumulado}"

# Função auxiliar para salvar parcial
def salvar_parcial(data, e1, s1, e2, s2):
    parcial = pd.DataFrame([{
        "Data": data,
        "1E": e1,
        "1S": s1,
        "2E": e2,
        "2S": s2,
        "Horas Trabalhadas": "",
        "Saldo Acumulado": ""
    }])
    df_final = pd.concat([banco, parcial], ignore_index=True)
    df_final.to_csv(arquivo_banco, index=False)
    print("Sessão armazenada. Continue depois.")

"Pronto para executar via terminal Python local."
