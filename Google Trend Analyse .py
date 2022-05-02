#!/usr/bin/env python
# coding: utf-8

# ### Google Trends Analyse

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[12]:


# pytrends api için promta yükleme işlemi yapılması gerekiyor .
#*** conda install pytrends***
from pytrends.request import TrendReq


# In[13]:


pytrends=TrendReq()


# In[14]:


#keyword listesi oluşturuyoruz
EList=["Trendyol","Hepsiburada","n11","çiçeksepeti"]


# In[ ]:


# payload yapıyoruz
pytrends.build_payload(EList,cat=None,timeframe='2015-01-01 2022-05-01',geo='TR')


# In[16]:


# zamana göre değişim için
data=pytrends.interest_over_time()


# In[17]:


# oluşturduğumuz dataframe i excel dosyası olarak kaydedelim
data.to_excel('trendsfile.xls')


# In[18]:


# zamana bağlı grafiğimizi oluşturalım
plt.figure(figsize=(13,6))
plt.plot(data.index,data.Trendyol,"k-")
plt.plot(data.index,data.Hepsiburada,"b*")
plt.plot(data.index,data.n11,"r-")
plt.plot(data.index,data.çiçeksepeti,"g*")

plt.legend(["Trendyol","Hepsiburada","n11","çiçeksepeti"])
plt.show()


# ** 2015 yılından itibaren e ticaret sitelerinin google trend analizini yaptık n11 ve hepsiburada 2020 yılından itibaren düşüş eğilimindeyken 2019 itibariyle trendyol genel olarak yükseliş trendindedir diyebiliriz

# In[ ]:




