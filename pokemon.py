from abc import ABC
from random import *

'''
    définition d'une classe abstraite
    une classe abstraite n'est pas instanciée et sert de modèle pour ses enfants
'''


class Pokemon(ABC):
    def __init__(self, nom):
        self._is_alive = True
        self.calc_hp()
        self.set_nom(nom)
        self.calc_atk()

    def set_hp(self, hp):
        self._hp = hp

    def get_hp(self):
        return self._hp

    def set_nom(self, nom):
        self._nom = nom

    def get_nom(self):
        return self._nom

    def set_atk(self, atk):
        self._atk = atk

    def get_atk(self):
        return self._atk

    def calc_hp(self):
        '''
            génération aléatoire des hp d'un pokemon
        '''
        hp = randint(70, 100)
        self.set_hp(hp)

    def calc_atk(self):
        '''
            génération aléatoire de l'atk d'un pokemon
        '''
        atk = randint(15, 30)
        self.set_atk(atk)

    def is_alive(self):
        '''
            vérification de l'état de notre pokemon
        '''
        if(self._hp <= 0):
            self._is_alive = False
            self.message()

    def statut(self):
        '''
            vérification des hp de notre pokemon
        '''
        if(self.get_hp() > 0):
            print(f"il reste {self.get_hp()} hp à {self.get_nom()}")

    def message(self):
        '''
            fin du game
        '''
        print(f"{self.get_nom()} est KO ")
