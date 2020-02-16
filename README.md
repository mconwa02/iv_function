Weight of evidence (WOE) and Information value (IV)
---------------------------------------------------
---------------------------------------------------

WOE and IV are powerful techniques to perform feature transformation and selection.
These concepts have huge connection with the logistic regression modeling technique.
It is widely used in credit scoring to measure the separation of good vs bad customers.

![Image](woe_iv.png)

![Image](iv.png)

The advantages of WOE transformation are
1. Handles missing values
2. Handles outliers
3. The transformation is based on logarithmic value of distributions. This is aligned with the logistic regression output function
4. No need for dummy variables

By using proper binning technique, it can establish monotonic relationship (either increase or decrease) between the target and a feature
Also, IV value can be used to select features quickly.

![Image](prediction_power.png)