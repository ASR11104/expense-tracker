import spacy
import threading
import sys
import os

def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

    return get_instance

@singleton
class NLPModel:
    model = None
    def __init__(self):
        pwd = os.path.dirname(__file__)
        model_path = os.path.join(pwd, 'nlpmodel')
        nlp_trained = spacy.load(model_path)
        self.model = nlp_trained
    
    def get_attributes(self, text):
        doc = self.model(text)
        return doc.ents