#Project for SE512  Fall 2021
#PCourt

import pandas as pd
from IPython.display import display
import numpy as np
import scipy.stats as st
import math 
import matplotlib.pyplot as plt
import seaborn as sns

#####################################################
#Uploads results CSV file.
#####################################################

Results = pd.read_csv(RandomShows.csv")
Eval = Results['Number of Matches out of 10 (Stemmed vs Manual)']
nt = Eval.shape[0]

###########################################################################
#  Evaluate and print the 90% CI for the number of predictions out of 5.
###########################################################################

# 90% CI for results of comparison of Netflix

mu = np.mean(Eval)
sigma = np.std(Eval)
lowerCI = mu - sigma*1.645/math.sqrt(nt)
upperCI = mu + sigma*1.645/math.sqrt(nt)

print('The mean number of manually matched shows is ', round(mu, 4), ' and standard deviation is ', round(sigma, 4), '.' )
print('This is the 90% CI for the evaluation of the data vs. established searches such as Netflix: ')
print()
print('(', round(lowerCI, 4), ', ',round(upperCI, 4), ')')

###################################################################################################################
#Stemming.....H0: there is no difference (All shows match) X = 10....Ha: There is a difference X < 10
###################################################################################################################

StemDif = Results['Stem vs Unstem Matches']
#  If there is no difference in Stemming and Not stemming, the searched shows would all match...This is the null hypothesis.
# H0:  mu = 10
# Ha:  mu < 10  with alpha-value 0.05.  One-tailed

mu1 = np.mean(StemDif)
sigma1 = np.std(StemDif)
print('The mean stemmed and unstemmed search matches is', round(mu1, 4), ' and standard deviation is ', round(sigma1, 4), '.' )
print()
t_value,p_value=st.ttest_1samp(StemDif,10)
p_value
print('Test statistic is ', round(t_value, 4))
print()
print('p-value for a one tailed test is', round(p_value, 4))

print('Boxplot of Stemmed vs. Unstemmed Description Recommendations.')

sns.boxplot(y='Stem vs Unstem Matches', data=LenDif)

####################################################################################################################
# Create a standard normal distribution with mean as 0 and standard deviation as 1
####################################################################################################################

muNorm = 0
stdNorm = 1
snd = st.norm(muNorm, stdNorm)

x = np.linspace(-5, 5, 100)

plt.figure(figsize=(7.5,7.5))
plt.plot(x, snd.pdf(x))
plt.xlim(-5, 5)
plt.title('t-Distribution', fontsize='15')
plt.xlabel('Values t-Statistic with n - 1 df.', fontsize='15')
plt.ylabel('Probability', fontsize='15')
section = np.arange(-5, t_value, 0.01)
plt.fill_between(section,snd.pdf(section), color = 'r')
plt.axvline(x=-1.64, color = 'black')
plt.show()

####################################################################################################################
# t-test for short and long descriptions  H0:  Mu1 = Mu2, Ha: Mu1 != Mu2
####################################################################################################################
#read values...
LenDif = pd.read_csv(RandomShows.csv")

LenDif = LenDif.drop(['ID', 'title', 'Number of Matches out of 10 (Stemmed vs Manual)', 'Number of Matches out of 10 (Unstemmed vs Manual)'], axis = 1)

####################################################################################################################
#  Separate into long and short description and describe each data set.
####################################################################################################################

short = LenDif.query('short == "yes"')['Stem vs Unstem Matches']
long = LenDif.query('short == "no"')['Stem vs Unstem Matches']

LenDif.groupby('short').describe()
res = st.ttest_ind(short, long, equal_var=True)

display(res)

print('Side by side Boxplots of Matched Recommendations with Description Categorized as Short or Long.')

sns.boxplot(x='short', y='Stem vs Unstem Matches', data=LenDif)

####################################################################################################################
# Create a standard normal distribution with mean as 0 and standard deviation as 1
####################################################################################################################

muNorm = 0
stdNorm = 1
snd = st.norm(muNorm, stdNorm)

x = np.linspace(-5, 5, 100)

plt.figure(figsize=(7.5,7.5))
plt.plot(x, snd.pdf(x))
plt.xlim(-5, 5)
plt.title('t-Distribution for Description Length', fontsize='15')
plt.xlabel('Values t-Statistic', fontsize='15')
plt.ylabel('Probability', fontsize='15')
section1 = np.arange(-5, -0.6773252817596217, 0.01)
plt.fill_between(section1,snd.pdf(section1), color = 'r')
section2 = np.arange(0.6773252817596217, 5 , 0.01)
plt.fill_between(section2,snd.pdf(section2), color = 'r')
plt.axvline(x=-1.96, color = 'black')
plt.axvline(x = 1.96, color = 'black')
plt.show()

