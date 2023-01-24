nim = []
nama = []
prodi = []

def pilihannya():
    print('\nSilahkan pilih menu yang tersedia : ')
    print ("1. masukan data.")
    print ("2. tampilkan data.")
    print ("3. update data.")
    print ("4. hapus data.")
    print ("0. logout.")
    pilihan = int(input('Masukkan Pilihanmu : '))
    if pilihan == 1:
        masukkan_data()
    elif pilihan== 2:
        tampilkan_data()
    elif pilihan == 3:
        ubah_data()
    elif pilihan == 4:
        hapus_data()
    elif pilihan == 0:
        print('Aplikasi akan dimatikan.....')
        quit()
    else :
        print("Input yang dimasukkan salah, ulangi!")
        pilihannya()

def masukkan_data():
    masnim = input("masukan nim : ")
    nim.append(masnim)
    masnama = input("masukan nama : ")
    nama.append(masnama)
    masprodi = input("masukan prodi : ")
    prodi.append(masprodi)
    pilihannya()

def tampilkan_data() :
    print('nim : ', *nim, sep=' |')
    print('nama : ', *nama, sep=' |')
    print('prodi : ', *prodi, sep=' |')
    out = eval(input('tekan angka apapun untuk kembali ke menu awal : '))
    if out == 1:
        pilihannya()
    else :
        pilihannya()

def ubah_data():
    ubahdata= int(input('''
Silahkan pilih data yang ingin dirubah :
1. NIM
2. Nama
3. prodi
Masukan pilihan disini : '''))
    if ubahdata == 1:
        pilubah = eval(input('Pilih data NIM ke-berapa yang ingin di update : '))
        l = pilubah
        if pilubah == l:
            updetnim = int(input('Masukan NIM yang baru : '))
            j = updetnim
            if updetnim == j:
                nim[l]= updetnim
                print ('Data NIM ke', l,'telah diubah menjadi',updetnim)
                out = eval(input('tekan angka apapun untuk kembali ke menu awal : '))
                if out == 1:
                    pilihannya()
                else :
                    pilihannya()
    if ubahdata == 2:
        pilubah = eval(input('Pilih data Nama ke-berapa yang ingin di update : '))
        l = pilubah
        if pilubah == l:
            updetnama = str(input('Masukan Nama yang baru : '))
            j = updetnama
            if updetnama == j:
                nama[l]= updetnama
                print ('Data Nama ke', l,'telah diubah menjadi',updetnama)
                out = eval(input('tekan angka apapun untuk kembali ke menu awal : '))
                if out == 1:
                    pilihannya()
                else :
                    pilihannya()
    if ubahdata == 3:
        pilubah = eval(input('Pilih data prodi ke-berapa yang ingin di update : '))
        l = pilubah
        if pilubah == l:
            updetprodi = str(input('Masukan Prodi yang baru : '))
            j = updetprodi
            if updetprodi == j:
                prodi[l]= updetprodi
                print ('Data prodi ke', l,'telah diubah menjadi',updetprodi)
                out = eval(input('tekan angka apapun untuk kembali ke menu awal : '))
                if out == 1:
                    pilihannya()
                else :
                    pilihannya()        
    pilihannya()

def hapus_data():
        masnim = int(input("masukan data NIM ke berapa yang ingin dihapus : "))
        masnama = int(input("masukkan data Nama ke berapa yang ingin dihapus : "))
        masprodi = int(input("masukkan data Prodi ke berapa yang ingin dihapus : "))
        k = masnim
        l = masnama
        m = masprodi
        del nim[k]
        del nama[l]
        del prodi[m]
        out = eval(input('tekan apapun untuk kembali ke menu awal : '))
        if out == 1:
            pilihannya()
        else :
            pilihannya()

pilihannya()