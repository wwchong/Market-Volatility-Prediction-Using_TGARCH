# Market-Volatility-Prediction
Using Threshold GARCH model to predict future market volatility in order to enhance investment decision

#Threshold GARCH Model
Normal ARCH/GARCH model provides symmetric prediction on both positive and negative shock of the market. However, negative shock actually is more persistent to market return (i.e. negative news/shocks at time t would have persistent effect on market return on time t+h where h>0).

Threshold GARCH model (TGARCH) was proposed by Glosten, Jagannathan and Runkle (1993) which decided to capture this effect. TGARCH includes a binary variable I in whcih I will be 1 when the market shock is negative and I will be 0 when the market shock is positive. Below is the TGARCH(1,1) dynamics:
  
![image](https://user-images.githubusercontent.com/80605152/142313495-ef0f2b05-dea9-4d89-9fcf-04101eefbf53.png)
<img src="https://user-images.githubusercontent.com/80605152/142313495-ef0f2b05-dea9-4d89-9fcf-04101eefbf53.png" width="100" height="50">

