import requests
import json


class GraphqlClient:

    def __init__(self, user_info):
        self.user_info = user_info
        self.user_id = user_info.user.id
        self.hasura_url = 'http://127.0.0.1:6002/v1/graphql'

    def execute_query(self, query, variables=None):
        json_body = {'query': query}
        if variables is not None:
            json_body['variables'] = variables
        r = requests.post(self.hasura_url, json=json_body, headers={'X-Hasura-Admin-Secret': 'academy'})
        result = json.loads(r.text)
        # print('\n-------- Query Result --------')
        # print('----> URL:', self.hasura_url)
        # print('--> QUERY:', query)
        # pprint(result)
        # print('-------------------------\n')
        return result


    def insert_message(self, text, sender, more_info):
        query = '''
            mutation InsertMessage($user_id: Int!, $text: String!, $sender: String!, $more_info: String) {
                insert_Message_one(object: {user_id: $user_id, text: $text, sender: $sender, date: "now()", cleared: false, more_info: $more_info}) {
                    id
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
            'text': text,
            'sender': sender,
            'more_info': more_info
        }
        query_result = self.execute_query(query, variables)
        return query_result


    def get_ca_question_topics(self, question_id):
        query = '''
            query get_ca_question_topics($question_id: Int!) {
                question: Question_by_pk(id: $question_id) {
                    difficulty
                    discrimination
                    guessing
                    topics: Join__Question_Topics {
                        topic: Topic {
                            name
                            id
                        }
                    }
                }
            }
        '''
        variables = {
            "question_id": question_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["question"]

    def get_ca_graded_slide_questions(self, topic_id):
        query = '''
            query get_ca_graded_slide_questions($user_id: Int!, $topic_id: Int!) {
                question: Question(where: {Slides: {user_id: {_eq: $user_id}, graded: {_eq: true}, answered: {_eq: true}}, Join__Question_Topics: {topic_id: {_eq: $topic_id}}}) {
                    id
                    guessing
                    discrimination
                    difficulty
                    slides: Slides(where: {user_id: {_eq: $user_id}, graded: {_eq: true}, answered: {_eq: true}}) {
                        answered
                        correct
                    }
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
            'topic_id': topic_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["question"]

    def get_ca_graded_test_questions(self, topic_id):
        query = '''
            query get_ca_graded_test_questions($user_id: Int!, $topic_id: Int!) {
                question: Question(where: {TestQuestions: {Test: {user_id: {_eq: $user_id}}, answered: {_eq: true}}, Join__Question_Topics: {topic_id: {_eq: $topic_id}}}) {
                    id
                    guessing
                    discrimination
                    difficulty
                    test: TestQuestions(where: {answered: {_eq: true}}) {
                        correct
                    }
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
            'topic_id': topic_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["question"]

    def get_user_ability_parameters(self):
        query = '''
            query get_user_ability_parameters($user_id: Int!) {
                AbilityParameter(where: {user_id: {_eq: $user_id}, value: {_is_null: false}}, order_by: {value: asc}) {
                    Topic {
                        id
                        name
                    }
                    value
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["AbilityParameter"]

    def set_user_ability_parameters(self, topic_id, parameter):
        query = '''
            mutation set_ability_parameter($user_id: Int!, $topic_id: Int!, $parameter: float8!) {
                update_AbilityParameter(where: {user_id: {_eq: $user_id}, topic_id: {_eq: $topic_id}}, _set: {value: $parameter}) {
                    affected_rows
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
            'topic_id': topic_id,
            'parameter': parameter
        }
        query_result = self.execute_query(query, variables)
        return query_result

    def get_topic_questions(self, topic_id):
        query = '''
            query get_topic_questions($topic_id: Int!) {
                Question(where: {Join__Question_Topics: {topic_id: {_eq: $topic_id}}}) {
                    id
                    text
                    choices
                    topics: Join__Question_Topics {
                        topic_id
                    }
                    difficulty
                    discrimination
                    guessing
                }
            }
        '''
        variables = {
            'topic_id': topic_id,
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["Question"]

    def get_previously_asked_test_questions(self):
        query = '''
            query get_previously_asked_questions($user_id: Int!) {
                test: Test(where: {user_id: {_eq: $user_id}, in_progress: {_eq: true}}) {
                    questions: TestQuestions {
                        question_id
                    }
                    id
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["test"]

    def get_previously_asked_module_questions(self, topic_id):
        query = '''
            query get_previously_asked_module_questions($user_id: Int!, $topic_id: Int!) {
                slide: Slide(where: {user_id: {_eq: $user_id}, type: {_eq: "question"}, Question: {Join__Question_Topics: {topic_id: {_eq: $topic_id}}}, answered: {_eq: true}}) {
                    id
                    question: Question {
                        id
                        text
                    }
                }
            }
        '''
        variables = {
            'user_id': self.user_id,
            'topic_id': topic_id
        }
        query_result = self.execute_query(query, variables)
        return query_result["data"]["slide"]

    def get_learning_module_id(self, name):
        query = '''
            query get_learning_module_id($name: String = "") {
                module: LearningModule(where: {name: {_eq: $name}}) {
                    id
                    name
                }
            }
        '''
        variables = {
            "name": name
        }
        query_result = self.execute_query(query, variables)

        if 'data' in query_result and 'module' in query_result['data'] and len(query_result['data']['module']) > 0:
            return int(query_result['data']['module'][0]['id'])
        else:
            print('query not found!', query_result)
            return 0
