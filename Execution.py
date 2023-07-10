#!/usr/bin/env python
# coding: utf-8

# In[ ]:


experiment = Experiment()
experiment.append_configs(
    initial_state = initial_state,
    partial_state_update_blocks = partial_state_update_blocks,
    sim_configs = sim_config
)

