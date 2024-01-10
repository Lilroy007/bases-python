# Exercise 1
age=input("Quel est votre âge ?")
age=int(age)
if age<18:
    print("Vous êtes mineur")
else:
    print("Vous êtes majeur")

# Exercice 2
tab1=[2, 7, 93, 45, 2, 129, 403, 5, 894, 345, 209]
def maximum(tab1):
    maxi=tab1[0]
    for i in range(len(tab1)):
        if tab1[i]>maxi:
            maxi=tab1[i]
    return maxi

print(maximum(tab1))

# Exercice 3
tab2 = [
    # [nom, prix, rendement]
    ["a", 120, "12%"],
    ["b", 10, "25%"],
    ["c", 26, "44%"],
    ["d", 390, "10%"],
    ["e", 225, "26%"],
    ["f", 89, "38%"],
]
def action_avec_max_rendement(tab2):
    max_rendement = 0
    action_max_rendement = None

    for action in tab2:
        nom, prix, rendement = action
        rendement = float(rendement.strip('%')) / 100  # Convertir le pourcentage en nombre décimal

        if rendement > max_rendement:
            max_rendement = rendement
            action_max_rendement = action

    return action_max_rendement

action = action_avec_max_rendement(tab2)
print(f"L'action avec le plus de rendement est {action[0]} avec un rendement de {action[2]}")

# Exercice 4
tab3 = [
    # [nom, prix, rendement]
    ["a", 120, "12.3%"],
    ["b", 10, "11.5%"],
    ["c", 26, "10.9%"],
    ["d", 390, "11.8%"],
    ["e", 225, "11.7%"],
    ["f", 89, "12.1%"],
]
def toto(valeur, tab3):
    gainPotentionnel = 0
    gainReel = 0
    bestRendement = 0
    bestAction = tab3[0]
    for action in tab3: 
       pourcentage = float(action[2].replace('%', ''))
       gainPotentionnel = (action[1] * pourcentage) / 100
       quotient = valeur // action[1]
       gainReel = quotient * gainPotentionnel
       if gainReel > bestRendement:
           bestRendement = gainReel
           bestAction = action
           return [bestAction, bestRendement]
resultat = toto(140, tab3)
print('La meilleure action est', resultat[1][0], 'avec un rendement maximal de', resultat[0], '€')