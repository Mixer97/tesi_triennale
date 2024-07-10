	
from openpyxl import load_workbook

# Carica il file CSV in un DataFrame
workbook = load_workbook('python\\Codice_Progetto\\Template_Euramet_Excel\\04. YYMMDD - Rapporto Taratura UUT v9.xlsx')
sheet_euramet = workbook["Euramet"]

sheet_euramet["D25"] = 877

workbook.save("python\\Codice_Progetto\\Certificati_Euramet_Completi\\Test Rapporto Taratura UUT v9.xlsx")

"""
codice per aumentare un lettera e spostarsi sul csv

# Carattere corrente
char = 'D'

# Converti il carattere in valore ASCII, incrementa di 1 e poi riconverti in carattere
next_char = chr(ord(char) + 1)

print(next_char)  # Output: E
"""