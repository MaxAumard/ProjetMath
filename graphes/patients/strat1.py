import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random as rd
import copy
colors=["#3454D1","#34D1BF","#D1345B","#3EC300","#FF1D15","#590925","#9B287B","#F3DE2C","#B0FF92","#DE6449"]

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
    for i,traitement in enumerate(traitements.keys()):
        probs.append(guerris[traitement]/patients[traitement])
    return probs;


def affichage_proba(plt):
    x = range(1,len(historique)+1)
    for i,traitement in enumerate(traitements.keys()):
        #Pourcentage de guerrison si patients>0 sinon 0 pour tout n nombre de patients traités
        y = [ historique[n][0][traitement]/historique[n][1][traitement]\
                if historique[n][1][traitement]>0\
                else 0\
                for n in range(len(historique))]
        plt.plot(x,y,label=traitement,color=colors[i])
        plt.ylabel("Part des patients ayant été guéris par un traitement")
        plt.xlabel("Nombre de patients")
        plt.legend(loc="center")



###CALCUL###

stat = application(nbr_tentative, choix_uniforme)

probs = liste_en_proba()

###AFFICHAGE###

affichage_proba(plt)

###GRAPH###
#plt.xlim(-1, 10)


plt.savefig('strat1.pdf')
