import os
from LLM_tasks import utils
import json
from io import StringIO
from knowledgebase.kb1.SpaceEnvironmentAndOrbits.entries.slide_text import slide_text
from knowledgebase.Module import Module




class SpaceEnvironmentAndOrbits(Module):

    def __init__(self):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))
        self.slide_info = self.parse_entries()
        self.write_entries()


    def get_entries(self):
        entries = []
        entries.extend(self.slide_info)
        return entries

    def write_entries(self):
        with open(self.entries_file, 'w') as f:
            json.dump(self.get_entries(), f, indent=4)

    def parse_entries(self):
        entries = []
        for entry in slide_text:
            entries.append({
                'entry': entry
            })
        return entries

    ##############
    ### Search ###
    ##############

    def search(self, inputs):

        # 1. Get Entries
        all_entries = self.get_entries()
        search_strings = [self.get_entry_search_string(entry) for entry in all_entries]

        # 2. Search Entries
        query = inputs['query']
        results, entries = self.similarity.search(query, search_strings, top_n=self.num_results)
        top_entries = [all_entries[index] for score, index in results]
        return top_entries

    def get_entry_search_string(self, entry):
        return entry['entry']



if __name__ == '__main__':
    module = SpaceEnvironmentAndOrbits()
    query_block = {
        'type': 'query',
        'id': 'Q1',
        'class': 'SpaceEnvironmentAndOrbits',
        'query': 'How is x y z calculated?'
    }
    results = module.search(query_block)
    print(results)












