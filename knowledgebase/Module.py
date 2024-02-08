import os
import importlib.util
import sys
import json

from LLM_tasks.embeddings.search import similarity

class Module:

    def __init__(self, module_dir):
        self.local_dir = module_dir
        self.entries_dir = os.path.join(self.local_dir, 'entries')
        self.entries_file = os.path.join(self.local_dir, 'entries.json')
        self.classifications_file = os.path.join(self.local_dir, 'classifications.json')

        # Similarity Search
        self.similarity = similarity
        self.num_results = 20

        # Entry Classifier
        self.entry_classifier = None


    """ Search
     - Input: query block
     - Output: list of entries
    """
    def search(self, inputs):
        return []

    """ Format
     - Input: list of entries
     - Output: formatted string containing matched context entries
    """
    def format(self, inputs):
        return ''


    """ Classify
     - Input: list of entries, query block
     - Output: list of matched entries, list of unmatched entries
    """
    def classify(self, inputs, query_block):
        return [], []

    def write_classified_entries(self, classified_entries, unclassified_entries):
        with open(self.classifications_file, 'w') as f:
            json.dump({'classified': classified_entries, 'unclassified': unclassified_entries}, f, indent=4)