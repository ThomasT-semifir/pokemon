from herbe import Herbe
from eau import Eau
from feu import Feu
from random import randint


class Combat:

    def __init__(self):
        pass

    def duel(self, p1, p2):
        '''
            starter du combat
        '''
        self.attaquer(p1, p2)

    def attaquer(self, p1, p2):
        '''
            méthode opérant le combat
            mise à jour des hp
            mise à jour des multiplicateurs d'atk
            verification de l'etat du pokemon
        '''
        self.print_atk_by_p1(p1, p2)
        self.get_type(p1, p2)
        new_hp = self.new_hp(p1, p2)
        p2.set_hp(new_hp)
        p2.statut()
        p2.is_alive()

    def get_type(self, p1, p2):
        '''
            verification du type des deux pokemon en combat
            permet la mise à jour d'un multiplicateur en cas cas de type différent
        '''
        self.atk_reduce(p1, p2)
        self.atk_up(p1, p2)

    def atk_up(self, p1, p2):
        if(isinstance(p1, Herbe) == True & isinstance(p2, Eau) == True):
            self.multiplicateur_up()

        if(isinstance(p1, Eau) == True & isinstance(p2, Feu) == True):
            self.multiplicateur_up()

        if(isinstance(p1, Feu) == True & isinstance(p2, Herbe) == True):
            self.multiplicateur_up()

    def atk_reduce(self, p1, p2):
        if(isinstance(p1, Feu) == True & isinstance(p2, Eau) == True):
            self.multiplicateur_reduce()

        if(isinstance(p1, Herbe) == True & isinstance(p2, Feu) == True):
            self.multiplicateur_reduce()

        if(isinstance(p1, Eau) == True & isinstance(p2, Herbe) == True):
            self.multiplicateur_reduce()

    def multiplicateur_up(self):
        self._multiplicateur = 2
        print("c'est tres efficace")

    def multiplicateur_reduce(self):
        self._multiplicateur = 0.5
        print("ce n'est pas tres efficace")

    def print_atk_by_p1(self, p1, p2):
        print(f"{p1.get_nom()} attaque {p2.get_nom()} ")

    def c_critique(self):
        '''
            check de coup critique
        '''
        cc = randint(1, 2)
        return cc

    def new_hp(self, p1, p2):
        '''
            mise à jour des hp du pokemon attaqué
        '''
        cc = self.c_critique()
        self.check_cc(p1, cc)
        self.print_dgts(p1, p2, cc)
        if(self._multiplicateur in locals()):
            new_hp = p2.get_hp() - (p1.get_atk() * cc * self._multiplicateur)
        else:
            new_hp = p2.get_hp() - (p1.get_atk() * cc)

        return new_hp

    def print_dgts(self, p1, p2, cc):
        print(f"{p1.get_nom()} inflige {(p1.get_atk() * cc)} dégats à {p2.get_nom()}")

    def check_cc(self, p1, cc):
        if(cc == 2):
            print(f"{p1.get_nom()} a fait un coup critique")
