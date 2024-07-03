import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "cipolla": "Beltrame"
    }
}

if __name__ == "__main__":
    with open("test\\data_file.json", "w") as write_file:
        json_string = json.dump(data, write_file)