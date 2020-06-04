#logicnya mirip dengan segitiga angka yang menerima z = '' kemudian menggunakan loop sebagai iterasi menemukan nilai2 nya sesuai pertambahan i
# 1
# 12
# 123
# 1234

def urai(kata): #menggunakan def dengan menerima satu parameter yaitu kata yg ingin dilakukan looping
    z = '' #inisiasi awal bernilai kososng
    for i in range(len(kata)): #mengiterasi i pada range(len(kata))
        z += kata[:i+1] #menambah hasil kosong tadi dengan indexing i + 1, C , Co, Cod, Code
    return z #mengembalikan nilai z

print(urai("Code"))
print(urai("Python"))
print(urai("Purwadhika"))

def rajut(kata):
    z = '' #inisiasi awal bernilai kosong
    for i in range(len(kata),0,-1): #mengiterasi i pada range start len(kata), end 0 yang bernilai exclussive, dengan step -1
        z += kata[i-1] #menambahkan hasil kosong tadi dengan indexing i-1, 
        if kata[i-1] == kata[0]: #jika katanya sama maka di break
            break
    return z[::-1] #mengembalikkan nilai z dengan reverse atau ::-1

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))