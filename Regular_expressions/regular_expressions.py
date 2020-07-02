import re
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

sentence = 'Start a sentence and then bring it to an end'
text_to_search = '''
Mr. Schafer
Mr. Smith
Ms Dacis
Mrs. Robinsion
Mr. T
'''

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w+')

matches = pattern.finditer(text_to_search)
#can also use,
matches_list = pattern.findall(text_to_search)
#or
mat = pattern.match(text_to_search)
print(mat)

for match in matches:
    print(match)
    
pattern_sen = re.compile(r'sentence')

matchese = pattern_sen.search(sentence)
print(matchese)



#HOW TO USE FLAGS?
#Suppose we want to match a word but match it regardless of upper or lowercase or even MIX.

#in regular expressions, use use (r'[Ss][Tt][Aa]')

#we can use flag such that above redundancy is removed

pattern_flag = re.compile(r'start', re.IGNORECASE) #can also use 'I' instead of full IGNORECASE

#There are other flags as well. So read about them when you'd like.

match_flag = pattern_flag.search(sentence)
print(match_flag)