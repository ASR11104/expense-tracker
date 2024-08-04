# Problem

- send expenses in form of a text message 
- read this message 
- create insights from these messages

# Tasks

1. create an NLP model to read messages and extract relevant data - Spacy
    - Done

2. create a simple REST microservice for the model
    - expose an expoint to give text and get the entity
    - store this in a table with timestamp of message (enhance this with date inside message)
    - dockerise this microservice

3. Create a Github to store this
