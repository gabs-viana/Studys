import tkinter as tk

# Mapeamento de empresas, senhas e domínios
mapeamento_empresas = {
    'CONASA INFRAESTRUTURA': ('conas@24', 'conasa.com'),
    'CONASA ÁGUAS DE ITAPEMA': ('conas@24', 'conasa.com'),
    'CONASA SANESALTO': ('conas@24', 'conasa.com'),
    'CONASA SANETRAT': ('conas@24', 'conasa.com'),
    'VIA BRASIL MT 100': ('viabr@24', 'viabrmt.com.br'),
    'VIA BRASIL MT 246': ('viabr@24', 'viabrmt.com.br'),
    'VIA BRASIL MT 320': ('viabr@24', 'viabrmt.com.br'),
    'VIA BRASIL BR-163': ('viabr@24', 'viabr163.com.br'),
    'ÁGUAS DO SERTÃO': ('aguasds@24', 'aguasdosertao.com'),
    'URBELUZ': ('urbe@24', 'urbeluz.com'),
    'CARAGUALUZ': ('caragua@24', 'caragua.com'),
    'LUZ DE BELÉM': ('luzdb@24', 'luzdebelem.com'),
    'ALEGRETE': ('alegrete@24', 'alegreterj.com')
}

def gerar_dados():
    nome = entry_nome.get()
    cargo = entry_cargo.get()
    setor = entry_setor.get()
    empresa = combo_empresa.get()

    # Verificar se a empresa está no mapeamento
    if empresa in mapeamento_empresas:
        senha, dominio = mapeamento_empresas[empresa]
    else:
        senha, dominio = '(senha indefinida)', '(domínio indefinido)'

    # Separar o primeiro e o último nome
    nomes = nome.split()
    primeiro_nome = nomes[0]
    ultimo_nome = nomes[-1]

    # Gerar Nome de usuário
    nome_usuario = f"{primeiro_nome.capitalize()}.{ultimo_nome.capitalize()}"

    # Gerar Email
    email = f"{primeiro_nome.lower()}.{ultimo_nome.lower()}@{dominio}"

    # Gerar Compartilhamento
    compartilhamento = f"\SPOOL\{primeiro_nome[0].upper()}{ultimo_nome.upper()}/"

    # Exibir os dados no Text widget
    text_resultado.delete(1.0, tk.END)
    text_resultado.insert(tk.END, f"Nome Completo: {nome}\n")
    text_resultado.insert(tk.END, f"Nome de Usuário: {nome_usuario}\n")
    text_resultado.insert(tk.END, f"Email: {email}\n")
    text_resultado.insert(tk.END, f"Cargo: {cargo}\n")
    text_resultado.insert(tk.END, f"Setor: {setor}\n")
    text_resultado.insert(tk.END, f"Senha: {senha}\n")
    text_resultado.insert(tk.END, f"Compartilhamento: {compartilhamento}\n")
    
    # Inserir o aviso em vermelho
    text_resultado.insert(tk.END, "\n")
    text_resultado.insert(tk.END, "!!! Não se esqueça de flagar \"Alterar senha no próx. login\" !!!\n", "aviso")
    
    # Gerar a mensagem de resposta para email
    mensagem_email = f"\nFeito.\n\nusuário: {nome_usuario}\nsenha: {senha} (trocar no próx. login)\n"
    text_resultado.insert(tk.END, mensagem_email)

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Gerador de Usuário Protheus")

# Labels e Entries
label_nome = tk.Label(janela, text="Nome Completo:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_cargo = tk.Label(janela, text="Cargo:")
label_cargo.grid(row=1, column=0, padx=10, pady=10)
entry_cargo = tk.Entry(janela, width=40)
entry_cargo.grid(row=1, column=1, padx=10, pady=10)

label_setor = tk.Label(janela, text="Setor:")
label_setor.grid(row=2, column=0, padx=10, pady=10)
entry_setor = tk.Entry(janela, width=40)
entry_setor.grid(row=2, column=1, padx=10, pady=10)

label_empresa = tk.Label(janela, text="Empresa:")
label_empresa.grid(row=3, column=0, padx=10, pady=10)

# Combobox para selecionar a empresa
combo_empresa = tk.StringVar()
opcoes_empresa = tk.OptionMenu(janela, combo_empresa, *mapeamento_empresas.keys())
opcoes_empresa.grid(row=3, column=1, padx=10, pady=10)

# Botão para gerar os dados
botao_gerar = tk.Button(janela, text="Gerar Dados", command=gerar_dados)
botao_gerar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Text widget para exibir os resultados
text_resultado = tk.Text(janela, height=15, width=60)
text_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Definir estilo do texto vermelho para o aviso
text_resultado.tag_config("aviso", foreground="red", font=("Helvetica", 10, "bold"))

janela.mainloop()
