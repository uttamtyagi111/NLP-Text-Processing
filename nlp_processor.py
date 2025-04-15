#This code is a simple NLP processor that uses spaCy to analyze text input by the user. 
#It cleans the text, tokenizes it, counts word frequencies, and extracts named entities. 
#The results are printed in a structured JSON format.
#The code includes error handling for loading the spaCy model and provides a sample text if no input is given.

import spacy
import json
import re
from collections import Counter

def process_text(text):
    # Load spaCy model
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # If model isn't installed, try downloading it
        print("Downloading spaCy model...")
        import subprocess
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    
    tokens = []
    for token in nlp(clean_text):
        if not token.is_stop and token.text.strip():
            tokens.append(token.text)
    
    word_freq = Counter(tokens)
    total_tokens = len(tokens)
    top_words = word_freq.most_common(5)
    
    
    entities = {}
    for ent in doc.ents:
        entity_type = ent.label_
        if entity_type not in entities:
            entities[entity_type] = []
        entities[entity_type].append(ent.text)
    
    filtered_entities = {}
    for entity_type in ['PERSON', 'ORG', 'GPE']:
        if entity_type in entities:
            filtered_entities[entity_type] = entities[entity_type]
    
    results = {
        "original_text": text,
        "cleaned_text": " ".join(tokens),
        "analysis": {
            "total_tokens": total_tokens,
            "top_words": {word: count for word, count in top_words}
        },
        "named_entities": filtered_entities
    }
    
    return results

def main():
    print("Enter a paragraph of text to analyze (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    text = "\n".join(lines)
    
    if not text.strip():
        text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976 in California. The company is headquartered in Cupertino and has revolutionized the technology industry with products like the iPhone and MacBook."
        print("\nUsing sample text since no input was provided:")
        print(text)
    
    results = process_text(text)
    
    print("\nResults:")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
    
    