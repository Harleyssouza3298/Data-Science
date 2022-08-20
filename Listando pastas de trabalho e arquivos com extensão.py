#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Biblioteca 'os' para ter acesso as pastas do pc
import os
import pandas as pd


# In[32]:


# Identificando a pasta onde está rodando o programa python
folder = os.getcwd()


# In[79]:


fileToOpen = '\\Players.csv'


# In[78]:


# Concatenando a pasta com o arquivo desejado.
# Depois, abrindo o arquivo e armazenando em openFile
openFile = pd.read_csv(folder + fileToOpen)


# #### Usando o comando da biblioteca "os"  para listar os arquivos com a extensão ".xlsx" existentes na pasta de trabalho

# In[77]:


# O comando os.walk(folder) retorna uma tupla com:
#- (diretório) - O nome da pasta com o caminho completo (Ex: C:\\Users)
#- (subpastas) - O nome das subpastas que estão contidas nessa pasta
#- (arquivo) - O nome dos arquivos que estão contidos nessa pasta
#---------------------------------------------------------------------------
lista = [] # Criando uma lista para armazenar os arquivos desejados

for diretorio, subpastas, arquivos in os.walk(folder):
    for arquivo in arquivos:
        if (arquivo.endswith('.xlsx')): # Listando os arquivos tipos 'xlsx' que estão na pasta
            #print(diretorio)
            #print(subpastas)
            #print(arquivo)
            lista.append(arquivo.replace('.xlsx',''))
print(lista) # Lista dos arquivos ".xlsx" que estão na pasta mostrados sem o índice


# In[ ]:




