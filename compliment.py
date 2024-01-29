#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def generate_compliment(name):
    compliments = [
        f"You're amazing, {name}!",
        f"Your positivity is infectious, {name}!",
        f"You're doing a great job, {name}!",
        f"The world is a better place with you in it, {name}!",
        f"{name}, you're a rockstar!",
    ]

    # Generate a random compliment
    compliment = random.choice(compliments)
    
    return compliment

# Replace "Your Name" with your actual name
your_name = "Your Name"
print(generate_compliment(your_name))

