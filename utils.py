#!/usr/bin/env python
# coding: utf-8

# In[3]:


import azureml
from azureml import Workspace
import pandas as pd
import os
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

def load_data():
    if os.path.isfile('data/maint.csv'):
        maint_df = pd.read_csv('data/maint.csv', index_col='Unnamed: 0')
    else:
        maint_df = utils.get_data(workspace_id, authorization_token, experiment_token, maint_node_id)
        maint_df.to_csv('data/maint.csv')

    if os.path.isfile('data/machines.csv'):
        machines_df = pd.read_csv('data/machines.csv', index_col='Unnamed: 0')
    else:
        machines_df = utils.get_data(workspace_id, authorization_token, experiment_token, machines_node_id)
        machines_df.to_csv('data/machines.csv')

    if os.path.isfile('data/telemetry.csv'):
        telemetry_df = pd.read_csv('data/telemetry.csv', index_col='Unnamed: 0')
    else:
        telemetry_df = utils.get_data(workspace_id, authorization_token, experiment_token, telemetry_node_id)
        telemetry_df.to_csv('data/telemetry.csv')

    if os.path.isfile('data/error.csv'):
        error_df = pd.read_csv('data/error.csv', index_col='Unnamed: 0')
    else:
        error_df = utils.get_data(workspace_id, authorization_token, experiment_token, error_node_id)
        error_df.to_csv('data/error.csv')

    if os.path.isfile('data/failures.csv'):
        failures_df = pd.read_csv('data/failures.csv', index_col='Unnamed: 0')
    else:
        failures_df = utils.get_data(workspace_id, authorization_token, experiment_token, failures_node_id)
        failures_df.to_csv('data/failures.csv')
    return machines_df, maint_df, telemetry_df, error_df, failures_df
