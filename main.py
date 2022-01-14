from combat import Combat
from eau import Eau
from feu import Feu
from partie import Partie

'''
    instanciation de deux pokemons de types différents
'''
feu = Feu("Salamèche")
eau = Eau("magicarpe")
'''
    instanciation de la classe combat pour son utilisation ultérieur
'''
combat = Combat()

'''
    lancement de la partie
'''
partie = Partie()
partie.set_tab1(feu)
partie.set_tab2(eau)
partie.duel(combat)
