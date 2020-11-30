#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse

def parsing_input():
    #Parsing the input for our program.
    #This function requires two positional arguments
    
    parser = argparse.ArgumentParser()
    #positional arguments
    parser.add_argument("artist", help='the arstist of song you are searching for')
    parser.add_argument("title", help='the title of the song you are searching for')
    
    #optional arguments
    parser.add_argument("verbosity", help='increases verbosity of the program')
    args = parser.parse_args()
    return args

