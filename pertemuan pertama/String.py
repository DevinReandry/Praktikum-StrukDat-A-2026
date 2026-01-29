#petik tidak akan merubah keluaran di kondisi ini
print("halo")
print('halo')

#petik dalam petik
print("doin' alright")
print("aku suka dipanggil 'Vybii'")
print('aku suka dipanggil "Vybii"')

#keluarkan data dari variabel langsung
a = "halo"
print(a)

#string beberapa line sekaligus pakai tanda kutip
a = """aku suka bahasa pemograman python doang
aku agak malas belajar
aku lebih suka tidur
"""
print(a)

a = '''aku suka bahasa pemograman python doang
aku agak malas belajar
aku lebih suka tidur
'''
print(a)

#slicing
b = "Halo, Dunia!"
print(b[1:4])

c = "Hello, Devin!"
print(c[:3])

d = "Halo, Balqis!"
print(b[7:])

e = "Hallo temanku Miku!"
print(b[-3:-7])

#modify
#jadiin huruf kapital semua
a = "jujur ngantuk"
print(a.upper())
#jadiin huruf non-kapital semua
b = "Aku suka tidur"
print(b.lower())
#hilangin semua spasi dan tab di depan dan belakang inputan
c = "       Aku suka push up doang           "
print(c.strip())
#gantu kata
d = "Aku suka makan telur setengah matang"
print(d.replace("u", "i"))
#bikin kalimat jadi terpisah dan dijadikan list
e = "Aku mau makan sekarang. lapar banget"
print(e.split(","))


#Concatenate
#gabungkan 2 variabel jadi 1 variabel
a = "Her"
b = "Lover"
c = a + b
print(c)

#tambahkan sesuatu diantara 2 variabel
a = "Her"
b = "Lover"
c = a + " " + b
print(c)


#Format
umur = 18
txt = f"umur ku {umur} tahun, aku ultah bulan 5"
print(txt)

umur = 18.77
txt = f"umur ku {umur: .7f} tahun, aku ultah bulan 5"
print(txt)

txt = f"aku mau tidur selama {5*4} jam"
print(txt)


#escape char
txt = "\'ini\' penting"
print(txt)


#methods
txt = "KDJALFJALJ"
txt = (txt.isalnum())
print(txt)