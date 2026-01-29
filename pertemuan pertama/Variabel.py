#python bisa deklarasi variabel tanpa ketik tipe datanya
x = 2
y = "Devin suka oatsdie rasa choco milk"
print(x)
print(y)

z = 4
z = "Fachrul harus ikut ke kampar"
print(z)
#yang akan keluar adalah z yang di line 8

x = str(9)      #output '9'
y = int(7)      #outputnya 7
z = float(10)   #outputnya 10.0

#akan outputkan tipe data dari variabel yang di print
x = 8
y = 8.9
z = "sonic"
print(type(x))
print(type(y))
print(type(z))

#tanda petik satu sama aja dengan tanda petik dua
x = "Devin"
x = 'Devin'

#huruf kapital dan huruf non-kapital berbeda kalau dijadikan variabel
a = 4
A = "Fahcrul Multo"

#==============================================================
#nama variabel yang legal untuk dipakai
devin = "Chest Pain"
de_vin = "Chest Pain"
_de_vin = "Chest Pain"
deVin = "Chest Pain"
DEVIN = "Chest Pain"
devin2 = "Chest Pain"

#nama variabel yang gak bisa dipakai
#2devin = "Chest Pain"
#de-vin = "Chest Pain"
#de vin = "Chest Pain"

#Beberapa yang dijadikan variabel
#Camel Case
#myVariabelDevin = "koi no uta"

#Pascal Case
#MyVariabelDevin = "koi no uta"

#Snake Case
#my_variabel_devin  = "koi no uta"

#==============================================================
#banyak variabel dalam satu line
x, y, z = "Devin", "Fahcrul", "Iann"
print(x)
print(y)
print(z)

#banyakk variabel tapi isi datanya sama
x = y = z = "I loveee I love herrr"
print(x)
print(y)
print(z)

#menyebarkan isi list
Lagu = ["Happy", "Enchanted", "Let Down"]
x, y, z = Lagu
print(x)
print(y)
print(z)

#==============================================================
#Output Variabel
x = "Desperate Love"
print(x)

#jadi satu kalimat
x = "Devin"
y = "suka"
z = "Ular"
print(x, y, z)

#jadi satu kata
x = "Devin"
y = "suka"
z = "Ular"
print(x + y + z)

#Tambahin angka
x = 230
y = 2937
print(x + y)

#print variabel yang beda tipe data
x = 5
y = "Susu tinggi protein"
print(x, y)

#==============================================================
#fungsi biasa
x = "Kebab"

def kesukaan():
    print("Devin suka makan" + x)

kesukaan()

#bikin variabel yang sama dengan variabel global didalam fungsi
x = "Nikah"
def ingin():
    x = ("devin mau" + x)

ingin()
print("Devin mau" + x )
print("as a joke")

#kata kunci fungsi global
def kunci_global():
    global x
    x = "bunga"

kunci_global()
print(x + "kesayanganku diambil orang")

#ada 2 variabel global
x = "bahagia"

def kunci_global():
    global x
    x = "bunga"

kunci_global()
print(x + "kesayanganku diambil orang")