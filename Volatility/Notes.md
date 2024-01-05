# Volatility 
Def : annualized standard deviation of returns.

**Historical or realized volatility**: is
a backward looking statistical measure of what volatility
has been. It assumes that there is some
information in this data that will tell us what volatility
will be in the future.\

**Implied volatility** is the number you have to put into
the Black–Scholes option-pricing formula to get the
theoretical price to match the market price. This is
often said to be the market’s estimate of volatility.\
Calculations : https://medium.com/hypervolatility/extracting-implied-volatility-newton-raphson-secant-and-bisection-approaches-fae83c779e56

**Forward volatility** is either actual or implied, over some time period in the future

### Types of Models
1. Econometric models/Time Series Models
2. Deterministic models: BSM - deterministic volatility (surface) model.
3. Stochastic volatility: Heston.
4. Poisson processes: times of low volatility and
times of high volatility
5. Uncertain volatility: we no longer get a single option
price, but a range of prices, representing worst-case
scenario and best-case scenario

**Econometric models:** These models use various forms of
time series analysis to estimate current and future
expected actual volatility. They are typically based on
some regression of volatility against past returns and
they may involve autoregressive or moving-average components.
In this category are the GARCH type of models.
Sometimes one models the square of volatility, the
variance, sometimes one uses high-low-open-close data
and not just closing prices, and sometimes one models
the logarithm of volatility. The latter seems to be quite
promising because there is evidence that actual volatility
is lognormally distributed. Other work in this area
decomposes the volatility of a stock into components,
market volatility, industry volatility and firm-specific
volatility. This is similar to CAPM for returns.

**Stochastic volatility**: Since volatility is difficult to measure,
and seems to be forever changing, it is natural to model
it as stochastic. The most popular model of this type is
due to Heston. Such models often have several parameters
which can either be chosen to fit historical data
or, more commonly, chosen so that theoretical prices
calibrate to the market. Stochastic volatility models
are better at capturing the dynamics of traded option prices better than deterministic models. However, different
markets behave differently. Part of this is because
of the way traders look at option prices. Equity traders
look at implied volatility versus strike, FX traders look
at implied volatility versus delta. It is therefore natural
for implied volatility curves to behave differently in
these two markets. Because of this there have grown
up the sticky strike, sticky delta, etc., models, which
model how the implied volatility curve changes as the
underlying moves.


### Volatility Smile