import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Define the text to be processed
text = "50 dollar"

# Process the text with the spaCy model
doc = nlp(text)

# Print the entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)
