#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
- The State Update Functions is the cell allow to 
randomize action between Trading and Liquidity provision/removal
on each timestep
- The functions are executed in the first subset
after execution of functions other blocks are updated
based on executions of these functions
'''

def s_price(system_params, substep, state_history, previous_state, policy_input):
    
    updated_price = previous_state['AMM']['A2'] / previous_state['AMM']['A1'] 

    return "price", updated_price


def s_agent(system_params, substep, state_history, previous_state, policy_input):
    
    updated_agent = policy_input['agent']

    return "agent", updated_agent


def s_token(system_params, substep, state_history, previous_state, policy_input):
    
    updated_token = policy_input['token']

    return "token", updated_token

def s_share(system_params, substep, state_history, previous_state, policy_input):
    
    updated_share = policy_input['share']

    return "share", updated_share

def s_timestep(system_params, substep, state_history, previous_state, policy_input):
    
    updated_timestep = previous_state["timestep"] + 1

    return "timestep", updated_timestep

def s_value(system_params, substep, state_history, previous_state, policy_input):
    
    updated_value = policy_input['value']

    return "value", updated_value


# In[6]:


'''
The function updates collected fees 
on each timestep
'''

def s_fee(system_params, substep, state_history, previous_state, policy_input):
    
    fee_A1 = previous_state['fee']['A1']
    fee_A2 = previous_state['fee']['A2']
    
    collected_fee_A1 = 0
    collected_fee_A2 = 0
    
    if previous_state["token"] == "A1" and previous_state["agent"] == "Trader":
        collected_fee_A2 = previous_state["value"] * system_params['fee']
        
    elif previous_state["token"] == "A2" and previous_state["agent"] == "Trader":
        collected_fee_A1 = previous_state["value"] * system_params['fee']

    return "fee", {"A1": fee_A1 + collected_fee_A1  , "A2": fee_A2 + collected_fee_A2}


# In[7]:


'''
The function updates the AMM state
on each timestep
'''

def s_AMM(system_params, substep, state_history, previous_state, policy_input):
    
    add_to_AMM_A1 = policy_input['add_to_AMM_A1']
    add_to_AMM_A2 = policy_input['add_to_AMM_A2']
    add_to_AMM_s = policy_input['add_to_AMM_s']
    
    
    # State Variables
    AMM_A1 = previous_state["AMM"]["A1"]
    AMM_A2 = previous_state["AMM"]["A2"]
    AMM_s =  previous_state["AMM"]["s"]
    

    # Calculate updated states
    updated_AMM_A1 = AMM_A1 + add_to_AMM_A1
    updated_AMM_A2 = AMM_A2 + add_to_AMM_A2
    updated_AMM_s = AMM_s + add_to_AMM_s
    

    return "AMM", {"A1":updated_AMM_A1,"A2":updated_AMM_A2,"s":updated_AMM_s}


# In[8]:


'''
The function updates the Trader balance state
on each timestep
'''

def s_Trader(system_params, substep, state_history, previous_state, policy_input):
    
    add_to_Trader_A1 = policy_input['add_to_Trader_A1']
    add_to_Trader_A2 = policy_input['add_to_Trader_A2']
    
    
    # State Variables
    Trader_A1 = previous_state["Trader"]["A1"]
    Trader_A2 = previous_state["Trader"]["A2"]
    

    # Calculate updated states
    updated_Trader_A1 = Trader_A1 + add_to_Trader_A1
    updated_Trader_A2 = Trader_A2 + add_to_Trader_A2
    

    return "Trader", {"A1":updated_Trader_A1,"A2":updated_Trader_A2,"s":100}


# In[9]:


'''
The function updates the LP balance state
on each timestep
'''

def s_LP(system_params, substep, state_history, previous_state, policy_input):
    
    add_to_LP_A1 = policy_input['add_to_LP_A1']
    add_to_LP_A2 = policy_input['add_to_LP_A2']
    add_to_LP_s = policy_input['add_to_LP_s']
    
    
    # State Variables
    LP_A1 = previous_state["LP"]["A1"]
    LP_A2 = previous_state["LP"]["A2"]
    LP_s =  previous_state["LP"]["s"]
    

    # Calculate updated states
    updated_LP_A1 = LP_A1 + add_to_LP_A1
    updated_LP_A2 = LP_A2 + add_to_LP_A2
    updated_LP_s = LP_s + add_to_LP_s
    

    return "LP", {"A1":updated_LP_A1,"A2":updated_LP_A2,"s":updated_LP_s}


# In[ ]:




