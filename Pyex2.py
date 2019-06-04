#!/usr/bin/env python
# coding: utf-8

# In[2]:


import feedparser
NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
entry = NewsFeed.entries[1]

print (entry.keys())


# In[ ]:




