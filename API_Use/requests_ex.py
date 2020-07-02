#Request library allows us to make HTTP requests to get information from webpages.
#HTTP for Humans.

import requests

#r = requests.get('https://xkcd.com/353/')

#downloading an image using python
#q = requests.get('https://imgs.xkcd.com/comics/python.png')

#print(q.content) #gives bytes for a picture

#we have to open and save the above file using,
# with open('comic.png', 'wb') as f:
#     f.write(q.content)

#print(r)

#print(dir(r))
#print(r.text)



#Monitoring a website, For your own personal use or others

# print(q.status_code) 
# 200 --> Success
# 300 --> Redirect
# 400 --> Client Errors, when you try to get an unauthorized page
# 500 --> Server Error (site crashes)

# print(q.ok) #Returns True for 200 only.


# print(q.headers) #All headers containing info about the server, content type etc.

#We will use httpbin.org to check and test different queries.

#check the website out.

payload = {
    'page' : 2,
    'count' : 25
}

#x = requests.get('https://httpbin.org/get?page=2&count=25')
#or we can also use a dictionary to pass in parameters

#x = requests.get('https://httpbin.org/get', params=payload)

#print(x.text) #to get response.
#print(x.url)


#let's post something.
payload_post = {
    'username' : 'corey',
    'password' : 'testing'
}
#w = requests.post('https://httpbin.org/post', data = payload_post)
#select payload according to forms.

#print(w.text)
#print(w.json())
#creates a python dictionary to capture data in json
#w_dict = w.json()

#print(w_dict['form'])

#For put request use request.put


#For log ins,
#request can do that.

#can use AUTH route to perform log ins.

#t = requests.get('https://httpbin.org/basic-auth/corey/testing', auth = ('corey', 'testing'))

#print(t.text) #returns authentication credentials.

#set a timeout in case you can't get any response which just means trouble.

try:
    v = requests.get('https://httpbin.org/delay/6', timeout=3)
except:
    TimeoutError
    print('timeout')
finally:
    print('We went there and gave you the response.')

#print(v)