# Market-Volatility-Prediction
Using Threshold GARCH model to predict future market volatility in order to enhance investment decision

#Threshold GARCH Model
Normal ARCH/GARCH model provides symmetric prediction on both positive and negative shock of the market. However, negative shock actually is more persistent to market return (i.e. negative news/shocks at time t would have persistent effect on market return on time t+h where h>0).

Threshold GARCH model (TGARCH) was proposed by Glosten, Jagannathan and Runkle (1993) which decided to capture this effect. TGARCH includes a binary variable I in whcih I will be 1 when the market shock is negative and I will be 0 when the market shock is positive. Below is the TGARCH(1,1) dynamics:
<img src="https://render.githubusercontent.com/render/math?math=sigma_t^{2} = alpha_0 + (alpha_1 + gamma*I_{t-q})epsilon_{t-1}^{2} + alpha_2*sigma_{t-1}^{2}">
