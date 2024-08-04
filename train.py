import spacy
from spacy.training import Example
import json
import random

# Load or create a spaCy model
nlp = spacy.blank("en")

# Load the dataset
with open("dataset_with_rupees.json", "r") as f:
    training_data = json.load(f)

# Prepare training data for spaCy
examples = []
for entry in training_data:
    text = entry["text"]
    annotations = {"entities": entry["entities"]}
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)

# Add the 'ner' component if it doesn't already exist
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add labels to the NER component
for label in ["QUANTITY", "AMOUNT", "CURRENCY"]:
    ner.add_label(label)

# Train the model
optimizer = nlp.begin_training()
for epoch in range(10):  # Number of epochs
    random.shuffle(examples)
    losses = {}
    for example in examples:
        nlp.update([example], drop=0.5, losses=losses)
    print(f"Epoch {epoch+1}: {losses}")

# Save the trained model
nlp.to_disk("./model")

print("Model trained and saved.")
