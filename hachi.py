import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in tokens if w.isalnum() and w not in stop]

documents = {}
for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            documents[file] = preprocess(f.read())

print("Total documents loaded:", len(documents))

inverted_index = defaultdict(set)
for doc_id, words in documents.items():
    for w in set(words):
        inverted_index[w].add(doc_id)

print("Vocabulary Size:", len(inverted_index))

print("\nSample inverted index terms:")
for term in list(inverted_index)[:10]:
    print(f"{term}: {sorted(inverted_index[term])}")
