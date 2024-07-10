	
from openpyxl import load_workbook

# Carica il file CSV in un DataFrame
workbook = load_workbook('python\\Codice_Progetto\\Template_Euramet_Excel\\04. YYMMDD - Rapporto Taratura UUT v9.xlsx')
sheet_euramet = workbook["Euramet"]

sheet_euramet["D25"] = 877

workbook.save("python\\Codice_Progetto\\Certificati_Euramet_Completi\\Test Rapporto Taratura UUT v9.xlsx")