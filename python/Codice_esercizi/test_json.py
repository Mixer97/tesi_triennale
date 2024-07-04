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
    with open("test\\data_file.json", "w", encoding="utf-8") as write_file:
        json_string = json.dump(data, write_file, indent=4)  
    with open("test\\data_file.json", "r", encoding="utf-8") as json_string:
        new_json_string = json.load(json_string)
        print(new_json_string)