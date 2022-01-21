def yazdir():
     with open("Çalışma_programı.txt","r",encoding="utf-8") as  file:
        for satir in file:
            print((satir))


def Ders_sec1():                  
    Pazartesi = input ('pazartesi_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(Pazartesi+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')

def Ders_sec2():                
    Salı = input ('salı_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(Salı+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')

def Ders_sec3():                
    carsamba = input ('ÇarŞamba_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(carsamba+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')

def Ders_sec4():                
    Persembe = input ('perşembe_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(Persembe+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')

def Ders_sec5():                
    cuma = input ('cuma_günü_için_ders_giriniz:')
    ders1 = input('ders 1:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(cuma+ '\n'+ders1+'\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')

def Ders_sec6():                
    cumartesi = input('cumartesi_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(cumartesi+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n') 

def Ders_sec7():                
    Pazar = input('pazar_günü_için_ders_giriniz:')
    ders2 = input('ders 2:')
    ders3 = input('ders 3:')
    ders4 = input('ders 4:')
    ders5 = input('ders 5:')

    with open("Çalışma_programı.txt","a",encoding="utf-8") as file:   
        file.write(Pazar+ '\n'+ders2+'\n'+ders3+'\n'+ders4+'\n'+ders5+'\n')                       

while True:
    islem = input("1-> Yazdırmak için 1'e basınız\n2-> Pazartesi günü derslerini girmek için 2'ye basınız\n3-> Salı günü derslerini girmek için 3'e basınız\n4-> Çarşamba günü derslerini girmek için 4'e basınız\n5-> Perşembe günü derslerini girmek için 5'e basınız\n6-> Cuma günü derslerini girmek için 6'ya basınız\n7-> Cumartesi günü derslerini girmek için 7'ye basınız\n8-> Pazar günü derslerini girmek için 8'e basınız")

    if islem == '1':
        yazdir()
        pass
    elif islem == '2':
        Ders_sec1()
        pass
    elif islem == '3':
        Ders_sec2()
        pass
    elif islem == '4':
        Ders_sec3()
        pass
    elif islem == '5':
        Ders_sec4()
        pass
    elif islem == '6':
        Ders_sec5()
        pass
    elif islem == '7':
        Ders_sec6()
        pass
    elif islem == '8':
        Ders_sec7()
    else:
        break
