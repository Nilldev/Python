#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk
import smtplib
from email.message import EmailMessage


ativos = ["^BVSP","BRL=X"]

hoje = datetime.datetime.now()
um_ano_atras = hoje- datetime.timedelta(days=365)

dados_mercado = yf.download(ativos,um_ano_atras, hoje)
display (dados_mercado)


# In[22]:


dados_fechamento = dados_mercado["Adj Close"]
dados_fechamento.columns = ["Dolar","ibovespa"]


# In[26]:



dados_fechamento=dados_fechamento.dropna()
dados_fechamento.head(50)


# In[28]:


dados_fechamento.plot()


# In[ ]:




