#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string

def generate_password(length):
    # Generate a random selection of letters, digits, and punctuation
    password_characters = string.ascii_letters + string.digits + string.punctuation
    # Use the random module to shuffle the characters
    password = ''.join(random.sample(password_characters, length))
    return password

# Generate a password with 20 characters
password = generate_password(20)
print(password)


# In[ ]:





# In[ ]:




