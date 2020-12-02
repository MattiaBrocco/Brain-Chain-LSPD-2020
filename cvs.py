#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Per creare e scrivere in un file CSV
#per creare un writer di file dinamico è necessario importare un pacchetto import csv ,
#quindi creare un'istanza del file con riferimento al file Ex: - con open ("D: \ sample.csv", "w", newline = "" ) 
#come file_writer


import csv 

with open("D:\\sample.csv","w",newline="") as file_writer: #qui se il file non esiste con la directory dei file menzionata, Python creerà uno stesso file nella directory specificata e "w" rappresenta la scrittura

    fields=["Artist","Title"]#creiamo alcuni nomi di campi (nomi di colonna) usando la lista

    writer=csv.DictWriter(file_writer,fieldnames=fields)# qui utilizzando il writer del dizionario e assegnando i nomi delle colonne
    #per scrivere i nomi delle colonne in CSV utilizziamo il writer. 
    writer.writeheader()

    writer.writerow({"Artist":"Lady Gaga","Title":"Paparazzi"})
    
print(row['artist'], row['title'])

