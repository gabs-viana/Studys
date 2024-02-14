import telebot

CHAVE_API = "6761897525:AAE5R7wJFmObm6K_kZC3QUuL_UcEZc2Ujck"

bot = telebot.TeleBot(CHAVE_API)

def resposta_personalizada(mensagem):
    # Mapeia os IDs dos usuários para suas respostas personalizadas
    respostas = {
        5858174443: "Olá Gabsᶜʳᶠ! 🔴⚫ ",
        987654321: "Olá Vitão! ",
        111222333: "Olá Matheus !",
        111222333: "Olá Gabriel !",
        111222333: "Olá Diorgny !",
        111222333: "Olá Fernando !",
        # Adicione mais IDs e respostas conforme necessário
    }
    
    # Obtém o ID do remetente da mensagem
    user_id = mensagem.from_user.id

    # Retorna a resposta personalizada se o ID estiver mapeado, caso contrário, retorna None
    return respostas.get(user_id)

# @bot.message_handler(commands=["falaVitao"])
# def falaVitao(mensagem):
#       bot.reply_to(mensagem, "E ai, firmeza Vitao? monstro sagrado, preceptor do acopalipse")
#       bot.send_photo(mensagem.chat.id, "https://img.freepik.com/fotos-gratis/bela-foto-de-um-gatinho-branco-de-pelo-curto-britanico_181624-57681.jpg")

# @bot.message_handler(commands=["falaMatheus"])
# def falaVitao(mensagem):
#       pass

# @bot.message_handler(commands=["falaDiorgny"])
# def falaVitao(mensagem):
#       pass

# @bot.message_handler(commands=["falaGabriel"])
# def falaVitao(mensagem):
#       pass
    
# @bot.message_handler(commands=["falaGabs"])
# def falaVitao(mensagem):
#       print(mensagem)
#       bot.reply_to(mensagem, "Xora Gabs, maluco criador deste botzão")
#        #Esta linha precisa de revisão, desejo adicionar uma imagem logo após a mensagem

@bot.message_handler(func=resposta_personalizada)
def responder(mensagem):
      texto_personalizado = resposta_personalizada(mensagem)
      bot.reply_to(mensagem, texto_personalizado)

@bot.message_handler(func=lambda message: True)
def responder_padrao(mensagem):
      texto = """
            Escolha uma opção para continuar (Clique no item): 
            # /falaVitao 
            # /falaMatheus
            # /falaDiorgny
            # /falaGabriel
            # /falaGabs
            Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
            """
      bot.reply_to(mensagem, texto)


bot.polling()