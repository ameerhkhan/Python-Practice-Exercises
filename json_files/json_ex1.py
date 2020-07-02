import json

# very common datatype
# json : Javascript Object Notation

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-222-4245",
            "emails": ["johnsmith@email.com", "john.smith@workmail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "888-092-1829",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# let's see how to load this data into python so we can work on it.

data = json.loads(people_string) # loads --> used to load a string.

print(data)
print(type(data))


# Basically python converts, (Encoder and Decoder 19.22)
# object --> Dictionary
# array --> list
# string --> str
# int --> int
# float --> float
# true --> True
# false --> False
# null --> None.

print(type(data['people'])) # --> returns a list object

# Now accessing,

for person in data['people']:
    print(person['name'])

# this was reading a json.

# ----------------------------------------------------

# Now we write

for person in data['people']:
    del(person['phone']) # --> Delete the key value pair containing phone number


# dumps --> write to a string
# dump --> write to a file.
new_string = json.dumps(data, indent=2, sort_keys=True) # no. of indents per {, sort_keys --> sort alphabetically
print(new_string)
