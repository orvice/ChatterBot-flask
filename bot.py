from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("deepThought",storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    database="/data/database.json")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")


def talk(msg):
    return chatbot.get_response(msg)

def train(input,res):
    chatbot.set_trainer(ListTrainer)
    chatbot.train([input,res])
    return "ok"