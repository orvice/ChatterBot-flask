from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("deepThought",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="/data/database.db")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.chinese"
)

def talk(msg):
    return chatbot.get_response(msg)

def train(input,res):
    trainer = ListTrainer(chatbot)
    trainer.train([input,res])
    return "ok"