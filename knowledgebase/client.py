import os
import importlib.util
import sys


from knowledgebase.kb1 import modules as kb1_modules


class KnowledgebaseClient:

    def __init__(self):
        self.knowledgebase_dir = os.path.dirname(os.path.abspath(__file__))
        self.modules = kb1_modules

    """ Query
     - Input: query block
     - Output: formatted string containing matched context entries

    Notes
    1. Each Module class has a search method to call

    """

    def query(self, query_block):
        # print('Query Block:', query_block)

        # 1. Get Module
        if query_block['class'] not in self.modules.keys():
            print('Class not found:', query_block['class'])
            return {'results': []}
        module = self.modules[query_block['class']]

        # 2. Search Module
        results = module.search(query_block)
        query_block['results'] = results

        # 3. Format Result
        if query_block['class'] == 'Designs':
            query_block['formatted_results'] = results
        else:
            query_block['formatted_results'] = [module.get_entry_search_string(result) for result in results]

        return query_block


if __name__ == '__main__':
    client = KnowledgebaseClient()
    query_block = {
        'type': 'query',
        'id': 'Q1',
        'class': 'SpaceMissionOverview',
        'query': 'Does this entry describe a scatterometer? (yes/no)'
    }
    response = client.query(query_block)
    print('Response:', response)












