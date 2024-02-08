import tiktoken
import os
import json
import sys
import re

# Supress Warnings
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)





def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return ''.join(lines)





def get_tokens(input):
    encoding = tiktoken.get_encoding("gpt2")
    tokens = encoding.encode(input)
    return tokens

def count_tokens(input):
    return len(get_tokens(input))




def parse_rules_file(rule_file):
    all_rules = []
    with open(rule_file, 'r') as f:
        content = f.read()
        blocks = content.split("-----")
        for block in blocks:
            properties = {}
            description = []
            code = []
            lines = block.strip().split('\n')
            state = -1
            for line in lines:
                if line.startswith('Name:'):
                    state = 0
                    properties['name'] = line[6:].strip()
                    continue
                elif line.startswith('Description:'):
                    state = 1
                    continue
                elif line.startswith('Code:'):
                    state = 2
                    continue
                if state == 1:
                    description.append(line)
                elif state == 2:
                    code.append(line)

            properties['description'] = "\n".join(description)
            code_text = "".join(code)
            code_text = re.sub(r'\s+', ' ', code_text)
            properties['code'] = code_text
            all_rules.append(properties)
    all_rules = [rule for rule in all_rules if 'name' in rule]
    return all_rules



def write_messages_to_file(messages, output_file):
    with open(output_file, 'w+') as f:
        for message in messages:
            f.write(f"{message['role'].capitalize()}:\n")
            f.write(f"{message['content']}\n\n")

def write_context_to_file(context, output_file):
    with open(output_file, 'w+') as f:
        f.write(context)









