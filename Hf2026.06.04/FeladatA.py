dic = {}

with open("Timeline_of_ programming_languages.txt", "r") as f ,open("output.txt", "w") as f_ki: 
    for sor in f:
        adatok = sor.strip().split(";")
        
        dic = {
            "year": adatok[0],
            "lan": adatok[1],
            "firstname": adatok[2],
            "lastname": adatok[3]
        }
        f_ki.write(f"{dic['year']};{dic['lan']}\n")
        
        
