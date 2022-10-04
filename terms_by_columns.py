import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

path = r'E:\koodit\Git\Master data_työversio_din_iso_modified.csv'

data = pd.read_csv(path)

data_old = data['Item description (local 1)']
data_new = data['Tekstinsyotto']

text = " ".join(review for review in data_new.astype(str))
text = text.split()

for i in text:
    i = i.strip()
    if len(i) == 0:
        text.pop(text.index(i))

text_len = len(text)
data['words'] = ''

for i in range(text_len):
#        if i == 50:
#                break

        data['words'][i] = text[i]
df1 = pd.DataFrame(data['words'])

df1['count'] = 1
df1 = df1.groupby(['words']).count()['count']
df1 = df1.reset_index()

new_data = df1.set_index('words').to_dict()['count']
#print(new_data)
df1.to_csv(r'E:\koodit\Git\most_used_terms_in_column.csv')