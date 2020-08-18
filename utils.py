#!/usr/bin/env python
# coding: utf-8

# In[3]:


import azureml
from azureml import Workspace
#get data from azureml

#@Author: Yogi
def get_data(workspace_id, authorization_token,experiment_token, node_id, port_name = 'Results dataset', data_type_id='GenericCSV'):
    ws = Workspace(
        workspace_id = workspace_id,
        authorization_token = authorization_token,
        endpoint = 'https://studioapi.azureml.net') #less likely to change
    experiment = ws.experiments[experiment_token]

    ds = experiment.get_intermediate_dataset(
        node_id = node_id,
        port_name = port_name,
        data_type_id = data_type_id)
    ds = ds.to_dataframe()
    return ds
