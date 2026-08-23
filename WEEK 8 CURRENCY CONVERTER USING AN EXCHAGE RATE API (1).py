#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('markdown', '', '# **WEEK 8 CURRENCY CONVERTER USING AN EXCHAGE RATE API**\n')


# In[19]:


import requests
print ("currency converter")
try:
    amount = float (input("enter amount:"))
    from_currency = input("currency from (example usd):")
    to_currency = input ("converter to(example pkr):")
    if amount < 0:
        print("amount connot be negative")
    elif from_currency =="" or to_currency =="":
        print("currency code cannot be empty ")
    elif from_currency == to_currency:
        print ("converter amount:" , amount, to_currency)
    else:
        url = f"https://apl.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"
        response = reqests.get(url, timeout=10)
        if response.status_code ==  200:
             data =response. json()
             exchange_rate =data["rate"]
             converted_amount =amount * exchange_rate
             print("conversion result")
             print("rate data:" , data["data"])
             print("1" , from_currency, "=", exchange_rate, to_currency)
             print(amount , from_currency, "=", round(converter_amount,2), to_currency)
        else: 

            print("currency code was not found")
except ValueError:
    print ("please enter a valid numeric amount")
except request.exceptions.RequsetException:
    print("Internet or API connection error")



# In[ ]:




