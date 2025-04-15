#NLP Text Processing Script

#Overview
This Python script performs Natural Language Processing (NLP) tasks on English text, including text cleaning, tokenization, frequency analysis, and named entity recognition using spaCy.

#Features
Text cleaning (removing punctuation, converting to lowercase, removing stopwords)
Tokenization and word frequency analysis
Named entity extraction (PERSON, ORG, GPE)
JSON output of results

#Requirements
Python 3.12
spaCy library
English language model for spaCy (en_core_web_sm)

#Installation
#1. Install Python
Make sure you have Python installed. You can download it from python.org.
#2. Install Required Packages
bashpip install spacy
python -m spacy download en_core_web_sm

#Usage
#1. Basic Usage
Run the script:
bashpython nlp_processor.py
When prompted, enter or paste your text and press Enter twice when done.

#2. Example Input
Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University. The company is headquartered in Mountain View, California and has offices around the world.

#3. Example Output
json{
  "original_text": "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University. The company is headquartered in Mountain View, California and has offices around the world.",
  "cleaned_text": "google founded larry page sergey brin phd students stanford university company headquartered mountain view california offices world",
  "analysis": {
    "total_tokens": 17,
    "top_words": {
      "google": 1,
      "founded": 1,
      "larry": 1,
      "page": 1,
      "sergey": 1
    }
  },
  "named_entities": {
    "ORG": ["Google", "Stanford University"],
    "PERSON": ["Larry Page", "Sergey Brin"],
    "GPE": ["Mountain View", "California"]
  }
}

#How It Works
The script loads the spaCy English language model
It processes the input text to remove punctuation and convert to lowercase
It tokenizes the text and removes common stopwords (e.g., "the", "and", "of")
It calculates word frequencies and identifies the top 5 most frequent words
It extracts named entities using spaCy's named entity recognition
It returns all results in a structured format and prints them as JSON

#Customization
To extract different types of entities, modify the entity_type list in the process_text function
To show more than the top 5 words, change the parameter in word_freq.most_common(5)

#Troubleshooting
If you receive "ModuleNotFoundError", make sure spaCy is installed: pip install spacy
If you see "OSError" about missing the model, run: python -m spacy download en_core_web_sm

#License
This script is available under the MIT License.
