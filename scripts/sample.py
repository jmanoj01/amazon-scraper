#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


URL = "https://www.amazon.com/s?k=playstation+5&crid=3BV45YDFQQE2G&sprefix=playstation+4%2Caps%2C269&ref=nb_sb_noss_2"


# In[6]:


# Headers for request
HEADERS = {'User-Agent': 'your_user_agent', 'Accept-Language': 'en-US, en;q=0.5'}


# In[7]:


# HTTP Request
webpage = requests.get(URL, headers=HEADERS)


# In[12]:


type(webpage.content)


# In[13]:


# Soup Object containiang all data
soup = BeautifulSoup(webpage.content, "html.parser")


# In[15]:


# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[36]:


links


# In[19]:


link = links[0].get('href')


# In[20]:


product_list = "https://amazon.com" + link


# In[21]:


product_list


# In[22]:


new_webpage = requests.get(product_list, headers=HEADERS)


# In[23]:


new_webpage


# In[24]:


# Soup Object containiang all data
new_soup = BeautifulSoup(new_webpage.content, "html.parser")


# In[25]:


new_soup


# In[28]:


new_soup.find("span", attrs={"id":'productTitle'}).text.strip()


# In[33]:


new_soup.find("span", attrs={"class":'a-price a-text-price a-size-medium'}).find("span", attrs={"class": "a-offscreen"}).text


# In[35]:


new_soup.find("span", attrs={"class":'a-icon-alt'}).text


# In[ ]:




