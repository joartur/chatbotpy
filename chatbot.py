from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar uma instância do chatbot
chatbot = ChatBot('MeuBot')

# Treinar o chatbot com o corpus padrão em inglês
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')

print("Olá! Eu sou o seu chatbot. Digite algo para começar a conversar.")

while True:
    try:
        user_input = input("Você: ")
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
