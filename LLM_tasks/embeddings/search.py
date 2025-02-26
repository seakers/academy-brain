import os
import importlib.util
import sys
import pickle
import tiktoken
import matplotlib.pyplot as plt

from nltk import tokenize as nlktokenize

import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster


import openai
openai.api_key = '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'
# openai.api_key = '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'


def num_tokens(input):
    encoding = tiktoken.get_encoding("gpt2")
    num_tokens = len(encoding.encode(input))
    return num_tokens

def get_tokens(input):
    encoding = tiktoken.get_encoding("gpt2")
    tokens = encoding.encode(input)
    return tokens

def vector_similarity(x, y):
    """
    Returns the similarity between two vectors.
    - Because OpenAI Embeddings are normalized to length 1, the cosine similarity is the same as the dot product.
    """
    return np.dot(np.array(x), np.array(y))


class SimilaritySearch:

    def __init__(self):
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        # self.root_dir = '/Users/mahima/Documents/daphne-academy/academy-brain/LLM_tasks/embeddings'
        self.embedding_model = 'text-embedding-ada-002'
        self.embedding_path = os.path.join(self.root_dir, 'embeddings.pickle')
        # self.embedding_path = "embeddings.pickle"
        self.embeddings = {}
        self.read_embedding_store()

    def search(self, query, search_list, top_n=10):
        # embedding_dict = self.context_manager.get_embedding_dict()
        embedding_dict = self.embed_list_batch(search_list)
        query_embedding = self.embed_text(query)
        context_similarities = sorted([
            (vector_similarity(query_embedding, embedded_context), idx) for idx, embedded_context in
            enumerate(embedding_dict)
        ], reverse=True)
        if len(context_similarities) < top_n:
            top_n = len(context_similarities)

        sorted_list = [search_list[i[1]] for i in context_similarities]
        return context_similarities[:top_n], sorted_list[:top_n]

    def read_embedding_store(self):
        if os.path.exists(self.embedding_path):
            self.embeddings = pickle.load(open(self.embedding_path, 'rb'))
        else:
            with open(self.embedding_path, 'wb') as f:
                pickle.dump(self.embeddings, f)

    def write_embedding_store(self):
        with open(self.embedding_path, 'wb') as f:
            pickle.dump(self.embeddings, f)

    # --------------------- #
    # --- Embed Context --- #
    # --------------------- #

    def embed_text(self, text):
        if text in self.embeddings.keys():
            return self.embeddings[text]
        result = openai.Embedding.create(model=self.embedding_model, input=text)
        self.embeddings[text] = result["data"][0]["embedding"]
        self.write_embedding_store()
        return self.embeddings[text]

    def embed_list_batch(self, text_list):
        if all(text in self.embeddings for text in text_list):
            # print('All texts found in pre-cache')
            return [self.embeddings[text] for text in text_list]

        embedding_list = []
        temp_batch = []
        batch_cnt = 1
        for idx, value in enumerate(text_list):
            if value == '':
                embedding_list.append(None)
                continue
            temp_batch.append(value)
            if len(temp_batch) == 1000:
                print('--> BATCH:', batch_cnt, '(1000)')
                batch_result = self.embed_list(temp_batch)
                embedding_list += batch_result
                temp_batch = []
                batch_cnt += 1
        if len(temp_batch) > 0:
            batch_result = self.embed_list(temp_batch)
            embedding_list += batch_result
        self.write_embedding_store()
        return embedding_list



    def embed_list(self, text_list):
        embeddings = {}
        not_found = []

        # Iterate over the text_list
        for text in text_list:
            # If the text is in the embeddings dictionary, retrieve it
            if text in self.embeddings:
                embeddings[text] = self.embeddings[text]
            else:
                # If the text is not in the embeddings dictionary, add it to the not_found list
                print('New text found: ', text)
                not_found.append(text)

        # If there are texts not found in the cache, generate embeddings for them
        if not_found:
            result = openai.Embedding.create(model=self.embedding_model, input=not_found)
            for text, res in zip(not_found, result['data']):
                embedding = res["embedding"]
                # Store the new embedding in the cache and the return dictionary
                self.embeddings[text] = embedding
                embeddings[text] = embedding
        else:
            print('All texts found in cache')

        # Return the embeddings in the order they were requested
        return [embeddings[text] for text in text_list]

    # def group_embeddings_kmeans(self, embedding_list, num_clusters=2, plot=False):
    #     embedded_strings = np.array(embedding_list)
    #     if plot:
    #         inertias = []
    #         K = range(1, 15)
    #         for k in K:
    #             kmeans = KMeans(n_clusters=k, random_state=0).fit(embedded_strings)
    #             inertias.append(kmeans.inertia_)
    #         plt.plot(K, inertias, 'bx-')
    #         plt.xlabel('k')
    #         plt.ylabel('Sum_of_squared_distances')
    #         plt.title('Elbow Method For Optimal k')
    #         plt.show()
    #     kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(embedded_strings)
    #     return kmeans.labels_

    def group_embeddings_hierarchical(self, embedding_list, threshold=3.9):
        # 3.4 / 3.9 is pretty good at identifying nonsense for ~150 pages
        embedded_strings = np.array(embedding_list)
        Z = linkage(embedded_strings, method='ward')
        labels = fcluster(Z, threshold, criterion='distance')
        return labels


similarity = SimilaritySearch()




if __name__ == '__main__':
    query = "In-depth study of Jupiter's atmosphere and magnetosphere using a specially designed spacecraft"

    # Set of short strings describing different space missions
    descriptions = [
        "Mission to land a rover on Mars and search for signs of past life",
        "Satellite designed to study Earth's climate and weather patterns",
        "Spacecraft sent to explore the rings and moons of Saturn",
        "Mission to capture and study high resolution images of distant galaxies using a telescope",
        "Asteroid sampling mission aiming to return samples back to Earth",
        "Designing a spacecraft to make detailed study of Jupiter's atmosphere and magnetic field",
        "Mission to observe the Sun and study its influence on Earth's climate",
        "Sending a probe to Venus to study its atmosphere and surface",
        "Lunar mission aiming to establish a research base on the moon"
    ]

    query = "satellite with lidar instrument"
    descriptions = [
        "Earth observing mission studying soil moisture",
        "Communications constellation with optical instruments",
        "Mission measuring atmospheric carbon dioxide",
    ]





    query = "Space exploration is fascinating."
    descriptions = [
        "The quick brown fox jumps over the lazy dog.",
        "Football is a popular sport in the United States.",
        "I enjoy reading books on history and philosophy.",
        "OpenAI has developed a powerful AI model called GPT-3.",
        "Astronomy is the study of the universe beyond Earth's atmosphere.",
        "Python is a versatile programming language widely used in data science.",
        "Cats are independent animals, while dogs are more social.",
        "The Eiffel Tower is a landmark in Paris, France.",
    ]

    result, items = similarity.search(query, descriptions, top_n=len(descriptions))

    sorted_output = sorted(result, key=lambda x: x[0], reverse=True)
    sorted_descriptions = [descriptions[i[1]] for i in sorted_output]
    similarity_scores = [i[0] for i in sorted_output]

    plt.figure(figsize=(10, 8))
    bars = plt.barh(range(len(sorted_descriptions)), similarity_scores, color='skyblue')
    plt.yticks(range(len(sorted_descriptions)), [''] * len(sorted_descriptions))  # remove y tick labels
    plt.xlabel('Similarity Score')
    plt.title('Similarity of Different Space Missions to Query')

    # Add mission descriptions near the left y-axis
    for i, description in enumerate(sorted_descriptions):
        plt.text(0.01, i,
                 description,
                 va='center', color='black')

    plt.gca().invert_yaxis()  # Highest score at the top
    plt.show()





