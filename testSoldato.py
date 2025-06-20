from abc import ABC, abstractmethod
import random as rand

class Soldato(ABC):
    def __init__(self, tipo = "Soldato"):
        super().__init__()
        self.__nome = "Generico"
        self.__costo = 0
        self.__attacco = 40
        self.__difesa = 40
        self.__salute = 100
        self.__tipo = tipo
         

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    
    def setCosto(self, costo):
        self.__costo = costo
    def getCosto(self):
        return self.__costo
    
    def setSalute(self, salute):
        self.__salute = salute
    def getSalute(self):
        return self.__salute
    
    def setAttacco(self, attaccoP):
        self.__attacco = self.__attacco + attaccoP
    def getAttacco(self):
        return self.__attacco
    
    def setDifesa(self, difesaP):
        self.__difesa = self.__difesa + difesaP
    def getDifesa(self):
        return self.__difesa
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    def getTipo(self):
        return self.__tipo
    

    @abstractmethod
    def attacca(self, avversario):
        pass

    @abstractmethod
    def usaAbilitaSpeciale(self):
        return True 

    def difenditi(self, danno):
        if rand.random() < 0.2:
            print(f"{self.getNome()} para l'attacco! Nessun danno subito!")
            return 0
        return danno
    
    def isAlive(self):
        if self.__salute > 0:
            return True
        else:
            return False
        
    def stato(self):
        saluteBar = "█" * (self.__salute // 10) + "_" * (10 - self.__salute // 10)
        print(f"{self.__nome} ({self.__tipo}) - Salute: {self.__salute} [{saluteBar}]")

    def subisciDanno(self, danno):
        self.difenditi(danno)
        self.__salute -= max(0, danno)
