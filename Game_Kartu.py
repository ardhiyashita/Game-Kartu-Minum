import random
import numpy

class Kartu:
    def __init__(self,tipe,face,value):
        self.tipe = tipe
        self.face = face
        self.value = value
    
    def showKartu(self):
        print(self.tipe,self.face,self.value)
        
    def returnKartu(self):
        return "{} {} {}".format(self.tipe, self.face, self.value)
        
    def returnKartuValue(self):
        return (self.tipe, self.face, self.value)

"""========================================================================="""

        
class KartuRemi(Kartu):
    def __init__(self):
        self.setsKartu = []

    def buatKartuRemi(self):
        self.tipes = ["Jantung","Wajik","Waru","Semanggi"]
        self.faces = ["As","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        
        for tipe in range(0,len(self.tipes)): #jantung
            for face in range(0,len(self.faces)): #as,1,2,3,4,5 (jantung)
                self.setsKartu.append(Kartu(self.tipes[tipe],self.faces[face],self.values[face])) #masuk ke list setsKartu
                
    def acakKartuRemi(self):
        for num in range(0,len(self.setsKartu)): #setsKartu = 52 kartu
            temp = self.setsKartu[num] # temp = setsKartu[0] = Jantung As,
            numAcak = random.randint(0, len(self.setsKartu)-1) # numAcak = ambil kartu acak,
            self.setsKartu[num] = self.setsKartu[numAcak] # setsKartu[0] = setsKartu[random = 23/12/9]
            self.setsKartu[numAcak] = temp # tukar numAcak = temp
            
            # ada tiga variabel yang dipake = temp, numAcak, num
            # dasar pertukaran:
            #     temp = num
            #     num = numAcak
            #     numAcak = temp

    def showKartuRemi(self):
        for kartu in self.setsKartu:
            kartu.showKartu()
            
    def ambilKartu(self):
        return self.setsKartu[0].returnKartu()
    
    def checkKartu(self,indeks):
        tipeK, faceK, valuesK = self.setsKartu[indeks].returnKartuValue()
        return tipeK, faceK, valuesK
    
    def showKartuIndeks(self,indeks):
        print(self.setsKartu[indeks].returnKartu())
    
    def kartuPegangan(self):
        listPegangan = []
        for kartu in self.setsKartu:
            ambil = kartu.returnKartu()
            listPegangan.append(ambil)
        return listPegangan    

"""========================================================================="""


class Pemain:
    def __init__(self,nama):
        self.nama = nama
        self.kartuPemain = KartuRemi()

    def namaPemain(self):
        return self.nama
        
    def tambahKartuPemain(self,kartu):
        self.kartuPemain.setsKartu.append(kartu) # nambahin kartu ke setsKartu
        
    def showKartuPemain(self):
        print("Nama pemain :",self.nama)
        for kartu in self.kartuPemain.setsKartu: # melihat kartu di kartuPemain
            kartu.showKartu() # memperlihatkan kartu dengan method showKartu di Class Kartu
        print("")
        
    def showKartuPegangan(self):
        print(self.kartuPemain.kartuPegangan())


"""========================================================================="""

                  
class Permainan:
    def __init__(self):
        self.kartuPermainan = [] # deklarasi
        self.paraPemain = []    # deklarasi
        self.maksPegangKartu = 5 # deklarasi
        self.pemenangGame = [] # awalnya listGiliran = []
    
    def tambahPemain(self,nama):
        self.paraPemain.append(Pemain(nama))
        
    def checkList(self,elem):
        if len(elem) >= 1:
            return True
        else:
            return False
        
    def mulaiPermainan(self):
        self.kartuPermainan = KartuRemi()
        self.kartuPermainan.buatKartuRemi()
        self.kartuPermainan.acakKartuRemi()

        for p in self.paraPemain:
            for j in range(0,self.maksPegangKartu):
                p.tambahKartuPemain(self.kartuPermainan.setsKartu[0])
                self.kartuPermainan.setsKartu.pop(0)   
            
            
    def showPermainan(self):
        for p in self.paraPemain:
            p.showKartuPemain()
        
        print("========================================================")
        print("Kartu di atas meja sekarang: ")
        # self.kartuPermainan = KartuRemi()
        s = self.kartuPermainan.ambilKartu()
        print(s)
        self.tipeK, self.faceK, self.valuesK = self.kartuPermainan.checkKartu(0) # indeks hanya untuk diisi, tapi nda dikembalikan
        self.kartuPermainan.setsKartu.pop(0)
        print("---------------------------")
        
        
# =========================================================================== #
        listKartuPilihan = []
        listPemenang = []
        pemenangSekarang = ""
        bermain = True
        while bermain:
            maxMain = len(self.paraPemain)
            # print(maxMain)
            
            # print(listGiliran)
            elemen = self.checkList(self.pemenangGame)
            # print(elemen)
            if elemen == True:
               for pemain in self.paraPemain:
                   if pemain.namaPemain() is self.pemenangGame[0]:
                       pemenangSekarang = self.pemenangGame[0]
                       
                       print("\n")
                       print("========================================================")
                       print("Anda menang. Giliran Anda mengeluarkan kartu remi :", pemain.namaPemain())
                       print("List kartu Anda: ")
                       pemain.showKartuPegangan()
                       pilihCard = int(input("Pilih indeks kartu Anda: "))
                       tipeK, faceK, valuesK = pemain.kartuPemain.checkKartu(pilihCard-1)
                       self.tipeK = tipeK
                       listKartuPilihan.append(valuesK)
                       listPemenang.append(pemain.namaPemain())
                       
                       print("========================================================")
                       print("Kartu di atas meja sekarang: ")
                       pemain.kartuPemain.showKartuIndeks(pilihCard-1)
                       print(listKartuPilihan)
                       pemain.kartuPemain.setsKartu.pop(pilihCard-1)
                   else:
                       continue

        # print(listKartuPilihan)
        # for pemain in range(0,len(self.paraPemain)):
        #     temp = self.paraPemain[pemain]
            
        #     acak = random.randint(0,len(self.paraPemain)-1) # output = 0, 1, 2, max player
        #     self.paraPemain[pemain] = self.paraPemain[acak]
        #     self.paraPemain[acak] = temp
        #     listGiliran.append(temp)
        
            for pemain in self.paraPemain:
                if pemain.namaPemain() is pemenangSekarang:
                    continue
                else:
                    print("\n---------------------------")
                    print("Giliran pemain : ", pemain.namaPemain())
                    print("List kartu Anda: ")
                    pemain.showKartuPegangan()
                    
                    print("Apakah memiliki kartu yang sesuai? 1 -> yes, 0 -> no")
                    pilihan = int(input("Pilihan Anda: "))
                    if pilihan == 1:
                        pilihKartu = int(input("Pilih indeks kartu Anda: "))
                        tipeK, faceK, valuesK = pemain.kartuPemain.checkKartu(pilihKartu-1)
                        if self.tipeK == tipeK:
                            listKartuPilihan.append(valuesK)
                            listPemenang.append(pemain.namaPemain())
                            pemain.kartuPemain.setsKartu.pop(pilihKartu-1)
                            print(listKartuPilihan)
                        else:
                            print("Tipe kartu tidak sesuai. Pemain berikutnya")
                    elif pilihan == 0:
                        print("Pemain berikutnya")
                    else:
                        print("Input Anda Salah. Coba ulang kembali")
            
            self.pemenangGame.clear()
            elem = self.checkList(listKartuPilihan)
            if elem == True:
                max_value = max(listKartuPilihan)
                max_index = listKartuPilihan.index(max_value)
                # print(max_index)
                self.pemenangGame.append(listPemenang[max_index])
                listKartuPilihan.clear()
                listPemenang.clear()
                # print(self.pemenangGame)
                             
            if len(listKartuPilihan) > maxMain:
                bermain = False

# k = KartuRemi()
# k.buatKartuRemi()
# k.showKartuRemi()
# print("")
# k.acakKartuRemi()
# k.acakKartuRemi()
# k.showKartuRemi()

p = Permainan()
p.tambahPemain("Putu")
p.tambahPemain("Made")
p.tambahPemain("Nyoman")
p.tambahPemain("Ketut")        

p.mulaiPermainan()
p.showPermainan()