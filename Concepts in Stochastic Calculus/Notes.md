

# Simulating Correlated Random Variables in Python
https://oscarnieves100.medium.com/simulating-correlated-random-variables-in-python-c3947f2dbb10

Different datasets and their correlations - described by ρ 
![img.png](img.png)


Let S1 and S2 be standard normal random variables (each with mean 0 and variance 1) sampled from a normal distribution. 
Because we are sampling them independently of one another, they are by default uncorrelated. 
We will test this out in Python by calculating the correlation coefficient. 
Remember, we define correlation as follows:
![img_1.png](img_1.png)

E[X] is defined as:
![img_2.png](img_2.png)


variance and standard deviations of some variable X as:
![img_3.png](img_3.png)



mpute two correlated variables X and Y with coefficient ρ (defined by us). 
To do this, we can use the following transformation:

![img_4.png](img_4.png)


 properties of normal random variables, namely:
![img_5.png](img_5.png)

which is true when S1 and S2 are statistically independent (uncorrelated). Next, using our previous definition of the correlation and the fact that S1 and S2 both have mean zero and variance 1:
![img_6.png](img_6.png)

therefore:
![img_7.png](img_7.png)

which completes our proof. 

