import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean, cityblock
from sklearn.metrics.pairwise import cosine_similarity
docs = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
]
query = "gold silver truck"
X = CountVectorizer(stop_words="english").fit_transform(docs + [query]).toarray()
docs, query = X[:-1], X[-1]
euclidean_dists = [euclidean(doc, query) for doc in docs]
manhattan_dists = [cityblock(doc, query) for doc in docs]
cosine_sims = cosine_similarity(docs, [query]).flatten()
top2_euclidean = np.argsort(euclidean_dists)[:2] + 1
top2_manhattan = np.argsort(manhattan_dists)[:2] + 1
top2_cosine = np.argsort(-cosine_sims)[:2] + 1
print("Euclidean:", euclidean_dists)
print("Manhattan:", manhattan_dists)
print("Cosine:", cosine_sims)
print("Top 2 Euclidean:", top2_euclidean)
print("Top 2 Manhattan:", top2_manhattan)
print("Top 2 Cosine:", top2_cosine)
