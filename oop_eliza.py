from pyDatalog import pyDatalog

class Program(pyDatalog.Mixin):
    pass

class Knowledge_base(pyDatalog.Mixin):
    pass

class Interlocutor(pyDatalog.Mixin):
    pass

class Dialog(pyDatalog.Mixin):
    def __init__(self, interlocutor_1, interlocutor_2):
        self.interlocutor_1 = interlocutor_1
        self.interlocutor_2 = interlocutor_2

class User(Interlocutor):
    def __init__(self, name):
        self.name = name

class Virtual_interlocutor(Program, Interlocutor):
    pass

class Psychotherapist():
    characterized_by = []

class Chat_bot(Virtual_interlocutor):
    pass

class Word_highlighter(pyDatalog.Mixin):
    pass

class Syntactical_analyzer(pyDatalog.Mixin):
    word_highlighter = Word_highlighter()

class Word_interpreter():
    pass

class Eliza(Chat_bot, Psychotherapist):
    syntactical_analyzer = Syntactical_analyzer()
    word_interpreter = Word_interpreter()


    #машина состояний
    def ask(self):
        pass

    #вызов из ask
    def __say__(self):
        pass

