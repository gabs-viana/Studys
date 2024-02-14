import telebot

CHAVE_API = "6761897525:AAE5R7wJFmObm6K_kZC3QUuL_UcEZc2Ujck"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["falaVitao"])
def falaVitao(mensagem):
      bot.reply_to(mensagem, "E ai, firmeza Vitao? monstro sagrado, preceptor do acopalipse")
      bot.send_photo(mensagem.chat.id, "https://img.freepik.com/fotos-gratis/bela-foto-de-um-gatinho-branco-de-pelo-curto-britanico_181624-57681.jpg")

@bot.message_handler(commands=["falaMatheus"])
def falaVitao(mensagem):
      pass

@bot.message_handler(commands=["falaDiorgny"])
def falaVitao(mensagem):
      pass

@bot.message_handler(commands=["falaGabriel"])
def falaVitao(mensagem):
      pass
    
@bot.message_handler(commands=["falaGabs"])
def falaVitao(mensagem):
      print(mensagem)
      bot.reply_to(mensagem, "Xora Gabs, maluco criador deste botzão")
      bot.send_photo(mensagem.chat.id, "https://logodownload.org/wp-content/uploads/2016/09/flamengo-logo-0.png") #Esta linha precisa de revisão, desejo adicionar uma imagem logo após a mensagem


def verificar(mensagem):
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item): 
      /falaVitao 
      /falaMatheus
      /falaDiorgny
      /falaGabriel
      /falaGabs
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    bot.reply_to(mensagem, texto)


bot.polling()