
with open("Rilke_A_parduc.txt", "r", encoding="utf-8") as f:
    szoveg = f.read()

maganhangzok = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']

betuk_szama = 0
maganhangzok_szama = 0

for karakter in szoveg:
  
    if karakter.isalpha():
        betuk_szama = betuk_szama + 1

    if karakter.lower() in maganhangzok:
        maganhangzok_szama = maganhangzok_szama + 1

szavak_listaja = szoveg.split()
szavak_szama = len(szavak_listaja)

print("A versben található betűk száma:", betuk_szama)
print("A versben található magánhangzók száma:", maganhangzok_szama)
print("A versben található szavak száma:", szavak_szama)