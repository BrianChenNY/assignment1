
# coding: utf-8

# In[3]:


# Question 1: A google search for the term "Tim Berners-Lee"

import requests
keyword = 'Tim Berners-Lee'
try:
    kw = {'q':keyword} 
    r = requests.get('http://www.google.com/search?',params=kw)
    r.raise_for_status()
    print(r.status_code)
    print((r.content[:500]))
    print((r.headers))
except:
    print('Fail to crawl')


# In[6]:


# Question2: a post request to a website that does not accept POST requests

import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://blog.sina.com.cn/twocold", data=payload)
print(r.status_code) 
#The 403 (Forbidden) status code indicates that the server understood the request but refuses to authorize it.
print((r.content[:500]))
print((r.headers))


# In[19]:


# Question3: A request to a URL that does not exist

import requests
url = 'http://www.google.com/szdasfaasdf'
r = requests.get(url)
print(r.status_code) 
print((r.content))
print((r.headers))

