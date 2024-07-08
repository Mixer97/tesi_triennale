import json
from time import sleep
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "cipolla": "Beltrame"
    }
}

if __name__ == "__main__":
    with open("python\\Codice_Progetto\\JSON\\test.json", "w", encoding="utf-8") as write_file:
        json_string = json.dump(data, write_file, indent=4) 
        print(json_string) 
    with open("python\\Codice_Progetto\\JSON\\test.json", "r", encoding="utf-8") as json_string:
        new_json_string = json.load(json_string)
        print(new_json_string["president"]["name"]) # Cosi accedo a dict di dict