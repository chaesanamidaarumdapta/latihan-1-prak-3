print('ayo kita cek apa jenis segitiga')

x = float(input('masukkan panjang sisi tegak segitiga'))
y = float(input('masukkan panjang sisi bawah segitiga'))
z = float(input('masukkan panjang sisi miring segitiga'))

if x == y == z :
    print('ini merupakan segitiga sama sisi')
elif (x == y) or (y == z) or (x == z):
    print('ini merupakan segitiga sama kaki')
elif (x + y <= z) or (x + y <= z) or (y + z <= x):
    print('tidak membentuk segitiga')
else : 
    print('merupakan segitiga sembarang')
