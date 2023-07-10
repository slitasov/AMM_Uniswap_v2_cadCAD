#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
1) Firstly, we execute functions that determine which 
action will be performed in the system: 
Trade (then determine its conditions) 
or Liquidity (add/removal) 
2) Secondly, we execute the action that was determined
in the previous step
3) Thirdly, we calculate the price in the pool 
after the action
'''
partial_state_update_blocks = [
    {
        'policies': {
            'p_action': p_action
        },
        'variables': {
            'agent': s_agent,
            'token': s_token,
            'share': s_share,
            'value': s_value
        }
    },
    {
        'policies': {
            'Swaps': p_swapToAsset,
            'Liquidity': p_Liquidity
        },
        'variables': {
            'AMM': s_AMM,
            'timestep': s_timestep,
            'Trader': s_Trader,
            'LP': s_LP,
            'fee': s_fee
        }
    },
    {
        'policies': {},
        'variables': {
            'price': s_price,
        }
    },
]

