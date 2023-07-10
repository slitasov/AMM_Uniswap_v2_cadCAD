#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
The function determines the action that 
will be executed in the system: 
Trade or Liquidity add/removal
'''

def p_action(system_params, substep, state_history, previous_state):

    weights = [system_params["chance_liquidity"], 1-system_params["chance_liquidity"]]
    strings = ["Liquidity", "Trader"]
    agent = random.choices(strings, weights=weights)[0]
    
    token = "A1"
    value = 0
    share = 0
    
    # If agent is Trader --> the action is a trade
    if agent == "Trader":
        
        weights = [system_params["chance_A1"], 1-system_params["chance_A1"]]
        strings = ["A1", "A2"]
        token = random.choices(strings, weights=weights)[0]
        
        if token == "A1":
            value = random.uniform(0, previous_state["Trader"]["A2"])
        elif token == "A2": 
            value = random.uniform(0, previous_state["Trader"]["A1"])
    # If agent is Liquidity --> the action is liquidity provision/removal
    elif agent == 'Liquidity':
        
        share = random.uniform(-0.4, 0.4)

    return {"agent": agent, "value": value, "share": share, 'token': token}


# In[4]:


'''
The function determines conditions
ot the Trade
'''

def p_swapToAsset(system_params, substep, state_history, previous_state):
    
    timestep =  previous_state["timestep"]
    
    # Parameters
    feeFactor = (1-system_params["fee"])
    
    # State Variables
    agent = previous_state['agent']
    token = previous_state['token']
    value = previous_state['value']
    
    AMM_A1 = previous_state["AMM"]["A1"]
    AMM_A2 = previous_state["AMM"]["A2"]
    Trader_A1 = previous_state["Trader"]["A1"]
    Trader_A2 = previous_state["Trader"]["A2"]
    
    # In this case we buy "A1" for "A2"
    if agent == 'Trader' and token == 'A1':

        dA2 = value
        dA1 = AMM_A1/(AMM_A2+dA2*feeFactor)*dA2*feeFactor
        
        if dA2 < Trader_A2:
            return {"add_to_Trader_A1": dA1 , "add_to_AMM_A1": -dA1, 
                        "add_to_Trader_A2": -dA2, "add_to_AMM_A2": dA2} 
    
    # In this case we buy "A2" for "A1"
    if agent == 'Trader' and token == 'A2':
        dA1 = value
        dA2 = AMM_A2/(AMM_A1+dA1*feeFactor)*dA1*feeFactor
        
        if dA1 < Trader_A1:
            return {"add_to_Trader_A1": -dA1 , "add_to_AMM_A1": dA1, 
                        "add_to_Trader_A2": dA2, "add_to_AMM_A2": -dA2}
    
    
    # Return an empty dictionary if no conditions were met
    return {"add_to_Trader_A1": 0 , "add_to_AMM_A1": 0, 
                    "add_to_Trader_A2": 0, "add_to_AMM_A2": 0}


# In[5]:


'''
The function determines conditions
ot the Liquidity add/removal
'''

def p_Liquidity(system_params, substep, state_history, previous_state):
    
    timestep =  previous_state["timestep"]
    
    # State Variables
    agent = previous_state['agent']
    share = previous_state['share']
    
    AMM_A1 = previous_state["AMM"]["A1"]
    AMM_A2 = previous_state["AMM"]["A2"]
    AMM_s =  previous_state["AMM"]["s"]
    
    LP_A1 = previous_state["LP"]["A1"]
    LP_A2 = previous_state["LP"]["A2"]
    LP_s = previous_state["LP"]["s"]
    
    # In case LP adds/removes liquidity from the pool
    if agent == 'Liquidity':
        
        dA1 = AMM_A1 * share
        dA2 = AMM_A2 * share
        add_s = AMM_s * share
    
        if (dA1 < 0 and dA2 < 0 and (AMM_A1 - dA1) > 0 and (AMM_A2 - dA2) > 0 ) or (
            dA1 > 0 and dA2 > 0 and (LP_A1 - dA1) > 0 and (LP_A2 - dA2) > 0):

            return {"add_to_AMM_A1": dA1 , "add_to_LP_A1": -dA1, "add_to_LP_s": add_s,
                        "add_to_AMM_A2": dA2, "add_to_LP_A2": -dA2, "add_to_AMM_s": add_s }
    
    return {"add_to_AMM_A1": 0 , "add_to_LP_A1": 0, "add_to_LP_s": 0,
                        "add_to_AMM_A2": 0, "add_to_LP_A2": 0, "add_to_AMM_s": 0 }


# In[ ]:




