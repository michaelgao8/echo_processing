import pandas as pd
import mudicom
import gdcm
import numpy as np
import os

#%%
filename = "103_0004_103_4700_20171012_170102976/USm.1.2.840.113654.431393207.135434770377608990412005411501063110802.dcm"
study = mudicom.load(filename)

#%%
#data = study.read()
#element_name_list = [x.name for x in data]
#element_value_list = [x.value for x in data]
#%%
# Extract metadata for all of the echos that are present
#
#filecount = 0
#metadata = {}
#
#for name in os.listdir("D:/PROMISE_ECHO"):
#    for echo in os.listdir("D:/PROMISE_ECHO/" + name):
#        
#        study = mudicom.load("D:/PROMISE_ECHO/"+name+"/"+echo)
#        data = study.read()
#        element_name_list = [x.name for x in data]
#        element_value_list = [x.value for x in data]
#        
#        for i,v in enumerate(element_name_list):
#            # insert into the metadata dict
#            if v not in metadata:
#                metadata[v] = [None] * filecount
#                metadata[v].append(element_value_list[i])
#            else:
#                current_length = len(metadata[v])
#                metadata[v].append(element_value_list[i])
#        
#        filecount += 1
#            
#%%

num_files = 0
metadata = {}

for name in os.listdir("D:/PROMISE_ECHO"):
    for echo in os.listdir("D:/PROMISE_ECHO/" + name):
        num_files += 1
        study = mudicom.load("D:/PROMISE_ECHO/"+name+"/"+echo)
        data = study.read()
        element_name_list = [x.name for x in data]
        
        for col in element_name_list:
            if col not in metadata:
                metadata[col] = []
                
#%%
for key in metadata:
    metadata[key] = [None] * num_files

#%%
file_number = 0
for name in os.listdir("D:/PROMISE_ECHO"):
    for echo in os.listdir("D:/PROMISE_ECHO/" + name):
        
        study = mudicom.load("D:/PROMISE_ECHO/"+name+"/"+echo)
        data = study.read()
        element_name_list = [x.name for x in data]
        element_value_list = [x.value for x in data]
        
        for i,v in enumerate(element_name_list):
            metadata[v][file_number] = element_value_list[i]
        
        file_number += 1

#%%
import pandas as pd
final = pd.DataFrame.from_dict(metadata)
#%%

final.to_csv("echo_metadata.csv")