import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random as rd
from math import sqrt,log
import copy
from scipy.stats import beta
from statistics import mean

colors=['#3454D1','#34D1BF','#D1345B','#3EC300','#FF1D15','#590925','#9B287B','#F3DE2C','#B0FF92','#DE6449']
class Drug:
    def __init__(self, name, effectiveness):
        self.name = name
        self.effectiveness = effectiveness
        self.cured = 0
        self.patients = 0
    def give_cure(self):
        if rd.random()<self.effectiveness:
            self.cured+=1
        self.patients+=1


traitements = {'traitement 1': 0.1, 'traitement 2' : 0.2, 'traitement 3' : 0.3, 'traitement 4' : 0.4, 'traitement 5' : 0.5,
        'traitement 6' : 0.6, 'traitement 7' : 0.7,'traitement 8' : 0.8, 'traitement 9' : 0.9, 'traitement 10' :0.1}
               

def strat1(drugs,n):
    return rd.choice(drugs)
    
def strat2_1(drugs,n):
    return max(drugs, key=lambda d: d.cured/d.patients)
    
def strat2_2(drugs,n):
    epsilon=0.1
    return max(drugs, key=lambda d: d.cured/d.patients) if rd.random()>epsilon else rd.choice(drugs)
    
def strat3(drugs,n):
    return  max(drugs, key=lambda d: d.cured/d.patients+sqrt(2*log(n)/d.patients))
    
def strat4(drugs,n):
    return max(drugs, key=lambda d: beta(1+d.cured,1+d.patients-d.cured).rvs())
    
strats=[("stratégie 1",strat1),("stratégie 2.1",strat2_1),("stratégie 2.2",strat2_2),("stratégie 3",strat3),("stratégie 4",strat4)]
    



def runbatch(drugselector):
    drugs = []
    for drug in traitements.keys():
        drugs.append(Drug(drug,traitements[drug]))

    history = []
    N = 10000
    K = len(drugs)


    for drug in drugs:
        drug.give_cure()
        history.append(copy.deepcopy(drugs))

    for n in range(K+1,N+1):
        drug = drugselector(drugs,n)
        drug.give_cure()
        history.append(copy.deepcopy(drugs))
        
    return history[-1]


deaths=[]
for strat in strats:
    print("Evaluation de la ",strat[0],"....",sep="")
    batches=[runbatch(strat[1]) for i in range(20)]
    deaths.append(mean(sum(d.patients-d.cured for d in data) for data in batches))

plt.bar(range(len(strats)),deaths,tick_label=[strat[0] for strat in strats],color="#FF0077")
plt.ylabel("Nombre de patients non guéris")
plt.xlabel("Strategie")
plt.savefig("deaths.pdf")

