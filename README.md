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
