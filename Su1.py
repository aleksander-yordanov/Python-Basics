def Av(): 
    num1 = int(input("въведете първо число: "))
    num2 = int(input("въведете второ число: "))
    num3 = int(input("въведете трето число: "))
    Avarage = (num1 + num2 +num3) / 3
    print(f"Средната стойност е {Avarage:.2f}")


def Exchange():
    print("Конвертор на лев към евро") 
    Lev = float(input("\nВъвeдeтe брой левове: "))
    Evro = Lev / 1.95
    print(f"{Lev} лева са равни {Evro:.2f} евро.")


def CtoF():
    Celsius = float(input("Въведете градусите в Целзии: "))
    Farenheit = (Celsius * 9/5) + 32
    print(f"{Celsius:.2f} в фаренхайт е {Farenheit:.2f} градуса ")
    

def Triangle():
    a = float(input("Въведете дължината на първата страна: "))
    b = float(input("Въведете дължината на втората страна: "))
    area = (a * b) / 2
    area = round(area, 2)

    print(f"Площта на правоъгълния триъгълник е: {area:.1f}")     
  

def InToCm():
    Inch = float(input("Въведете инчове: "))
    Cm = Inch * 2.53
    print(f"{Inch} инча са {Cm:.2f} сантиметра")


def Calc():
    num1 = float(input("Въведете първото чисоло: "))
    num2 = float(input("Въведете вторто чисоло: "))
    devide = num1 / num2
    print(f"{num1} делено на {num2} e {devide:.2f}")


def DDS():  
    cena = float(input("Въведете цена на стока: "))
    dds = float(input("Въведете ДДС като процент: "))
    DdsOtCena = cena * dds / 100
    print(f"\nПри ддс {dds}%, на {cena} лева ддс-то е {DdsOtCena:.2f}")
    print(f"Новата цена след ддс е: {cena + DdsOtCena:.2f}")


def FuelCalc():
    rastoqnie = int(input("Въведете растояние в километри: "))
    razhod = float(input("Въведете разход гориво за 100км: "))
    nujnoGorivo = (rastoqnie * razhod) / 100
    print(f"\nЗа {rastoqnie}км при разход {razhod},")
    print(f"ще са ви нужни {nujnoGorivo:.1f} литра гориво") 


def Chasovnik():
    minuti = int(input("Въведете минути: "))    
    dni = minuti // (24 * 60)
    ostavashtiMinuti = minuti % (24 * 60)

    chasove = (minuti // 60) - (dni * 24 )
    ostavashtiMinuti = minuti % 60
    print(f"{minuti} sa ravni na {dni} dena {chasove} chasa i {ostavashtiMinuti} minuti")   