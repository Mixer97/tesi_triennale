# tesi_triennale_Git

## tesi triennale presso Easting Electronics


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

    **NUOVO PROBLEMA**: quando concludo Il setup ho una chance che non vada in porto la modifica della scheda, che la app non si chiuda del tutto quando la chiudo e che il display si rompa.  
    OSS: quando l'interfaccia è chiusa non ho problemi <<valutare stoppare l' interfaccia e il logger mentre si fa il setup>>

10/06 
    Problema da risolvere: non riuscivo a fare riconoscere una package da parte di python, nonostante lo avessi installato sul venv corretto.   
        Ho osservato che sebbene il comando pip list mi dava il package come installato, nella cartella fisica non era presente. Ho provato poi a copiare e incollare la cartella del package che volevo fare riconoscere e la cosa sembra avere funzionato (per quanto il problema rimanga).
    Problema da risolvere: sono riuscito a realizzare una connessione con la scheda Z-4AI(-1) tramite RS-232.
        Appena riuscirò a capire come comunicare informazione aggiornerò la lista.

11/06
    Problema risolo: comunicazione con la scheda viene fatta con RS-232 e con impostazioni segnate sul tablet.
    Nuovo obiettivo: decidere cosa mettere dentro una finestra di dialogo per il setup dei canali.

12/06
    Continuazione sul lavoro delle finestre di setup per i vari canali.
    Rimane da implementare quello che ho fatto per setup Dialog 1 su gli altri setup e anche di implementare per tutti il bottone per azzerare.
    I menù a tendina devono essere colorati in modo diverso quando scendono e non devono essere tondeggianti.

13/06
    Inizio a connettere i due client in modo che vengano attivati dello stesso pulsante e fermati pure.
    Nello specifico inizio la modifica del Logger.
    Ho iniziato a implementare la lettura del registro dalla scheda mediante loop. Dovrebbe funzionare tutto e nel pomeriggio collego i due lcd ai valori e vedo se tornano.
    Implementato funzionamento del logger con successo per la registrazione di valri in mV dei due canali dell'SG600.
    Attivazione del canale 1 di default nel caso ci sia la disattivazione di ogni canale.
    Gestione della configurazione 0000 fatta con successo. 

14/06
    Inizio la giornata lavorando sulle schermate di setup dei vari canali della scheda laumas.

17/06
    Ristrutturazione del codice secondo logica a oggetti e non statica.
    Parti fatte e funzionanti: Controller_TCP, Controller_MODBUS, Main_TCP, Logger, Banco di taratura, Dialog_setup_1
    (FARE ATTENZIONE CON IL CAST A STRING E FARE L'ASSEGAZIONE AL DI FUORI DI ESSA)
    
18/06
    Ho capito meglio la programmazione a oggetti, ora sto facendo dei cambiamenti per dare in input un solo oggetto di cuimi interessano i vari campi.
    Ristrutturazione efficace: Banco_di_taratura, Main_window, i 2 controller, Logger, finita.

21/06
    installare: Docker desktop (installer dal sito),
                {{Podman (gestire immagini virtuali) --> se non voglio usare solo comandi da riga di comando}}

    Incontro con Emanuele per decidere cosa fare. Scartata idea della webapp. Continuare a lavorare con QT per creare una applicazione in loco. L'idea è quella di andare poi a lavorare con un docker che ha dentro GRAPHANA (grafici e collegamento tramite web) e INFLUX (database con estensione per Python e si accede da web per vedere il funzionamento) e nel quale gira l'applicazione.
        Necessaria implementazione della parte gestione misura (settaggio delgli step di misura e acquisizione del dato quando arrivato alla stabilità).
        Necessaria implementazione della parte grafica per visualizzazione dei dati.

28/06
    Continuo sul lavoro dei grafici. Realizzare una media mobile per fare il grafico

01/07
    Setup banco con pesi [V], 
    far partire il grafico quando l'applicazione parte[V],
    - Problema: il grafico non funziona quando mostra valori non messi nelle combobox
    pulsanti per cambiare canale,
    creazione classe canale con buffer o senza,
    aggiornamento valori separato dalle ComboBox,
    setting per visualizzazione scala automatica o manuale.
    imparare come settare i vari canali dalla combobox