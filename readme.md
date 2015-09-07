## Flavours of Physics - Kaggle Challenge
https://www.kaggle.com/c/flavours-of-physics


### Competition Background
*"In this competition, you are given a list of collision events and their properties. You will then predict whether a τ → 3μ decay happened in this collision. This τ → 3μ is currently assumed by scientists not to happen, and the goal of this competition is to discover τ → 3μ happening more frequently than scientists currently can understand."*

As we understand it, we essentially are looking to predict whether or not a particular decay has occured in a collision, given a certain set of properties about that collision.

There are a couple of distinctions that have to be made because these τ → 3μ collision events are simulated --- in other words, there are not actually observed.

Because of this (as stated by the hosts of the competition) we must do two things:

**Check Agreement**
   - Classifiers should agree on real and simulated data. (This is because some data cannot be perfectly simulated and a high performance classifier can be developed by picking those features)
   - The requirement is that the classifier does not show a significant discrepancy when applied to simulated vs. real data. The **Kolmogorov-Smirnov test** is used to evaluate the differences between the classifier distribution.


**Check Correlation**
   - Model should be uncorrelated to the τ mass.
   - _"Each particle has its own mass. In an ideal world, one would just the mass of a particle to tell which particle it is. However, in reality, mass is an estimation, and it isn't a feature that scientists trust when building a model. Correlations with mass can cause an artificial signal-like mass peak or lead to incorrect background estimations."_
   - Our submission needs a **Cramer-von Mises** test value less than 0.002 to pass.
