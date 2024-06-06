# tesi_triennale_Git

tesi triennale presso Easting Electronics


28/05:
    Problema da rislvere: GUI stutters quando ho l'aggiornamento delle labels attivo. 
        Risolto problema del lag riferito alla GUI. Ho scoperto che era dettato dalla funzione read_holding_registers_mV() del Client. Dopo qualche test ho deciso di fare un update del valore in un loop continuo (in un thread separato), per poi leggerlo tramite un getter.
        Spiegato meglio: ho una variabile nella class DATA del client che viene updatata nel ciclo while presente nel main. In fine ho il comando update presente nella view, che abilita l'update dei 4 lcdDisplay tramite la variabile che sta venendo updatata.   
    Problema da risolvere: Logger continua a essere lento e non costante.
        Risolto il problema. Era legato alread_holding_registers_mV() del Client pure questo, quindi lo stesso trick usato per la GUI è bastato per risolvere. Ora ho a disposizione una acquisizione di ben oltre 1000 campioni al secondo.

29/05:
    Problema da risolvere: Il logger devere riuscire a scrivere i valori corretti con le corrette unita di misura. 
        Per realizzare questo ho implementato un secondo timer nella view che con una funzione aggiorna una lista, presente nel logger, con il testo di ogni lcdDisplay.  
        Dopo pranzo preocedo all' implementazione della scrittura sul CSv della lista e dei valori corretti in base all'unità di misura rilevata.

30/05
    Problema da risolvere: Chiusura di tutto il programma quando la finestra si chiude.
        Trovato segnale di chiusura lastWindowClosed() che viene chiamato quando l'ultima finestra viene chiusa e sistemata la chiusuare dei thread quando la finestra viene chiusa

06/06
    Problema da risolvere: Troppi click sui checkbox mandano in pappa il sistema.
        Provare a risolvere con un timer che esegue tutte le funzioni necessarie ogni secondo e che utilizza lo stato del tasto che è dato da una serie di variabili globali (che possono cambiare fra un clock e l'altro)
    Problema da risolvere: La scheda non gestisce il caso di 0 canali aperti.
        Impostare che il canale 1 sia attivo all'apertura della applicazione.
        Impostare un thread separato nel main, che vada ad aggiornare i canali nella scheda prendendo dati da una list
        NUOVA IDEA: usare un pulsante per eseguire l'update di tutte le robe nelle impostazioni in un unica volta.
        Alla fine è stato risolto nel seguente metodo: inizio leggendo lo stato della scheda e faccio corrispondere i vari checkbox allo stato corretto. Poi mi segnare i vari cambiamenti agli stati nella lista che ho inizializzato in precedenza. Alla fine il pulsante CUNCLUDI SETUP, o qaulcosa di simile, mi permette di inviare questa lista nel Client Controller e di utilizzarla per la chiamata di set_status fatta quando il bottone è premuto!    

    **NUOVO PROBLEMA**: quando concludo Il setup ho una chance che non vada in porto la modifica della scheda, che la app non si chiuda del tutto  
    quando la chiudo e che il display si rompa.  