import json
import os

# Java Object Notion.

# loading a file.
with open('Q:\Hamza\Python\Python_new_exercises\json_files\states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

# let's write some object to the file.

for state in data['states']:
    del state['area_code']

os.chdir('Q:/Hamza/Python/Python_new_exercises/json_files')

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)