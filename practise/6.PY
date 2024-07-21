import numpy  as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean,cityblock
from sklearn.metrics.pairwise import cosine_similarity


docs=[ "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
    
    
    
]

query="gold silver truck"

X=CountVectorizer(stop_words='english').fit_transform(docs,[query]).toarray()
docs,query=X[:-1],X[-1]
euclidean_distannce=[euclidean(doc,query)for doc in docs]
manhattan_distannce=[cityblock(doc,query)for doc in docs]
cosine_distannce=cosine_similarity(docs,[query]).flatten()
euclidian_distannce_top_2=np.argsort(euclidean_distannce)[:2]+1
manhattan_distannce_top_2=np.argsort(manhattan_distannce)[:2]+1
cosine_distance_top_2=np.argsort(-cosine_distannce)[:2]+1

print(euclidean_distannce)
print(manhattan_distannce)
print(cosine_distannce)
print(euclidian_distannce_top_2)
print(manhattan_distannce_top_2)
print(cosine_distance_top_2)