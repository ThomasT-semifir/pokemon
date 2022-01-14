class Partie:
    def __init__(self):
        pass

    def set_tab1(self, pokemon):
        self.tab1 = pokemon

    def set_tab2(self, pokemon):
        self.tab2 = pokemon

    def duel(self, combat):
        '''
            déroulé du combat au tour par tour
            vérification si l'un des pokemon est KO
            dans ce cas, le pokemon en vie remporte la victoire
        '''
        while(self.tab1._is_alive == True & self.tab2._is_alive == True):
            if(self.tab1._is_alive == True):
                combat.duel(self.tab1, self.tab2)

            if(self.tab2._is_alive == True):
                combat.duel(self.tab2, self.tab1)
