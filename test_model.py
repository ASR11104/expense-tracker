import spacy

nlp_trained = spacy.load("./model")
doc = nlp_trained("bought a mac for 68k")
for ent in doc.ents:
    print(ent.text, ent.label_)