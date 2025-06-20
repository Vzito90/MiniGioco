import soldati as s
import random as rand
import time as t

BUDGET_INIZIALE = 1000  
round = 0

def scegliCombattente():
    budget = BUDGET_INIZIALE
    squadra = []

    while budget >= 100:
        print(f"Il tuo budget è: {budget}$")
        print("1 - Cavaliere - 200$")
        print("2 - Arciere - 100$")
        print("3 - Guaritore - 100$")
        print("4 - Mago - 200$")
        scelta = input("Scegli membro squadra (seleziona il numero): ")
        try:
            if scelta == "1":
                costo = s.Cavaliere().getCosto()
                if budget >= costo:
                    soldato = s.Cavaliere()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
                else:
                    print("Non hai abbastanza soldi per un Cavaliere!")
            elif scelta == "2":
                costo = s.Arciere().getCosto()
                if budget >= costo:
                    soldato = s.Arciere()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
                else:
                    print("Non hai abbastanza soldi per un Arciere!")
            elif scelta == "3":
                costo = s.Guaritore().getCosto()
                if budget >= costo:
                    soldato = s.Guaritore()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
                else:
                    print("Non hai abbastanza soldi per un Guaritore!")
            elif scelta == "4":
                costo = s.Mago().getCosto()
                if budget >= costo:
                    soldato = s.Mago()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
                else:
                    print("Non hai abbastanza soldi per un Mago!")
            else:
                print("Scelta non valida.")
        except ValueError:
            print("Input non valido. Inserisci un numero corretto.")
        except:
            print("Errore grave")

    return squadra

def generaSquadraAI():
    budget = BUDGET_INIZIALE
    squadraAi = []
    id = 0

    tipi = [
        (s.Cavaliere, s.Cavaliere().getCosto()),
        (s.Arciere, s.Arciere().getCosto()),
        (s.Guaritore, s.Guaritore().getCosto()),
        (s.Mago, s.Mago().getCosto())
    ]

    while budget >= 100:
        opzioni_possibili = [t for t in tipi if t[1] <= budget]
        if opzioni_possibili:
            classe, costo = rand.choice(opzioni_possibili)
            soldato = classe()
            soldato.setNome(f"Team AI {id}")
            id += 1 
            squadraAi.append(soldato)
            budget -= costo
            print(f"AI sceglie: {soldato.getTipo()} (costo: {costo}$) - Budget residuo: {budget}$") 
    return squadraAi

def combattimento(player1, player2, teamUmano, teamAi):
    global round
    print("\n\n")
    player1.stato()
    player2.stato()
    print("\n\n")
    print(f"Inizia lo scontro tra {player1.getTipo()} e {player2.getTipo()}")
    turno = 0

    while player1.isAlive() and player2.isAlive():
        print(f"\nTurno {turno+1}")
        player1.stato()
        player2.stato()

        if turno % 2 == 0: 
            if isinstance(player1, s.Guaritore):
                player1.attacca(teamUmano)
                if rand.random() < 0.5:
                    player1.usaAbilitaSpeciale(teamUmano)
                if isinstance(player2, s.Guaritore):
                    print("Entrambi sono guaritori! Si infliggono 5 danni.")
                    player2.subisciDanno(5)
            elif isinstance(player1, s.Arciere):
                if not player1.getAbilitaUsata():
                    if rand.random() < 0.5:  
                        player1.usaAbilitaSpeciale([player2])
                else:
                    player1.attacca(player2)
            elif isinstance(player1, s.Mago):
                player1.attacca(player2)
                if rand.random() < 0.5:
                    player1.usaAbilitaSpeciale(teamUmano)
            else:
                player1.attacca(player2)
        else: 
            if isinstance(player2, s.Guaritore):
                player2.attacca(teamAi)
                if rand.random() < 0.5:
                    player2.usaAbilitaSpeciale(teamAi)
                if isinstance(player1, s.Guaritore):
                    print("Entrambi sono guaritori! Si infliggono 5 danni.")
                    player1.subisciDanno(5)
            elif isinstance(player2, s.Arciere):
                if not player2.getAbilitaUsata():
                    if rand.random() < 0.5:
                        player2.usaAbilitaSpeciale([player1])
                else:
                    player2.attacca(player1)
            elif isinstance(player2, s.Mago):
                player2.attacca(player1)
                if rand.random() < 0.5:
                    player2.usaAbilitaSpeciale(teamAi)
            else:
                player2.attacca(player1)

        turno += 1

    vincitore = player1 if player1.isAlive() else player2
    print(f"\n{vincitore.getNome()} ha vinto la partita!\n")
    round += 1
    return vincitore

def acquistaUmani(budget, squadra):
    print(f"\nHai ricevuto +300$! Budget attuale: {budget}$")
    while budget >= 100:
        print(f"Budget attuale: {budget}$")
        print("Vuoi acquistare un nuovo soldato?")
        print("1 - Cavaliere - 200$")
        print("2 - Arciere - 100$")
        print("3 - Guaritore - 100$")
        print("4 - Mago - 200$")
        print("0 - Fine acquisti")
        scelta = input("Scegli membro squadra (numero): ")
        try:
            if scelta == "0":
                break
            elif scelta == "1":
                costo = s.Cavaliere().getCosto()
                if budget >= costo:
                    soldato = s.Cavaliere()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
            elif scelta == "2":
                costo = s.Arciere().getCosto()
                if budget >= costo:
                    soldato = s.Arciere()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
            elif scelta == "3":
                costo = s.Guaritore().getCosto()
                if budget >= costo:
                    soldato = s.Guaritore()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
            elif scelta == "4":
                costo = s.Mago().getCosto()
                if budget >= costo:
                    soldato = s.Mago()
                    soldato.setNome("Tuo team")
                    squadra.append(soldato)
                    budget -= costo
            else:
                print("Scelta non valida.")
        except ValueError:
            print("Input non valido.")
        except:
            print("Errore imprevisto.")
    return budget, squadra

def acquistaAI(budget, squadra):
    id = len(squadra)
    tipi = [
        (s.Cavaliere, s.Cavaliere().getCosto()),
        (s.Arciere, s.Arciere().getCosto()),
        (s.Guaritore, s.Guaritore().getCosto()),
        (s.Mago, s.Mago().getCosto())
    ]
    while budget >= 100:
        opzioni_possibili = [t for t in tipi if t[1] <= budget]
        if opzioni_possibili:
            classe, costo = rand.choice(opzioni_possibili)
            soldato = classe()
            soldato.setNome(f"Team AI {id}")
            id += 1
            squadra.append(soldato)
            budget -= costo
    return budget, squadra

def torneo(teamUmano, teamAi):
    global round
    budgetGiocatore = 0
    budgetAI = 0

    while len(teamUmano) > 0 and len(teamAi) > 0:
        s1 = teamUmano.pop(0)
        s2 = teamAi.pop(0)
        vincitore = combattimento(s1, s2, teamUmano, teamAi)

        if vincitore == s1 and vincitore.isAlive():
            teamUmano.append(vincitore)
        elif vincitore == s2 and vincitore.isAlive():
            teamAi.append(vincitore)

        if vincitore.isAlive():
            if vincitore == s1:
                teamUmano.append(vincitore)
            else:
                teamAi.append(vincitore)

        if len(teamUmano) == 0 or len(teamAi) == 0:
            break 

    budgetGiocatore += 300
    budgetAI += 300
    print("\n--- FASE ACQUISTI ---")
    budgetGiocatore, teamUmano = acquistaUmani(budgetGiocatore, teamUmano)
    budgetAI, teamAi = acquistaAI(budgetAI, teamAi)

    print("\n=== TORNEO TERMINATO ===")
    if len(teamUmano) == 0:
        print("Hai perso! L'IA ha vinto il torneo!")
    else:
        print("Complimenti! Hai vinto il torneo!")
    print("Numero round giocati:", round)

print("BENVENUTO AL TORNEO DEL REGNO\n")
print("Costruisci la tua squadra!\n")
teamUmano = scegliCombattente()

print("\nL'IA sta scegliendo la sua squadra...\n")
teamAi = generaSquadraAI()

print("\n--- INIZIA IL TORNEO ---")
torneo(teamUmano, teamAi)
