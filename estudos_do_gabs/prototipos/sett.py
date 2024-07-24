resposta = input("\nO que você quer aprender hoje?: \n\n 1)Passiva do Sett \n 2)habilidade Q \n 3)Habilidade W \n 4)Habilidade E \n 5)Habilidade Ultimate(R) \n\n Escolha um número de 1 à 5: ")

if resposta == "1":
    print("Nome: Ousadia da Arena \nDescrição: Os ataques básicos de Sett alternam entre socos de direita e esquerda. Socos de direita são levemente mais fortes e rápidos. Como Sett odeia perder, recebe Regeneração de Vida adicional com base na Vida perdida.")
elif resposta == "2":
    print("Nome: Pancadaria \nDescrição: Os próximos dois ataques de Sett causam dano adicional com base na Vida máxima do alvo. Ele também recebe Velocidade de Movimento enquanto se move em direção a Campeões inimigos.")
elif resposta == "3":
    print("Nome: Casca-grossa \nDescrição: O dano que Sett sofre é armazenado passivamente como Ousadia. Ao conjurar a habilidade, Sett consome toda a Ousadia armazenada em troca de um escudo e desfere um soco em uma área, causando Dano Verdadeiro no centro e Dano Físico nas laterais.")
elif resposta == "4":
    print("Nome: Quebra-crânio \nDescrição:  Sett puxa todos os inimigos de cada lado seu, causando dano e atordoando. Caso haja inimigos somente de um lado, eles sofrem redução de velocidade em vez de atordoamento.")
elif resposta == "5":
    print("Nome: Hora do Show \nDescrição: Sett carrega um Campeão inimigo pelos ares e o arremessa no chão, causando dano e redução de velocidade a todos os inimigos que estiverem próximos ao local de aterrissagem.")

outroChamp = input("\nVocê deseja verificar outro campeão? ")

if outroChamp == "Sim" or "sim":
    print("\nSelecione o campeão")
    novo_champ = input("""    1) Nasus
    2) Kennen
    3) Draven
    4) Twitch
    5) Teemo
""")
    if novo_champ == "1":
        print("Nasus surgiu como uma figura sábia e forte, com cabeça de chacal, e Renekton tornou-se uma fera musculosa semelhante a um crocodilo. Nasus havia recebido poderes muito além da compreensão dos mortais. A grande dádiva de sua Ascensão era que, agora, ele poderia passar vidas inteiras estudando e refletindo...")
    elif novo_champ == "2":
        print("Rápido como um raio e sábio devido a longos anos de experiência e muitas histórias vividas, Kennen trabalha junto ao Olho do Crepúsculo, Shen, para proteger a frágil harmonia das Primeiras Terras usando tempestades de shuriken e ataques devastadores de energia elétrica.")
    elif novo_champ == "3":
        print("Em Noxus, guerreiros conhecidos como Desafiadores lutam um contra o outro em uma arena onde sangue é derramado e a força é testada, mas nenhum foi tão celebrado como Draven. Antes um soldado, ele descobriu que as multidões apreciavam seu instinto pelo drama e sua habilidade suprema com seus machados giratórios. Viciado no espetáculo de sua própria perfeição impetuosa, Draven jurou derrotar qualquer que seja seu oponente para garantir que seu nome será cantado pelo império para todo o sempre.")
    elif novo_champ == "4":
        print("Um rato zaunita empesteado de nascença e um apreciador da imundície por paixão, Twitch não tem medo de sujar as patas. Mirando com uma balestra embebida em químicos no centro do coração dourado de Piltover, ele jurou mostrar àqueles na cidade de cima quão imundos eles realmente são. Sempre à espreita, quando ele não está se esgueirando no Sumidouro, ele está cavando fundo no lixo dos outros por tesouros descartados… e talvez um sanduíche bolorento.")
    elif novo_champ == "5":
        print("Indiferente até aos obstáculos mais perigosos e ameaçadores, Teemo vasculha o mundo com infinito entusiasmo e animação. Um yordle com uma inabalável moral que se orgulha de seguir o Código dos Escoteiros de Bandópolis, às vezes com tanta dedicação que não se toca das possíveis consequências de suas ações.")
    else:
        print("Este caracter não é correspondente a um Champ main Gabs")
else:
    print("\nOk, é nois")