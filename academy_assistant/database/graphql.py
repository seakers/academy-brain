import requests
import json
import time











class GraphqlClient:

    def __init__(self, user_info):
        # GRAPHQL URL
        self.hasura_url = 'https://academy2.selva-research.com/graphql/v1/graphql'
        # self.hasura_url = 'http://127.0.0.1:6002/v1/graphql'
        self.user_info = user_info
        self.user_id = user_info.user.id
        # self.user_id = 1
        # self.user_id = 1


    def execute_query(self, query, variables=None):
        headers = {'X-Hasura-Admin-Secret': 'academy'}
        json_body = {'query': query }
        if variables is not None:
            json_body['variables'] = variables
        r = requests.post(self.hasura_url, json=json_body, headers=headers)
        result = json.loads(r.text)
        # print('\n-------- Query Result --------')
        # print('----> URL:', self.hasura_url)
        # print('--> QUERY:', query)
        # pprint(result)
        # print('-------------------------\n')
        return result


    def index_action(self, action):
        mutation = '''
        mutation MyMutation {
          insert_UserAction_one(object: {action: "''' + str(action) + '''", user_id: ''' + str(self.user_id) + ''', timestamp: "now()"}) {
            id
          }
        }
        '''
        self.execute_query(mutation)

    def get_textbooks(self):
        query = '''
        query TextBookQuery($user_id: Int!) {
            textbooks: TextBook(where: {user_id: {_eq: $user_id}}) {
                id
                title
                textbook_url
            }
        }'''
        variables = {
            "user_id": self.user_id
        }
        query_result = self.execute_query(query, variables)
        print("query result",query_result, self.user_id)
        return query_result["data"]["textbooks"]




    def get_learning_modules(self):
        query = '''
        query LearningModuleQuery($user_id: Int!) {
            modules: LearningModule(where: {Join__User_LearningModules: {user_id: {_eq: $user_id}}}) {
                id
                name
                icon
                join_info: Join__User_LearningModules(where: {user_id: {_eq: $user_id}}){
                    slide_idx
                }
                slides: Slides(where: {user_id: {_eq: $user_id}}, order_by: {idx: asc}) {
                    id
                    idx
                    correct
                    context
                    choice_id
                    answered
                    type
                    src
                    question_id
                    module_id
                    attempts
                    question: Question {
                        choices
                        difficulty
                        discrimination
                        explanation
                        guessing
                        id
                        text
                        topic_list: Join__Question_Topics {
                            topic: Topic {
                                id
                                name
                            }
                        }
                    }
                }
            }
        }'''
        variables = {
            "user_id": self.user_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["modules"]



    def get_ability_levels(self):
        query = '''
                query AbilityLevelQuery($user_id: Int!) {
                    topics: Topic(where: {AbilityParameters: {user_id: {_eq: $user_id}}}) {
                        id
                        name
                        ability_level: AbilityParameters {
                            value
                        }
                    }
                }'''
        variables = {
            "user_id": self.user_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["topics"]


    def get_test_history(self):
        query = '''
            query TestHistoryQuery($user_id: Int!) {
                tests: Test(where: {user_id: {_eq: $user_id}}, order_by: {date: asc}) {
                    questions: TestQuestions {
                        id
                        correct
                        choice_id
                        answered
                        test_id
                        question_id
                        question: Question {
                            text
                            id
                            guessing
                            explanation
                            discrimination
                            difficulty
                            choices
                            Join__Question_Topics {
                                Topic {
                                    name
                                }
                            }
                        }
                    }
                    type
                    num_questions
                    in_progress
                    id
                    duration
                    date
                    score
                }
            }'''
        variables = {
            "user_id": self.user_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["tests"]



    def get_messages(self):
        query = '''
        query MessageSubscription($user_id: Int!) {
            messages_db: Message(where: {user_id: {_eq: $user_id}, cleared: {_eq: false}}, order_by: {date: asc}) {
                id
                date
                sender
                text
                cleared
                more_info
            }
        }'''
        variables = {
            "user_id": self.user_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["messages_db"]

    
    ################ GET SLIDE IMAGE URL ####################
    def get_slide_info(self, module_id, idx):
        # query = '''
        #     query getSlideInfo($topic_id: Int!, $module_id: Int!, $slide_id: Int!) {
        #         slide_info(where: {topic_id: {_eq: $topic_id}, module_id: {_eq: $module_id}, slide_id: {_eq: $slide_id}}) {
        #             image_url
        #         }
        #     }
        # '''
        query = '''
            query getSlideInfo($module_id: Int!, $idx: Int!) {
                slide_info: Slide(where: {module_id: {_eq: $module_id}, idx: {_eq: $idx}}) {
                    image_url
                }
            }
        '''
        variables = {
            # 'topic_id': topic_id,
            'module_id': module_id,
            'idx': idx,
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["slide_info"]  
    
    def get_slide_explanation(self, module_id, slide_number):
        query = '''
            query GetSlideExplanation($module_id: Int!, $slide_number: Int!) {
                SlideExplanation(where: {module_id: {_eq: $module_id}, slide_number: {_eq: $slide_number}}) {
                    explanation
                }
            }
        '''
        variables = {
            "module_id": module_id,
            "slide_number": slide_number
        }
        result = self.execute_query(query, variables)
        print(result)
        explanations = result['data'].get('SlideExplanation', [])
        if explanations:
            print(explanations)
            return explanations[0]['explanation']
        return None

    def store_slide_explanation(self, module_id, slide_number, explanation):
        mutation = '''
            mutation InsertSlideExplanation($module_id: Int!, $slide_number: Int!, $explanation: String!) {
                insert_SlideExplanation_one(object: {module_id: $module_id, slide_number: $slide_number, explanation: $explanation}) {
                    id
                }
            }
        '''
        variables = {
            "module_id": module_id,
            "slide_number": slide_number,
            "explanation": explanation
        }
        result = self.execute_query(mutation, variables)
        return result['data'].get('insert_SlideExplanation_one', {}).get('id', None)


def test_graphql_client():
    user_info = {"id": 1, "username": "duser5"}
    graphql_client = GraphqlClient(user_info)

    module_id = 1
    slide_number = 1
    explanation_text = "This is a test explanation."

    # Store explanation
    stored_id = graphql_client.store_slide_explanation(module_id, slide_number, explanation_text)
    print(stored_id)
    if stored_id:
        print(f"Stored ID: {stored_id}")
    else:
        print("Failed to store explanation.")

    # Retrieve explanation
    retrieved = graphql_client.get_slide_explanation(module_id, slide_number)
    if retrieved:
        print(f"Retrieved Explanation: {retrieved}")
    else:
        print("No explanation found.")

if __name__ == "__main__":
    test_graphql_client()










