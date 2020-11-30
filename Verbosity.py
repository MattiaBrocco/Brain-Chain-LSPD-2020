#!/usr/bin/env python
# coding: utf-8

# In[4]:


def check_output (verbosity,output): 
    #This function defines 
    # :param verbosity: the level of verbosity required by the user
    if verbosity is True and output is True:
        print('artist:{}, title:{}'.format(artist,title)')
    elif verbosity is True and output is False:
        print('Try with another song')
    elif verbosity is False and output is True:
        print('artist:{}'.format(artist))
    elif verbosity is False and output is False:
        print('Something wrong, try with other parameters')
              
    return check_output
            
     
        

