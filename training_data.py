import json
import random

# Function to generate random amounts
def generate_random_amount():
    return random.randint(10, 10000)  # Random amounts between 10 and 10000

# Function to generate random quantities
def generate_random_quantity():
    return random.randint(1, 20)  # Random quantities between 1 and 20

# Sample sentences
samples = [
    "bought {quantity} items for {amount} rupees",
    "spent {amount} rupees on {item}",
    "paid {amount} rupees for {service}",
    "purchased {quantity} units for {amount} rupees",
    "spent {amount} rupees on groceries",
    "paid {amount} rupees for dinner",
    "bought {item} worth {amount} rupees",
    "spent {amount} rupees at the store",
    "bought {quantity} pieces of {item} for {amount} rupees",
    "paid {amount} rupees for a new {item}",
]

# List to hold the generated data
data = []

# Generate 1000 entries
for _ in range(1000):
    sentence_template = random.choice(samples)
    amount = generate_random_amount()
    quantity = generate_random_quantity()
    item = random.choice(["book", "shirt", "laptop", "phone", "pen", "notebook", "camera", "watch"])
    service = random.choice(["service", "cleaning", "subscription", "repair"])

    sentence = sentence_template.format(
        quantity=quantity,
        amount=amount,
        item=item,
        service=service
    )

    entities = []
    if "quantity" in sentence_template:
        start = sentence.find(str(quantity))
        end = start + len(str(quantity))
        entities.append([start, end, "QUANTITY"])
    if "amount" in sentence_template:
        start = sentence.find(str(amount))
        end = start + len(str(amount))
        entities.append([start, end, "AMOUNT"])
    if "rupees" in sentence_template:
        start = sentence.find("rupees")
        end = start + len("rupees")
        entities.append([start, end, "CURRENCY"])

    data.append({
        "text": sentence,
        "entities": entities
    })

# Save dataset to a JSON file
with open("dataset_with_rupees.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dataset with 1000 entries saved to dataset_with_rupees.json")
