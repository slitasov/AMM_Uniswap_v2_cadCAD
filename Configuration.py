#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sim_config = config_sim({
    "N": 1, # the number of times we'll run the simulation ("Monte Carlo runs")
    "T": range(100), # the number of timesteps the simulation will run for
    "M": system_params # the parameters of the system
})

