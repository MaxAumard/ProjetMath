import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random as rd
import pylab

###VAR###

#dictionnaire des traitements (KEY son nom : VALUE poucentage d'efficacité)

traitements = {'traitement 1': 10, 'traitement 2' : 20, 'traitement 3' : 30, 'traitement 4' : 40, 'traitement 5' : 50,
        'traitement 6' : 60, 'traitement 7' : 70,'traitement 8' : 80, 'traitement 9' : 90, 'traitement 10' :10}

patients = {'traitement 1': 0, 'traitement 2' : 0, 'traitement 3' : 0, 'traitement 4' : 0, 'traitement 5' : 0,
        'traitement 6' : 0, 'traitement 7' : 0,'traitement 8' : 0, 'traitement 9' : 0, 'traitement 10' : 0}
guerris = {'traitement 1': 0, 'traitement 2' : 0, 'traitement 3' : 0, 'traitement 4' : 0, 'traitement 5' : 0,
        'traitement 6' : 0, 'traitement 7' : 0,'traitement 8' : 0, 'traitement 9' : 0, 'traitement 10' : 0}

data = [key for key in traitements.keys()]
print(data)
nbr_tentative = 100


###FONCTION###

def choix_uniforme(l):
    variable_aleatoire = rd.randint(0, len(l) - 1)
    rand_choice = data[variable_aleatoire]
    patients[rand_choice]+=1
    guerris[rand_choice]+=(rd.random()<(traitements[rand_choice]/100))
    
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


def affichage_proba(probs):
    count = 0
    print("pour", nbr_tentative, "tentative :")
    for k in probs:
        print("La proba du traitement", count + 1, "est :", k)
        count += 1


###CALCUL###

stat = application(nbr_tentative, choix_uniforme)

probs = liste_en_proba()

###AFFICHAGE###

affichage_proba(probs)

###GRAPH###
plt.xlim(-1, 10)
plt.bar(stat.keys(), probs, width=0.2, color='deeppink')
pylab.xticks(list(range(0, len(stat.keys()))), stat.keys(), rotation=20)
plt.show()
