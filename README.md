# AMM_cadCAD

This project documents my initial foray into creating a cadCAD model, specifically simulating trading on Uniswap V2's Automated Market Maker (AMM). The project was executed in three stages: Discovery, Design, and Deployment.

## Discovery Phase
During the Design phase, I delved into the concept of AMM and designed a system that aligns with its primary objectives: minimizing operational costs and market risks.

The main goals of the system were identified, leading to the formulation of system requirements. Some of these include:

Traders can only engage in transactions with tokens they possess.
The asset prices in the pool should fluctuate in response to trades.
The addition or removal of liquidity by a Liquidity Provider should not affect the pool's prices.
The value of already-distributed shares should remain unaffected when a Liquidity Provider adds or removes liquidity.
In the third step of the design phase, I identified the key stakeholders of Uniswap V2, namely Traders and Liquidity Providers, and explored their interactions and mutual benefits.

The fourth step involved identifying the main metrics for Uniswap V2: slippage and impermanent loss, both of which should be minimized. Additionally, the system should offer high returns to liquidity providers and maintain high trading volumes.

Lastly, I utilized Causal Loop and Stock & Flow diagrams to formalize the system.

## Design phase

During the design phase, the system that was conceptually outlined in the discovery phase was mathematically formalized. I delved into the study of Constant Sum Market Maker (CSMM) and Constant Product Market Maker (CPMM), and explored their differences. As an outcome of this phase, I derived mathematical formulas for various aspects such as trading, adding/removing liquidity, slippage, impermanent loss, and others. For instance, here's an example of a formula used to calculate slippage.

<img width="327" alt="image" src="https://github.com/slitasov/AMM_cadCAD/assets/43509889/9fede037-a041-4655-b553-ee94b7a908ec">

## Deployment Phase

During the deployment phase, I utilized the cadCAD Python library, which is designed for validating complex systems, to implement a simulation of Uniswap V2's AMM.

Furthermore, the simulation includes a component that generates random transactions at each timestep, either a Trade or a Liquidity addition/removal. If the action is a Trade, the simulation randomly determines the value based on the Trader's balance. If the action is a Liquidity addition/removal, the Liquidity Provider alters the amount of liquidity in the pool.

The simulation results are visualized through four graphs. Here is a brief description of each graph:

Price over Time. This graph displays the variation of the price over time. The price is represented on the y-axis, while the x-axis represents the time. The line plot shows the trend of the price, with a cyan color scheme.

AMM Balance (A1 and A2) over Time. This graph illustrates the balance of tokens A1 and A2 in the Automated Market Maker (AMM) over time. The y-axis represents the balance, and the x-axis denotes the time. The line plots show the changes in the balances of A1 and A2, with the AMM A1 balance displayed in lime color and the AMM A2 balance in purple.

LP Balance (A1 and A2) over Time. This graph depicts the balance of tokens A1 and A2 held by the Liquidity Provider (LP) over time. The y-axis represents the balance, and the x-axis represents the time. The line plots show the fluctuations in the balances of A1 and A2, with the LP A1 balance displayed in orange color and the LP A2 balance in pink.

Collected Fees for A1 and A2 over Time. This graph illustrates the fees collected for tokens A1 and A2 over time. The y-axis represents the collected fees, and the x-axis denotes the time. The line plots show the changes in the collected fees for A1 and A2, with the fee collected for A1 displayed in red and the fee collected for A2 in blue.
