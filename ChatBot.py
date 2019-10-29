from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create instance of chatbot
chatbot = ChatBot('TestBot',
                  logic_adapters=[
                      'chatterbot.logic.BestMatch',
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.TimeLogicAdapter'
                  ]
                  )

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.conversations"
)
# trainer = ListTrainer(chatbot)
# training_data = open('textfile path','r').readlines()
# trainer.train(training_data)

print('Type something to begin...')

# Infinite loop to execute whenever user enters an input. Break loop using CTRL-C or CTRL-D
while True:
    try:
        user_input = input('You: ')
        bot_response = chatbot.get_response(user_input)
        print('Bot: ', bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
