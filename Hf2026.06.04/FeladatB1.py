szotarak_lista = []
ketdimenzios_lista = []

fajlnev = "Timeline_of_ programming_languages.txt"

with open(fajlnev, "r", encoding="utf-8") as f:
    fejlec = f.readline().strip().split(";")  
    for sor in f:
        adatok = sor.strip().split(";")
        if len(adatok) == len(fejlec):
            dic = {
                "year": int(adatok[0]), 
                "lan": adatok[1],
                "firstname": adatok[2],
                "lastname": adatok[3]
            }
            szotarak_lista.append(dic)

with open(fajlnev, "r", encoding="utf-8") as f:
    f.readline()  
    for sor in f:
        adatok = sor.strip().split(";")
        if len(adatok) == 4: 
            sor_lista = [int(adatok[0]), adatok[1], adatok[2], adatok[3]]
            ketdimenzios_lista.append(sor_lista)

print(f"A szótárak listájának tartalma:\n{szotarak_lista}\n")
print(f"A kétdimenziós lista tartalma:\n{ketdimenzios_lista}")