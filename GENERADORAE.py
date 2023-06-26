def uno():
 while True:

    import os

    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    print("DEL SIGUIENTE LISTADO:")
    print("1:PEDREGAL\t2:LOMAS:\t3:MEXICO\t4:METROPOLITANO\t5:CLINICA LONDRES \t6:MOCEL\t7:ROMA\t8:LINDAVISTA\t9:ACOXPA")
    print("10:STA MONICA \t11:UNIVERSIDAD:\t12:DEL CARMEN \t13:TORREON\t14:TAMPICO \t15:TIJUANA\t16:VALLE ORIENTE \t17:JUAREZ\t18:CULIACAN")
    print("19:XALAPA \t20:MORELIA:\t21:QUERETARO \t22:VILLAHERMOSA\t23:LEON \t24:PUEBLA\t25:SLP")
    hospital=input("SELECCIONA EL NUMERO DE HOSPITAL: \n")
    if hospital == "1":
     hospital= str("PD")
     hospital1 = "PEDREGAL"
    elif hospital == "2":
     hospital=str("LM")
     hospital1 = "LOMAS"
    elif hospital == "3":
     hospital=str("MX")
     hospital1 = "MÉXICO"
    elif hospital == "4":
     hospital=str("MT")
     hospital1 = "METROPOLITANO"
    elif hospital == "5":
     hospital=str("LM")
     hospital1 = "CLINICA LONDRES"
    elif hospital == "6":
     hospital=str("MC")
     hospital1 = "MOCEL"
    elif hospital == "7":
     hospital=str("SE")
     hospital1 = "ROMA"
    elif hospital == "8":
     hospital=str("LV")
     hospital1 = "LINDAVISTA"
    elif hospital == "9":
     hospital=str("AC")
     hospital1 = "ACOXPA"
    elif hospital == "10":
     hospital=str("SM")
     hospital1 = "STA MONICA"
    elif hospital == "11":
     hospital=str("CR")
     hospital1 = "DEL CARMEN"
    elif hospital == "12":
     hospital=str("UN")
     hospital1 = "UNIVERSIDAD"
    elif hospital == "13":
     hospital=str("TR")
     hospital1 = "TORREÓN"
    elif hospital == "14":
     hospital=str("TM")
     hospital1 = "TAMPICO"
    elif hospital == "15":
     hospital=str("TJ")
     hospital1 = "TIJUANA"
    elif hospital == "16":
     hospital=str("VO")
     hospital1 = "VALLE ORIENTE"
    elif hospital == "17":
     hospital=str("CJ")
     hospital1 = "CIUDAD JUAREZ"
    elif hospital == "18":
     hospital=str("CU")
     hospital1 = "CULIACAN"
    elif hospital == "19":
     hospital=str("XL")
     hospital1 = "XALAPA"
    elif hospital == "20":
     hospital=str("MR")
     hospital1 = "MORELIA"
    elif hospital == "21":
     hospital=str("QR")
     hospital1 = "QUERETARO"
    elif hospital == "22":
     hospital=str("VL")
     hospital1 = "VILLAHERMOSA"
    elif hospital == "23":
     hospital=str("LN")
     hospital1 = "LEÓN"
    elif hospital == "24":
     hospital=str("PB")
     hospital1 = "PUEBLA"
    elif hospital == "25":
     hospital=str("CM")
     hospital1 = "SAN LUIS POTOSI"
    else:
     print("NUMERO NO EXISTENTE")

    clear()

    print("1:ARCO EN C\t2:CAMARA NUCLEAR:\t3:DENSITOMETRIA\t4:FLUOROSCOPIA\t5:MASTOGRAFIA\t:6MASTO C/TOMOSINTESIS")
    print("7:ORTOPANTOMOGRAFIA\t8:PET CT:\t9:RADIOTERTAPIA\t10:RX\t11:RX DIGITAL\t12:RX SIN MESA")
    print("13:RX PORTATIL\t14:RESONANCIA:\t15:RX/FLUOROSCOPIA\t16:HEMODINAMIA\t17:SPECT/CTX")
    print("18:TOMOGRAFIA\t19:ULTRASONIDO:\t20:US PORTATIL\t21:ECOCARDIOGRAFO\t22:ESTACION DE POSTPROCESO\t23:DIGITALIZADOR")
    print("24:OARM\t25:NEURONAVEGADOR\t25:INORESORA")
    modalidad=input("INGRESA EL NUMERO DE MODALIDAD: \n")
    if modalidad == "1":
     print("ARCO EN C")
     modalidad = str("A")
     modalidad1 = str("ARCO EN C")
    elif modalidad == "2":
     modalidad=str("B")
     modalidad1 = str("CAMARA NUCLEAR")
     print("CAMARA NUCLEAR")
    elif modalidad == "3":
     modalidad=str("C")
     modalidad1=str("DENSITOMETRIA")
     print("DENSITOMETRIA")
    elif modalidad == "4":
     modalidad=str("D")
     modalidad1=str("FLUOROSCOPIA")
     print("FLUOROSCOPIA")
    elif modalidad == "5":
     modalidad=str("E")
     modalidad1=str("MASTOGRAFIA")
     print("MASTOGRAFIA")
    elif modalidad == "6":
     modalidad=str("F")
     modalidad1=str("MASTO C/TOMOSINTESIS")
     print("MASTO C/TOMOSINTESIS")
    elif modalidad == "7":
     modalidad=str("G")
     modalidad1=str("ORTOPANTOMOGRAFIA")
     print("ORTOPANTOMOGRAFIA")
    elif modalidad == "8":
     modalidad=str("H")
     modalidad1=str("PET CT")
     print("PET CT")
    elif modalidad == "9":
     modalidad=str("I")
     modalidad1=str("RADIOTERTAPIA")
     print("RADIOTERTAPIA")
    elif modalidad == "10":
     modalidad=str("J")
     modalidad1=str("RX")
     print("RX")
    elif modalidad == "11":
     modalidad=str("K")
     modalidad1=str("RX DIGITAL")
     print("RX DIGITAL")
    elif modalidad == "12":
     modalidad=str("L")
     modalidad1=str("RX SIN MESA")
     print("RX SIN MESA")
    elif modalidad == "13":
     modalidad=str("M")
     modalidad1=str("RX PORTATIL")
    elif modalidad == "14":
     modalidad=str("N")
     modalidad1=str("RESONANCIA MaGNÉTICA")
    elif modalidad == "15":
     modalidad=str("O")
     modalidad1=str("RX/FLUOROSCOPIA")
    elif modalidad == "16":
     modalidad=str("P")
     modalidad1=str("HEMODINAMIA")
    elif modalidad == "17":
     modalidad=str("Q")
     modalidad1=str("SPECT CT")
    elif modalidad == "18":
     modalidad=str("R")
     modalidad1=str("TOMOGRAFIA")
    elif modalidad == "19":
     modalidad=str("S")
     modalidad1=str("ULTRASONIDO")
    elif modalidad == "20":
     modalidad=str("T")
     modalidad1=str("ULTRASONIDO PORTATIL")
    elif modalidad == "21":
     modalidad=str("U")
     modalidad1=str("ECOCARDIOGRAFO")
    elif modalidad == "22":
     modalidad=str("V")
     modalidad1=str("ESTACION PROCESAMIENTO")
    elif modalidad == "23":
     modalidad=str("W")
     modalidad1=str("DIGITALIZADOR")
    elif modalidad == "24":
     modalidad=str("X")
     modalidad1=str("O-ARM")
    elif modalidad == "25":
     modalidad=str("Y")
     modalidad1=str("NEURONAVEGADORI")
    elif modalidad == "26":
     modalidad=str("Z")
     modalidad1=str("IMPRESORA")

    nequipo=input("INGRESA EL NUMERO CONSECUTIVO QUE ASIGNARA A ESTE EQUIPO: \n")

    clear()

    print("1:ACCURACY\t2:ALOKA:\t3:CAREASTREAM\t4:CMR\t5:ELEKTA\t:6:ESAOTE")
    print("7:GE\t8:GENERAL MEDICAL MERATE:\t9:HOLOGIC\t10:IMS\t11:MINDRAY\t12:PANORAMIC CO")
    print("13:PHILIPS\t14:SHIMADZU:\t15:SIEMENS\t16:SIRONA\t17:VILLA SISTEMI\t18:DEL MEDICAL")
    print("19:MEDTRONIC\t20:CODOnICS:\t21:LG\t22:HP\t23:GIOTTO\t24:MEDTRONIC")
    print("25:SAMSUNG")
    marca=input("SELECCIONA EL NUMERO DE MARCA: \n")
    if marca == "1":
     marca1=str("ACCURACY")
     marca = str("A")
    elif marca == "2":
     marca=str("B")
     marca1=str("ALOKA")
    elif marca == "3":
     marca=str("C")
     marca1=str("CAREASTREAM")
    elif marca == "4":
     marca=str("D")
     marca1=str("CMR")
    elif marca == "5":
     marca=str("E")
     marca1=str("ELEKTA")
    elif marca == "6":
     marca=str("F")
     marca1=str("ESAOTE")
    elif marca == "7":
     marca=str("G")
     marca1=str("GE")
    elif marca == "8":
     marca=str("H")
     marca1=str("GENERAL MEDICAL MERATE")
    elif marca == "9":
     marca=str("I")
     marca1=str("HOLOGIC")
    elif marca == "10":
     marca=str("J")
     marca1=str("IMS")
    elif marca == "11":
     marca=str("K")
     marca1=str("MINDRAY")
    elif marca == "12":
     marca=str("L")
     marca1=str("PANORAMIC CO")
    elif marca == "13":
     marca=str("M")
     marca1=str("PHILIPS")
    elif marca == "14":
     marca=str("N")
     marca1=str("SHIMADZU")
    elif marca == "15":
     marca=str("O")
     marca1=str("SIEMENS")
    elif marca == "16":
     marca=str("P")
     marca1=str("SIRONA")
    elif marca == "17":
     marca=str("Q")
     marca1=str("VILLA SISTEMI")
    elif marca == "18":
     marca=str("R")
     marca1=str("DEL MEDICAL")
    elif marca == "19":
     marca=str("S")
     marca1=str("MEDTRONIC")
    elif marca == "20":
     marca=str("T")
     marca1=str("CODOnICS")
    elif marca == "21":
     marca=str("U")
     marca1=str("LG")
    elif marca == "22":
     marca=str("V")
     marca1=str("HP")
    elif marca == "23":
     marca=str("W")
     marca1=str("GIOTTO")
    elif marca == "24":
     marca=str("X")
     marca1=str("MEDTRONIC")
    elif marca == "25":
     marca=str("Y")
     marca1=str("SAMSUNG")
    clear()

    año = input("INGRESA EL AÑO DE FABRICACIÓN DEL EQUIPO (####) : \n")
    print("")

    if año < "2000":
        año1 = año.replace("19", "")
    else:
        año1 = año.replace("20", "")

    clear()

    print(f"EQUIPO UBICADO EN: HA {hospital1}")
    print(f"MODALIDAD: {modalidad1}")
    print(f"MARCA: {marca1}")
    print(f"FABRICADO EN EL AÑO: {año}")
    print(f"NUMERO DE EQUIPO: {nequipo}")
    print("AEtitle HOMOLGADO: ", "H"+hospital+modalidad+marca+nequipo+año1)




    continuar = input('DESEA CONSULTAR OTRO AETITLE? S / N : \n ')
    if continuar.lower() in "s si y yes":
        continue
    else:
        break

def dos():
 while True:

    import os

    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


    AE=input("INGRESA EL AETITLE A HOMOLOGAR  \n")
    AE=AE.upper()
    if AE[1:3] == "PD":
     HOS="PEDREGAL"
    elif AE[1:3] == "LM":
     HOS = "LOMAS"
    elif AE[1:3] == "MX":
     HOS = "MÉXICO"
    elif AE[1:3] == "MT":
     HOS = "METROPOLITANO"
    elif AE[1:3] == "CL":
     HOS = "CLINICA LONDRES"
    elif AE[1:3] == "MC":
     HOS = "MOCEL"
    elif AE[1:3] == "SE":
     HOS = "ROMA"
    elif AE[1:3] == "LV":
     HOS = "LINDAVISTA"
    elif AE[1:3] == "AC":
     HOS = "ACOXPA"
    elif AE[1:3] == "SM":
     HOS = "STA MONICA"
    elif AE[1:3] == "CR":
     HOS = "DEL CARMEN"
    elif AE[1:3] == "UN":
     HOS = "UNIVERSIDAD"
    elif AE[1:3] == "TR":
     HOS = "TORREÓN"
    elif AE[1:3] == "TM":
     HOS = "TAMPICO"
    elif AE[1:3] == "TJ":
     HOS = "TIJUANA"
    elif AE[1:3] == "VO":
     HOS = "VALLE ORIENTE"
    elif AE[1:3] == "CJ":
     HOS = "CIUDAD JUAREZ"
    elif AE[1:3] == "CU":
     HOS = "CULIACAN"
    elif AE[1:3] == "XL":
     HOS = "XALAPA"
    elif AE[1:3] == "MR":
     HOS = "MORELIA"
    elif AE[1:3] == "QR":
     HOS = "QUERETARO"
    elif AE[1:3] == "VL":
     HOS = "VILLAHERMOSA"
    elif AE[1:3] == "LN":
     HOS = "LEÓN"
    elif AE[1:3] == "PB":
     HOS = "PUEBLA"
    elif AE[1:3] == "CM":
     HOS = "SAN LUIS POTOSI"
    else:
     print("NUMERO NO EXISTENTE")
    clear()

    if AE[3] == "A":
     mod = str("ARCO EN C ")
    elif AE[3] == "B":
     mod = str("CAMARA NUCLEAR")
    elif AE[3] == "C":
     mod = str("DENSITOMETRIA")
    elif AE[3] == "D":
     mod = str("FLUOROSCOPIA")
    elif AE[3] == "E":
     mod = str("MASTOGRAFIA")
    elif AE[3] == "F":
     mod = str("MASTO C/TOMOSINTESIS")
    elif AE[3] == "G":
     mod = str("ORTOPANTOMOGRAFIA")
    elif AE[3] == "H":
     mod = str("PET CT")
    elif AE[3] == "I":
     mod = str("RADIOTERTAPIA")
    elif AE[3] == "J":
     mod = str("RX")
    elif AE[3] == "L":
     mod = str("RX DIGITAL")
    elif AE[3] == "L":
     mod = str("RX SIN MESA")
    elif AE[3] == "M":
     mod = str("RX PORTATIL")
    elif AE[3] == "N":
     mod = str("RESONANCIA MaGNÉTICA")
    elif AE[3] == "O":
     mod = str("RX/FLUOROSCOPIA")
    elif AE[3] == "P":
     mod = str("HEMODINAMIA")
    elif AE[3] == "Q":
     mod = str("SPECT CT")
    elif AE[3] == "R":
     mod = str("TOMOGRAFIA")
    elif AE[3] == "S":
     mod = str("ULTRASONIDO")
    elif AE[3] == "T":
     mod = str("ULTRASONIDO PORTATIL")
    elif AE[3] == "U":
     mod = str("ECOCARDIOGRAFO")
    elif AE[3] == "V":
     mod = str("ESTACION PROCESAMIENTO")
    elif AE[3] == "W":
     mod = str("DIGITALIZADOR")
    elif AE[3] == "X":
     mod = str("O-ARM")
    elif AE[3] == "Y":
     mod = str("NEURONAVEGADOR")
    elif AE[3] == "Z":
     mod = str("IMPRESORA")

    if AE[5] == "A":
     marc = str("ACCURACY")
    elif AE[5] == "B":
     marc = str("ALOKA")
    elif AE[5] == "C":
     marc = str("CAREASTREAM")
    elif AE[5] == "D":
     marc = str("CMR")
    elif AE[5] == "E":
     marc = str("ELEKTA")
    elif AE[5] == "F":
     marc = str("ESAOTE")
    elif AE[5] == "G":
     marc = str("GE")
    elif AE[5] == "H":
     marc = str("GENERAL MEDICAL MERATE")
    elif AE[5] == "I":
     marc = str("HOLOGIC")
    elif AE[5] == "J":
     marc = str("IMS")
    elif AE[5] == "K":
     marc = str("MINDRAY")
    elif AE[5] == "L":
     marc = str("PANORAMIC CO")
    elif AE[5] == "M":
     marc = str("PHILIPS")
    elif AE[5] == "N":
     marc = str("SHIMADZU")
    elif AE[5] == "O":
     marc = str("SIEMENS")
    elif AE[5] == "P":
     marc = str("SIRONA")
    elif AE[5] == "Q":
     marc = str("VILLA SISTEMI")
    elif AE[5] == "R":
     marc = str("DEL MEDICAL")
    elif AE[5] == "S":
     marc = str("MEDTRONIC")
    elif AE[5] == "T":
     marc = str("CODOnICS")
    elif AE[5] == "U":
     marc = str("LG")
    elif AE[5] == "V":
     marc = str("HP")
    elif AE[5] == "W":
     marc = str("GIOTTO")
    elif AE[5] == "X":
     marc = str("MEDTRONIC")
    elif AE[5] == "Y":
     marc = str("SAMSUNG")
    neq = AE[4]
    fab = AE[6:8]
    print(f"EQUIPO UBICADO EN HA {HOS}")
    print(f"MODALIDAD: {mod}")
    print(f"NUMERO DE EQUIPO: {neq}")
    print(f"MARCA: {marc}")
    print(f"AÑO DE FABRICACIÓN: 20{fab}")

    continuar = input('Desea consultar otro AEtitle? S / N :')
    if continuar.lower() in "s si y yes":
      continue
    else:
         break

print(f"CNRI                                    GASS")

r=input("Selecciona la opcion deseada:  \nA) Generación de AEtitle \nB)Verificación de AEtitle ya creado\n")
print("")
r=r.upper()
if r == "A":
 uno()
elif r=="B":
 dos()
else:
 print("bye")


