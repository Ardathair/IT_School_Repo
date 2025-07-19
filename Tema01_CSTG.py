'''
Problema 1. Operatii aritmetice
Scrie un program care:
    - Cere doua numere si calculeaza:
        - Suma
        - Diferenta
        - Produsul
        - Impartirea
        - Imaprtirea intreaga
        - Restul impartirii (modulo)
        - Puterea
    - La final, afiseaza fiecare rezultat
'''

Number1 = int(input ("Primul numar este: "))
Number2 = int(input ("Al doilea numar este: "))

Suma = (Number1 + Number2)
Diferenta = (Number1 - Number2)
Diviziunea = (Number1 / Number2)
DiviziuneaIntreaga = (Number1 // Number2)
Modulo = (Number1 & Number2)
Puterea = (Number1 ** Number2)

print("\n--- Rezultate: ---")

print(f"Suma numerelor tale este: {Number1 + Number2}")
print(f"Diferenta numerelor tale este: {Number1 - Number2}")
print(f"Produsul numerelor tale este: {Number1 * Number2}")
print(f"Diviziunea numerelor tale este: {(Number1 / Number2):.3f}")
print(f"Diviziunea intreaga a numerelor tale este: {Number1 // Number2}")
print(f"Modulo numerelor tale este: {Number1 & Number2}")
print(f"Puterea numerelor tale este: {Number1 ** Number2}")

print(f"\nRecap rezultate: {Suma, Diferenta, Diviziunea, DiviziuneaIntreaga, Modulo, Puterea}")


'''
Problema 2. Tipuri de date
Declara cate o variabila pentru fiecare tip de date studiat si afiseaza tipul acesteia
'''

#Incepe de aici problema 2

#Sfarsit problema 2


'''
Problema 3. Transforma din minute in ore si minute
    - Primeste de la tastatura un numar de minute(ex. 135)
    - Afiseaza cate ore si minute reprezinta acel numar
'''

NumarMinute = int(input("Introdu numarul de minute pentru conversie: "))

Ora = NumarMinute // 60
MinuteRamase = NumarMinute % 60

print(f"Rezultatul conversiei tale este: ")
print(str(Ora)+" ore" " si " +str(MinuteRamase)+" minute")


'''
Problema 4. Bonul de cumparaturi
O persoana cumpara 3 produse. Vrem sa afisam:
    - Totalul fara TVA
    - TVA(ex. 19%)
    - Totalul cu TVA
'''

Produsul1 = float(input("Pretul primului produs este: "))
Produsul2 = float(input("Pretul celui de-al doilea produs este: "))
Produsul3 = float(input("Pretul celui de-al treilea produs este: "))

TotalFaraTVA = Produsul1 + Produsul2 + Produsul3
TVA1 = Produsul1 * 0.19
TVA2 = Produsul2 * 0.19
TVA3 = Produsul3 * 0.19
TVATotal = TVA1 + TVA2 + TVA3
TotalCuTVA = TotalFaraTVA + TVATotal

print(f"Costul total al produselor tale (fara TVA) este: {TotalFaraTVA}")
print(f"Costul TVA-ului este: {TVATotal}")
print(f"Costul total al produselor tale (TVA inclus) este: {TotalCuTVA}")


'''
Problema 5. Bugetul pentru un concediu
Cerinta: Un grup de prieteni planuieste o vacanta. Trebuie sa calculezi:
    - Contributia totala
    - Costul cheltuielilor (transport, cazare, mancare pe zile)
    - Ce suma ramane pentru distractii

Date de intrare:
    - Numarul de prieteni
    - Suma de bani per persoana
    - Costul transportului
    - Costul pe zi pentru cazare
    - Costul pe zi pentru mancare
    - Numarul de zile
'''

Numar_Prieteni = float(input("Numar de prieteni: "))
Suma_Per_Persoana = float(input("Suma de bani per persoana: "))
Cost_Transport = float(input("Cost transport: "))
Cost_Cazare = float(input("Cost cazare: "))
Cost_Mancare = float(input("Cost mancare: "))
Numar_Zile = float(input("Numar de zile: "))

Contributia_Totala = Numar_Prieteni * Suma_Per_Persoana
Cost_Cheltuieli = (Cost_Transport + Cost_Cazare + Cost_Mancare) * Numar_Zile
Distractie = Contributia_Totala - Cost_Cheltuieli

print("\n--- Rezultate: ---")

print (f"Contributia totala este: {Contributia_Totala}")
print (f"Costul cheltuielilor este: {Cost_Cheltuieli}")
print (f"Suma ramasa pentru distractie este: {Distractie}")