
# coding: utf-8

# In[5]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[6]:


videogames = pd.read_csv('C:\\Users\\Thereza\\Desktop\\vgsales.csv')


# In[7]:


videogames.head(10)


# In[8]:


videogames.describe()


# In[9]:


videogames.dtypes


# In[10]:


videogames.shape


# In[11]:


videogames.columns = ['Ranking','Nome','Plataforma','Ano','Gênero','Editora','Vendas na América do Norte','Vendas nos EUA','Vendas no Japão','Outras vendas','Vendas Global']


# In[12]:


videogames.head(10)


# In[13]:


videogames[videogames['Ano'].isnull()].head()


# In[14]:


videogames['Plataforma'].value_counts()


# In[15]:


titulos_lancados = videogames['Plataforma'].value_counts()
titulos_lancados.plot()

videogames['Plataforma'].value_counts().plot


# In[16]:


#Criando um gráfico utilizando apenas uma linha de código
videogames['Plataforma'].value_counts().head(10).plot(kind='bar', figsize=(11,5), grid = False, rot=0, color = 'green')

#Enfeitando o gráfico. Abaixo definimos um título
plt.title('Os 10 videogames com mais títulos lançados')
plt.xlabel('Videogame')#nomeando o eixo x, onde ficam os vídeogames
plt.ylabel('Quantidade de Jogos lançados')#Nomeando o eixo y, onde fica a quantidade de jogos lançados
plt.show()#Exibindo o gráfico


# In[17]:


#Os 10 jogos mais vendidos da história
top10_vendidos = videogames[['Nome','Vendas Global']].head(20).set_index('Nome').sort_values('Vendas Global', ascending=True)
top10_vendidos.plot(kind='barh',figsize=(11,7),grid=False,color='darkred',legend=False)

plt.title('Os 20 jogos mais vendidos da história')
plt.xlabel('Total de vendas (em milhões de dólares)')
plt.show()


# In[18]:


crosstab_vg = pd.crosstab(videogames['Plataforma'], videogames['Gênero'])
crosstab_vg.head(20)


# In[19]:


crosstab_vg['Total'] = crosstab_vg.sum(axis=1)
crosstab_vg.head(20)


# In[20]:


top10_platforms = crosstab_vg[crosstab_vg['Total']>1000].sort_values('Total',ascending=False)
top10_final = top10_platforms.append(pd.DataFrame(top10_platforms.sum(),columns=['Total']).T, ignore_index=False)

sns.set(font_scale=1)
plt.figure(figsize=(18,9))
sns.heatmap(top10_final, annot=True, vmax = top10_final.loc[:'PS',:'Strategy'].values.max(),vmin = top10_final.loc[:,:'Strategy'].values.min(),fmt='d')
plt.xlabel('Gênero')
plt.ylabel('Console')
plt.title('QUANTIDADE DE TÍTULOS POR GÊNERO E CONSOLE')
plt.show()

