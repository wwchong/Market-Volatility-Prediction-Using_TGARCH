# Using Threshold GARCH Model in Market-Volatility-Prediction
Using Threshold GARCH model to predict future market volatility in order to enhance investment decision

# Introduction of Threshold GARCH Model 
Normal ARCH/GARCH model provides symmetric prediction on both positive and negative shock of the market. However, negative shock actually is more persistent to market return (i.e. negative news/shocks at time t would have persistent effect on market return on time t+h where h>0).

Threshold GARCH model (TGARCH) was proposed by Glosten, Jagannathan and Runkle (1993) which decided to capture this effect. TGARCH includes a binary variable I in whcih I will be 1 when the market shock is negative and I will be 0 when the market shock is positive. Below is the TGARCH(1,1) dynamics:

![image](https://user-images.githubusercontent.com/80605152/142313495-ef0f2b05-dea9-4d89-9fcf-04101eefbf53.png)

# Realized Variance 
I used 5 years S&P 500 index data to build the model. First, I used 5 minutes data to calculate the daily realized variance. The autocorrelation graph shows there is serial correlation in realized variance of S&P 500 index. Therefore, we can probably predict future volatility.

![RV](https://user-images.githubusercontent.com/80605152/142336568-3a5a39c7-5f34-4ec0-825f-f821652bc804.jpg)

# AR(1) Process of S&P 500 Index Log Daily Return
In order to build TGARCH(1,1) model, we will also need to build a AR(1) model of  S&P 500 index log return in order to calculate the epsilon squared used in TGARCH model. Below is the summary of the AR(1) model:

![Screen Shot 2021-11-17 at 7 46 37 PM](https://user-images.githubusercontent.com/80605152/142336215-82f009ef-3538-4649-8316-574953d63ea6.png)

We can see that the coefficient of lagged log daily return is also statistically significant so there is also serial correlation in the log daily return.

The AR(1) coefficient would be used to calculate the epsilon squared.

# Building Threshold GARCH Model
After calculating the epsilon squared, we can then add a dummy variable I into the data and set it to 1 when epsilon squared is negative and set it to 0 when epsilon squared is zero or positive.

The result of the TGARCH model is as follow:
![Screen Shot 2021-11-17 at 7 53 58 PM](https://user-images.githubusercontent.com/80605152/142336917-4d0bdd93-2f31-4a69-8a13-de836db875e7.png)
