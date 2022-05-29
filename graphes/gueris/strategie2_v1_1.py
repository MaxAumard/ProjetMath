import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random as rd
import copy
import pylab

###VAR###

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
drugs = []
for drug in traitements.keys():
    drugs.append(Drug(drug,traitements[drug]))

history = []
N = 10000
K = len(drugs)


def affichage_proba(plt):
    x = range(1,len(history))
    y = [[ history[n][drug].patients/n\
            for n in x] for drug in range(len(drugs)) ]
    print(y[0],x[0])
    plt.stackplot(x,y,labels=[drug.name for drug in drugs])
    plt.ylabel("Part des patients ayant reçu un traitement k")
    plt.xlabel("Nombre de patients")
    plt.legend(loc="center")
    plt.ylim(0,1)


for drug in drugs:
    drug.give_cure()
    history.append(copy.deepcopy(drugs))

for n in range(K+1,N+1):
    drug = sorted(drugs, key=lambda d: d.cured/d.patients, reverse=True)[0]
    drug.give_cure()
    history.append(copy.deepcopy(drugs))




###AFFICHAGE###

affichage_proba(plt)

###GRAPH###
#plt.xlim(-1, 10)


plt.savefig('strategie2_v1_1.pdf')
