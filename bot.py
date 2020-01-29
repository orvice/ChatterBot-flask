from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("deepThought",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="/data/database.db")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")


def talk(msg):
    return chatbot.get_response(msg)

def train(input,res):
    chatbot.set_trainer(ListTrainer)
    chatbot.train([input,res])
    return "ok"