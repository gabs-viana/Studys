import tkinter as tk
from PIL import Image, ImageTk  # Pillow para manipular as imagens


class Comodo:
    def __init__(self, nome, dono, pendencias, status, imagem):
        self.nome = nome
        self.dono = dono
        self.pendencias = pendencias
        self.status = status
        self.imagem = imagem  # Caminho para a imagem do cômodo

# Instâncias dos cômodos
comodo1 = Comodo("Sala de estar", "Geral", ["1)Suporte para Modem de internet", "2)Instalar a TV no suporte"], "95% Funcional", "imgs/sala.png")
comodo2 = Comodo("Quarto 1", "Gabriel", ["1)Reforma e pintura parede vermelha", "2)Substituir a janela por uma mais moderna + blackout"], "98% Funcional", "imgs/sala.png")
comodo3 = Comodo("Banheiro", "Geral", ["1)Substituir pia por uma mais eficiente", "2)Comprar um suporte de itens decente"], "80% Funcional", "imgs/sala.png")
comodo4 = Comodo("Quarto 2", "Felipe e Miguel", ["1)Organização pessoal", "2)Cortinas para o varão"], "70% Funcional", "imgs/sala.png")
comodo5 = Comodo("Cozinha", "Geral", ["1)Substituir a pia por uma mais decente", "2)Melhorar a organização dos alimentos"], "85% Funcional", "imgs/sala.png")
comodo6 = Comodo("Suíte", "Júlio e Fernanda", ["1)Consertar e colocar em uso o banheiro", "2)Organização pessoal"], "92% Funcional", "imgs/sala.png")
comodo7 = Comodo("Corredor principal", "Geral", ["1)Consertar paredes", "2)Trocar lâmpadas por inteligentes"], "68% Funcional", "imgs/sala.png")
comodo8 = Comodo("Área", "Geral", ["1)Consertar paredes", "2)Trocar lâmpadas por inteligentes"], "68% Funcional", "imgs/sala.png")
comodo9 = Comodo("Pets", "Geral", ["1)Consertar e substituir grades", "2)Trocar lâmpadas por inteligentes"], "75% Funcional", "imgs/sala.png")
comodo10 = Comodo("Corredor adjacente", "Geral", ["1)Otimizar o espaço reduzindo inutilidades", "2)Consertar os varais"], "88% Funcional", "imgs/sala.png")
comodo11 = Comodo("Fundos", "Geral", ["1)Consertar calhas", "2)Organizar tralhas"], "77% Funcional", "imgs/sala.png")

# Função para exibir detalhes de um cômodo em uma janela pop-up
def exibir_detalhes(comodo):
    # Criar uma nova janela pop-up
    janela_detalhes = tk.Toplevel(janela)
    janela_detalhes.title(f"Detalhes do {comodo.nome}")
    janela_detalhes.geometry("300x400")  # Ajuste o tamanho conforme necessário

    # Exibir os detalhes do cômodo
    detalhes_texto = f"Nome: {comodo.nome}\nDono: {comodo.dono}\nPendências:\n- " + "\n- ".join(comodo.pendencias) + f"\nStatus: {comodo.status}"
    detalhes_label = tk.Label(janela_detalhes, text=detalhes_texto, justify=tk.LEFT)
    detalhes_label.pack(padx=10, pady=10)

    # Carregar e exibir a imagem do cômodo
    img = Image.open(comodo.imagem)
    img = img.resize((250, 250))  # Redimensiona a imagem para caber na janela
    img_tk = ImageTk.PhotoImage(img)
    label_imagem = tk.Label(janela_detalhes, image=img_tk)
    label_imagem.image = img_tk  # Manter uma referência da imagem
    label_imagem.pack(pady=10)

    # Botão para editar as informações
    def editar_comodo():
        janela_edicao = tk.Toplevel(janela_detalhes)
        janela_edicao.title(f"Editar {comodo.nome}")

        tk.Label(janela_edicao, text="Pendências:").pack()
        entrada_pendencias = tk.Entry(janela_edicao, width=100)
        entrada_pendencias.insert(0, ", ".join(comodo.pendencias))
        entrada_pendencias.pack()

        tk.Label(janela_edicao, text="Status:").pack()
        entrada_status = tk.Entry(janela_edicao, width=50)
        entrada_status.insert(0, comodo.status)
        entrada_status.pack()

        def salvar_mudancas():
            # Atualizar as pendências e status do cômodo com as novas entradas
            comodo.pendencias = entrada_pendencias.get().split(", ")
            comodo.status = entrada_status.get()
            # **Atualizar a label de detalhes com os novos valores** - MUDAÇA VISÍVEL
            detalhes_label['text'] = f"Nome: {comodo.nome}\nDono: {comodo.dono}\nPendências:\n- " + "\n- ".join(comodo.pendencias) + f"\nStatus: {comodo.status}" 
            # Fechar a janela de edição após salvar as mudanças
            janela_edicao.destroy()

        tk.Button(janela_edicao, text="Salvar", command=salvar_mudancas).pack()

    tk.Button(janela_detalhes, text="Editar", command=editar_comodo).pack(pady=10)

# Criar a janela principal
janela = tk.Tk()
janela.title("Mapa da Casa")
janela.geometry("600x500")  # Ajuste o tamanho conforme necessário

# Criar um Canvas para desenhar a planta baixa
canvas = tk.Canvas(janela, width=600, height=500, bg='white')
canvas.pack()

# Criar um Frame dentro do Canvas para os botões
frame_botao = tk.Frame(canvas, bg='lightgrey')
frame_botao.place(x=0, y=0, width=600, height=500)

# Representação dos cômodos no Frame
# Cada botão é posicionado conforme a planta baixa real
botao_comodo1 = tk.Button(frame_botao, text="Sala de estar", command=lambda: exibir_detalhes(comodo1))
botao_comodo1.place(x=250, y=250, width=100, height=100)  # Ajuste as posições e tamanhos

botao_comodo2 = tk.Button(frame_botao, text="Quarto 1", command=lambda: exibir_detalhes(comodo2))
botao_comodo2.place(x=235, y=200, width=90, height=50)

botao_comodo3 = tk.Button(frame_botao, text="Banheiro", command=lambda: exibir_detalhes(comodo3))
botao_comodo3.place(x=235, y=170, width=90, height=30)

botao_comodo4 = tk.Button(frame_botao, text="Quarto 2", command=lambda: exibir_detalhes(comodo4))
botao_comodo4.place(x=235, y=120, width=90, height=50)

botao_comodo5 = tk.Button(frame_botao, text="Cozinha", command=lambda: exibir_detalhes(comodo5))
botao_comodo5.place(x=200, y=75, width=150, height=45)

botao_comodo6 = tk.Button(frame_botao, text="Suíte", command=lambda: exibir_detalhes(comodo6))
botao_comodo6.place(x=235, y=15, width=115, height=60)

botao_comodo7 = tk.Button(frame_botao, text="C.", command=lambda: exibir_detalhes(comodo7))
botao_comodo7.place(x=325, y=120, width=25, height=130)

botao_comodo8 = tk.Button(frame_botao, text="Área", command=lambda: exibir_detalhes(comodo8))
botao_comodo8.place(x=250, y=350, width=100, height=70)

botao_comodo9 = tk.Button(frame_botao, text="Pets", command=lambda: exibir_detalhes(comodo9))
botao_comodo9.place(x=200, y=250, width=50, height=170)

botao_comodo10 = tk.Button(frame_botao, text="C.2", command=lambda: exibir_detalhes(comodo10))
botao_comodo10.place(x=200, y=120, width=40, height=130)

botao_comodo11= tk.Button(frame_botao, text="Fund", command=lambda: exibir_detalhes(comodo11))
botao_comodo11.place(x=200, y=15, width=35, height=60)

# Executar a janela principal
janela.mainloop()
