import testSoldato as c
import random as rand

class Cavaliere(c.Soldato):
    def __init__(self):
        super().__init__(tipo = "Cavaliere")
        self.setCosto(200)
        self.setAttacco(10)
        self.setDifesa(30)
        self.__assorbiMetaDanno = False

    def attacca(self, avversario):
        danno = self.getAttacco() - avversario.getDifesa() // 2
        if rand.random() < 0.2:
            danno *= 2
            print(f"{self.getNome()} usa COLPO CRITICO e infligge {danno} danni!")
        else:
            print(f"{self.getNome()} attacca e infligge {danno} danni!")
        avversario.subisciDanno(danno)

    def usaAbilitaSpeciale(self):
        print(f"Cavaliere del {self.getNome()} attiva abilità speciale!")
        self.__assorbiMetaDanno = True 
        
    
    def subisciDanno(self, danno):
        if self.__assorbiMetaDanno:
            danno = danno //2
            self.__assorbiMetaDanno = False
        super().subisciDanno(danno)

class Arciere(c.Soldato):
    def __init__(self):
        super().__init__(tipo = "Arciere")
        self.setCosto(100)
        self.setAttacco(25)
        self.setDifesa(0)
        self.__abilitaUsata = False

    def getAbilitaUsata(self):
        return self.__abilitaUsata
    def setAbilitaUsata(self, bool):
        self.__abilitaUsata = bool

    def attacca(self, avversario):
        danno = self.getAttacco() - avversario.getDifesa() //2
        avversario.subisciDanno(danno)

    def usaAbilitaSpeciale(self, avversari):
        if self.__abilitaUsata == False:
            print("Colpisce tutti i nemici")
            for avv in avversari:
                danno = max(1, (self.getAttacco()//2) - avv.getDifesa() // 2)
                avv.subisciDanno(danno)
        self.__abilitaUsata = True

class Guaritore(c.Soldato):
    def __init__(self):
        super().__init__(tipo = "Guaritore")
        self.setCosto(100)
        self.setAttacco(0)
        self.setDifesa(0)
        self.__rianimazioneUsata = False

    def attacca(self, players):
        vivi = [p for p in players if p.isAlive()]

        if not vivi:
            print("Nessun giocatore vivo da curare.")
        elif vivi and self.getTipo()=="Guaritore":
            player = rand.choice(vivi)
            print(f"Guaritore cura {player.getTipo()} del {player.getNome()}")
            player.setSalute(100)
    
    def usaAbilitaSpeciale(self, team):
        if self.__rianimazioneUsata == False:
            caduti = [p for p in team if not p.isAlive()]
            if caduti:
                giocatore =  rand.choice(caduti)
                giocatore.setSalute(50)
                print(f"{self.getNome()} rianima {giocatore.getTipo()} con 50 salute!")
                self.__rianimazioneUsata = True
            else:
                print("Nessun alleato da rianimare")
        

class Mago(c.Soldato):
    def __init__(self):
        super().__init__(tipo = "Mago")
        self.setCosto(200)
        self.setAttacco(0)
        self.setDifesa(0)
        self.__creaturaEvocata = False 

    def attacca(self, avversario):
        if rand.random() < 0.25:
            danno = 0
            print(f"{self.getNome()} è troppo stanco {danno} danni!")
        else:
            danno = rand.randint(1, 4)
            danno *= 10
            print(f"{self.getNome()} lancia una magia e infligge {danno} danni!")
        
        avversario.subisciDanno(danno)
    

    def usaAbilitaSpeciale(self, team):
        if self.__creaturaEvocata:
            print(f"Impossibile usare Evocazione")
            return
        
        class Fantasma(c.Soldato):
            def __init__(self):
                super().__init__(tipo="Fantasma")
                self.setNome("Fantasma")
                self.setAttacco(40)
                self.setDifesa(0)
                self.setSalute(1)
            def attacca(self, avversario):
                print(f"Fantasma attacca con spavento mostruoso!")
                danno = self.getAttacco()
                avversario.subisciDanno(danno)
            def usaAbilitaSpeciale(self):
                pass
        
        print(f"{self.getNome()} evoca un Fantasma!")
        team.append(Fantasma())
        self.__creaturaEvocata = True