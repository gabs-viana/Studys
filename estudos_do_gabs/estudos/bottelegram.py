import telebot

CHAVE_API = "6761897525:AAE5R7wJFmObm6K_kZC3QUuL_UcEZc2Ujck"

bot = telebot.TeleBot(CHAVE_API)

def resposta_personalizada(mensagem):
    # Mapeia os IDs dos usuários para suas respostas personalizadas
    respostas = {
        5858174443: """Olá Gabsᶜʳᶠ! 🔴⚫ 
            Olá! 👋

Eu sou o MergeGuard, seu assistente de integração entre o GitLab e o Telegram! 🤖🔒

ℹ️ Como eu posso te ajudar?
➡️ Você pode usar os seguintes comandos para interagir comigo:

      /start - Inicia a interação com o MergeGuard e exibe esta mensagem de boas-vindas.

      📢 Além disso, estou aqui para manter você atualizado sobre eventos importantes do seu projeto no GitLab! Receba notificações sobre commits, merge requests, pipelines e muito mais diretamente no seu Telegram.

      Agora vamos lá, explorar todas as funcionalidades do MergeGuard juntos! 🚀 .        
        """,
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

@bot.message_handler(commands=["start"])
def falaVitao(mensagem):
      bot.reply_to(mensagem, "Olá, tudo beleza? ")
      bot.send_photo(mensagem.chat.id, "https://img.freepik.com/fotos-gratis/bela-foto-de-um-gatinho-branco-de-pelo-curto-britanico_181624-57681.jpg")



@bot.message_handler(func=resposta_personalizada)
def responder(mensagem):
      texto_personalizado = resposta_personalizada(mensagem)
      bot.reply_to(mensagem, texto_personalizado)

@bot.message_handler(func=lambda message: True)
def responder_padrao(mensagem):
      texto = """
            Olá! 👋

      Eu sou o MergeGuard, seu assistente de integração entre o GitLab e o Telegram! 🤖🔒

      ℹ️ Como eu posso te ajudar?
      ➡️ Você pode usar os seguintes comandos para interagir comigo:

      /start - Inicia a interação com o MergeGuard e exibe esta mensagem de boas-vindas.

      📢 Além disso, estou aqui para manter você atualizado sobre eventos importantes do seu projeto no GitLab! Receba notificações sobre commits, merge requests, pipelines e muito mais diretamente no seu Telegram.

      Agora vamos lá, explorar todas as funcionalidades do MergeGuard juntos! 🚀 .
            """
      bot.reply_to(mensagem, texto)


bot.polling()