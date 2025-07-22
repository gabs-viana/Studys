from datetime import datetime, timedelta

tipo_site = input("""Qual a complexidade do site desejado?
1) Básico
2) Médio
3) Avançado
Insira sua resposta: """)

tempo_basico = 3
tempo_medio = 5
tempo_avancado = 10
data_atual = datetime.now()

if tipo_site == "1":
    data_estimada = data_atual + timedelta(days=tempo_basico)
    print(f"O site foi requerido na data {data_atual.strftime("%d/%m/%Y")} e ficará pronto até dia {data_estimada.strftime("%d/%m/%Y às %H:%M")}")
elif tipo_site == "2": 
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O site foi requerido na data {data_atual.strftime("%d/%m/%Y")} e ficará pronto até dia {data_estimada.strftime("%d/%m/%Y às %H:%M")}")
elif tipo_site == "3":
    data_estimada = data_atual + timedelta(days=tempo_avancado)
    print(f"O site foi requerido na data {data_atual.strftime("%d/%m/%Y")} e ficará pronto até dia {data_estimada.strftime("%d/%m/%Y às %H:%M")}")
else: 
    print("Opção inválida patrão.")