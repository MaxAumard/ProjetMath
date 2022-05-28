import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random as rd
import copy
import pylab

###VAR###

#dictionnaire des traitements (KEY son nom : VALUE poucentage d'efficacité)

traitements = {'traitement 1': 10, 'traitement 2' : 20, 'traitement 3' : 30, 'traitement 4' : 40, 'traitement 5' : 50,
        'traitement 6' : 60, 'traitement 7' : 70,'traitement 8' : 80, 'traitement 9' : 90, 'traitement 10' :10}
patients = {'traitement 1': 0, 'traitement 2' : 0, 'traitement 3' : 0, 'traitement 4' : 0, 'traitement 5' : 0,
        'traitement 6' : 0, 'traitement 7' : 0,'traitement 8' : 0, 'traitement 9' : 0, 'traitement 10' : 0}
guerris = {'traitement 1': 0, 'traitement 2' : 0, 'traitement 3' : 0, 'traitement 4' : 0, 'traitement 5' : 0,
        'traitement 6' : 0, 'traitement 7' : 0,'traitement 8' : 0, 'traitement 9' : 0, 'traitement 10' : 0}
historique = []
data = [key for key in traitements.keys()]
print(data)
nbr_tentative = 10000


###FONCTION###

def choix_uniforme(l):
    variable_aleatoire = rd.randint(0, len(l) - 1)
    rand_choice = data[variable_aleatoire]
    patients[rand_choice]+=1
    guerris[rand_choice]+=(rd.random()<(traitements[rand_choice]/100))
    historique.append((copy.deepcopy(guerris),copy.deepcopy(patients)))
    return rand_choice


def compter_nbr(l):
    dico = {}
    for traitement in data:
        dico.update({traitement: 0})
    for key in dico.keys():
        dico.update({key: l.count(key)})
    return dico




def application(nbr_tentative, fonction):
    echantillon = []
    for i in range(nbr_tentative):
        echantillon.append(fonction(data))
    return compter_nbr(echantillon)


def liste_en_proba():
    probs = [];
    for traitement in traitements.keys():
        probs.append(guerris[traitement]/patients[traitement])
    return probs;


def affichage_proba(plt,r):
    x = range(1,r+1)
    for traitement in traitements.keys():
        #Pourcentage de guerrison si patients>0 sinon 0 pour tout n nombre de patients traités
        y = [ historique[n][0][traitement]\
                for n in range(r)]
        plt.plot(x,y,label=traitement)
        plt.legend(loc="center")

def affichage_total(plt,r):
    x = range(1,r+1)
    y=[]
    for n in range(r):
        guerris = 0
        for traitement in traitements.keys():
            guerris+=historique[n][0][traitement]
        y.append(guerris)
    plt.plot(x,y,label="TOTAL",color='deeppink',linewidth=4)
    plt.legend(loc="best")




###CALCUL###

stat = application(nbr_tentative, choix_uniforme)

probs = liste_en_proba()

###AFFICHAGE###

for r in range(0,len(historique)):
    plt.cla();
    affichage_proba(plt,r)
    affichage_total(plt,r)
    plt.pause(0.0001)

###GRAPH###
#plt.xlim(-1, 10)

plt.show()
