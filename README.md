# Market-Volatility-Prediction
Using Threshold GARCH model to predict future market volatility in order to enhance investment decision

#Threshold GARCH Model
Normal ARCH/GARCH model provides symmetric prediction on both positive and negative shock of the market. However, negative shock actually is more persistent to market return (i.e. negative news/shocks at time t would have persistent effect on market return on time t+h where h>0).

Threshold GARCH model (TGARCH) was proposed by Glosten, Jagannathan and Runkle (1993) which decided to capture this effect. TGARCH includes a binary variable I in whcih I will be 1 when the market shock is negative and I will be 0 when the market shock is positive. Below is the TGARCH(1,1) dynamics:

![image](https://user-images.githubusercontent.com/80605152/142313495-ef0f2b05-dea9-4d89-9fcf-04101eefbf53.png)

I used 5 years S&P 500 index data to build the model. First, I used 5 minutes data to calculate the daily realized variance. The autocorrelation graph shows there is serial correlation in realized variance of S&P 500 index. Therefore, we can probably predict future volatility.

![RV](https://user-images.githubusercontent.com/80605152/142335886-e00e7033-8ef6-4d38-9d20-0734139a77bc.jpg)

In order to build TGARCH(1,1) model, we will also need to build a AR(1) model of  S&P 500 index log return in order to calculate the epsilon squared used in TGARCH model. Below is the summary of the AR(1) model:

![Screen Shot 2021-11-17 at 7 46 37 PM](https://user-images.githubusercontent.com/80605152/142336215-82f009ef-3538-4649-8316-574953d63ea6.png)

