# Questo Model ha il compito di tenere dentro di se i dati della sessione e i dati necessari al controller.
# NON DEVE COMUNICARE DIRETTAMENTE CON LA VIEW

class Logger:
    def __init__(self, nome_CSV = None):
        self.nome_CSV = nome_CSV
        
    def CSV_name_getter(self):
        return f"{self.nome_CSV}"
    
    def CSV_name_setter(self, nuovo_nome_CSV):
        self.nome_CSV = nuovo_nome_CSV
        
    def CSV_path_getter(self):
        self.path_CSV = f'Codice_Progetto\\CSV\\{self.nome_CSV}.csv'
        return f"{self.path_CSV}"