from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")


def talk(msg):
    return chatbot.get_response(msg)

def train(in,res):
    chatbot.train([in,res])
    return "ok"