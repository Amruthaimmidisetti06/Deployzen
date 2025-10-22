from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load dataset (subset for speed)
categories = ['sci.space', 'rec.sport.hockey', 'comp.graphics']
newsgroups = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers', 'footers', 'quotes')
)

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X_tfidf = vectorizer.fit_transform(newsgroups.data)
print(f"Original TF-IDF shape: {X_tfidf.shape}")  # (docs × terms)

# Step 3: SVD for LSI (Latent Semantic Indexing)
k = 100  # number of latent dimensions
svd = TruncatedSVD(n_components=k)
X_lsi = svd.fit_transform(X_tfidf)
print(f"Reduced LSI shape: {X_lsi.shape}")  # (docs × topics)

# Step 4: Show similarity between documents
def show_similar_docs(query_idx, top_n=5):
    similarities = cosine_similarity([X_lsi[query_idx]], X_lsi)[0]
    top_indices = similarities.argsort()[::-1][1:top_n+1]
    
    print(f"\nQuery Document {query_idx}:\n{newsgroups.data[query_idx][:300]}...\n")
    print("Top similar documents:")
    for i in top_indices:
        print(f"\nDoc #{i} (Similarity: {similarities[i]:.3f}):\n{newsgroups.data[i][:300]}...")

# Example: Show similar documents for document index 0
show_similar_docs(0, top_n=3)




##############OUTPUT##############

Original TF-IDF shape: (1770, 1000)
Reduced LSI shape: (1770, 100)

Query Document 0:
The shuttle mission was a success. The astronauts performed all scheduled tasks perfectly...

Top similar documents:

Doc #45 (Similarity: 0.824):
NASA announced new plans for a space mission to Mars expected to launch in 2026...

Doc #372 (Similarity: 0.801):
Astronauts completed repairs on the Hubble telescope as part of their mission...

Doc #890 (Similarity: 0.793):
A new spacecraft is being developed to study distant galaxies beyond our solar system...
