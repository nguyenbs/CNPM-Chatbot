# # -*- coding: utf-8 -*-
# from chatterbot import ChatBot


# # Uncomment the following lines to enable verbose logging
# # import logging
# # logging.basicConfig(level=logging.INFO)

# # Create a new instance of a ChatBot
# bot = ChatBot(
#     "Terminal",
#     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#     logic_adapters=[
#         "chatterbot.logic.MathematicalEvaluation",
#         "chatterbot.logic.TimeLogicAdapter",
#         "chatterbot.logic.BestMatch"
#     ],
#     input_adapter="chatterbot.input.TerminalAdapter",
#     output_adapter="chatterbot.output.TerminalAdapter",
#     database="../database.db"
# )

# print("Type something to begin...")

# # The following loop will execute each time the user enters input
# while True:
#     try:
#         # We pass None to this method because the parameter
#         # is not used by the TerminalAdapter
#         bot_input = bot.get_response(None)

#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break

# def process(input="hello"):
#     if input=="hello":
#         return "Cuoc doi van dep sao"
#     return "Đời vẫn đẹp"



from chatterbot import ChatBot
import GITTER
# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)
chatbot = ChatBot(
    'GitterBot',
    gitter_room=GITTER['ROOM'],
    gitter_api_token=GITTER['API_TOKEN'],
    gitter_only_respond_to_mentions=False,
    input_adapter='chatterbot.input.Gitter',
    output_adapter='chatterbot.output.Gitter',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.train('chatterbot.corpus.english')
# The following loop will execute each time the user enters input
while True:
    try:
        response = chatbot.get_response(None)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break