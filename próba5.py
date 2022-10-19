import json

with open("próba/lista.json") as file:
    nev_kor=json.load(file)

bemenet=input("Adja meg a felhasználó nevet: ")
name_try = 2
correct_name = False
code_try = 2
correct_code= True

while correct_name == False:
    if bemenet in nev_kor.keys():
        bemenet2 = input("Felhasználó:{}\nAdja meg a jelszót: ".format(bemenet))
        correct_name = True
        correct_code = False
        break
    if name_try==0:
        print("Túl sokszor próbálkozott!")
        break  
    else:
        bemenet = input("Hibás felhasználónév.\n{} lehetőség maradt.\nAdja meg a felhasználónevet: ".format(name_try))
        name_try-=1
    
while correct_code == False:
    if bemenet2 == str(nev_kor.get(bemenet)):
        print("Hozzáférés megadva.")
        correct_code = True
        break
    if code_try==0:
        print("Túl sokszor próbálkoztál. Hozzáférés megtagadva.")
        break
    else:
        bemenet2 = input("Hibás jelszó.\n{} lehetőség maradt.\nAddja meg a helyes jelszót: ".format(code_try))
        code_try-=1
    
bemenet3 = input("\n{} felhasználó menüje: \n\tJelszó módosítása:1\n\tFelhasználónév módosítása:2\n\tÚj felhasználó hozzáadása:3\n\tKilépés:4".format(bemenet))
while bemenet3:
    if bemenet3 == "1":
        code_try=2
        bemenet4 = input("Adjon meg egy új jelszót: ")
        bemenet5 = input("Adja meg újra a jelszót: ")
        while bemenet4!=bemenet5:
            if code_try !=0:
                bemenet5 = input("Helytelen megerősítő jelszó.\n{} lehetősége maradt.\nAdja meg újra az új jelszavát: ".format(code_try))
                code_try-=1
            else:
                print("Túl sokszor póbálkozott. Kezdje újra.")
                break
        if bemenet4==bemenet5:
            print("Jelszó mentve.")
            nev_kor[bemenet]=bemenet5
            uj_jelszo=json.dumps(nev_kor)
            with open("próba\lista.json","w") as f:
                f.write(uj_jelszo)
    if bemenet3=="2":
        uj_felhasznalonev = input("Adja meg az új felhasználó nevet: ")
        nev_kor.pop(bemenet)
        nev_kor[uj_felhasznalonev]=bemenet2
        uj_felhasznalo=json.dumps(nev_kor)
        with open("próba\lista.json","w") as f:
            f.write(uj_felhasznalo)
        bemenet = uj_felhasznalonev
    if bemenet3=="3":
        uj_felhasznalo = input("Adja meg a létrehozni kívánt felhasználót: ")
        print("Az új felhasználó az alapértelmezett jelszóval (1234) jött létre.\n Kérjük az első belépésnél változtassa meg.")
        nev_kor.update({uj_felhasznalo:1234})
        new_user = json.dumps(nev_kor)
        with open("próba\lista.json","w") as f:
            f.write(new_user)
    if bemenet3=="4":
        print("Kijelentkezés")
        break
    else:
        bemenet3 = input("\n{} felhasználó menüje: \n\tJelszó módosítása:1\n\tFelhasználónév módosítása:2\n\tÚj felhasználó hozzáadása:3\n\tKilépés:4\n".format(bemenet))