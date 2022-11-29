data_album = [
    {'id': 0 , 'nama':'HotSpace','stok':20,'harga':200000 , 'group': 'Queen'},
    {'id': 1 , 'nama':'Hebirote','stok':20,'harga':40000 , 'group': 'Jeketi48'},
    {'id': 2 , 'nama':'Fearless','stok':20,'harga':200000 , 'group': 'lesserafim'},
    {'id': 3 , 'nama':'Color*Iz','stok':20,'harga':200000 , 'group': 'IZ*ONE'}
]
def menuawal():  #memakai function def
    while True:  #memakai while true agar menu looping
        print('''
        Welcome to Secret shoop

        List Menu :
        1. Daftar Album
        2. Tambah album
        3. Edit album
        4. Hapus album
        5. Keluar
    ''')
        pilih = input('chose wisely please 1 - 5: ')
        if pilih == '1':
            submenudaftar()
        elif pilih == '2':
            subtambahalbum()
        elif pilih == '3':
            subeditalbum()
        elif pilih  == '4':
            subdeletalbum()
        elif pilih == '5':
            print('Byee dont forget your ward')
            break
        else:
            print(f'Gaada {pilih} Jangan aneh2!')

 

        
def pin():
    pin = [48] # pin kasir
    jmlhpin = 1 #jumlah memasukan pin
    while True: #pake while true supaya bisa looping kaya infernity  
        enter_pin = int(input("Masukan pin sebanyak 2 digit: ")); # minta kode pin
        if (enter_pin) in pin:
        # print("")
                print("Pin benar")   
                menuawal()
    # print("")
        print("pin salah.BYE")   # pemberitahuan pin salah
        jmlhpin += 1
        if jmlhpin == 4:   # ini buat patokan berapa kali pin salah
            print("Sorry, BYE")
        break  

def submenudaftar():
    print (f'''
        List Menu :
        1. Semua daftar album
        2. Cari album
        3. Menu awal
        ''')
    inpsubmenu = input('Chose wisely please [1-3] ')
    if inpsubmenu =="1": 
        print("\nsemua daftar album")
        daftar_album()
        submenudaftar()
    elif inpsubmenu =="2": 
        print("\n cari album ")
        cari_album()
    elif inpsubmenu == "3": 
        print("\nByee")
        menuawal()

def daftar_album():

    print('\nDaftar Album')
    print(f'{"id":<11}| {"Nama":<11}| {"Stok":<11}| {"Harga":<11}| {"Group":<11}')
    for i in range(len(data_album)):
        id = data_album[i]['id']
        nama = data_album[i]['nama']
        stok = data_album[i]['stok']
        harga = data_album[i]['harga']
        group = data_album[i]['group']
        print(f'{id:<11}| {nama:<11}| {stok:<11}| {harga:<11}| {group:<11}')

def cari_album():
    idalbum = int(input("\tMasukkan id album:"))         
    for i in range(len(data_album)):
        if idalbum == data_album[i]['id']:
             print(data_album[idalbum])
             submenudaftar()
        # else:
    print ('salah')
    submenudaftar()     

def subtambahalbum():
    while True:
        print(''' 
        1. Tambah Data Album
        2. Kembali ke Menu Utama
        ''')
        pilihan2 = input('Chose wisely [1-2]: ')
        if pilihan2 == '1':
            tambahalbum()
        elif pilihan2 == '2':
            menuawal()
        else:
            print(f'Gaada {subtambahalbum} !')

def tambahalbum():
    while True:
        id = int(input('Masukan id album: '))
        for id in range(len(data_album)):
            print(f'Data {id} sudah ada.')
        else:
            break
        
    nama_album = input('Masukan Nama album: ').title()
    stock_album = int(input('Masukan stock album: '))
    harga_album = int(input('Masukan harga album: '))
    group_baru = input('Masukan nama group: ').title()
    album_baru = [id, nama_album, stock_album, harga_album, group_baru]
        
    while True:
        dataUpdate = input('Apakah data akan disimpan [y/n]: ').upper()
        if dataUpdate == 'Y':
            print('Data Tersimpan')
            subtambahalbum()
        elif dataUpdate == 'N':
            print('Data Tidak Tersimpan')
            tambahalbum()
        else:
            print(f'Pilihan {dataUpdate} tidak tersedia!')
        for i, item in enumerate(album_baru):
            data_album.append(item)

def subeditalbum():
    while True:
        print(''' 
        1. Edit Album
        2. Kembali ke Menu Utama
        ''')
        inpsubedit = input('Chose wisely [1-2]: ')
        if inpsubedit == '1':
            updatealbum()
        elif inpsubedit == '2':
            menuawal()
        else:
            print(f'Gaada {subeditalbum} Jangan aneh2!')


def updatealbum():
    updtid= int(input("\masukan id album"))
    for i in range(len(data_album)):
        if updtid == data_album[i]['id']:
            print(data_album[updtid])
            global inptkolom
            inptkolom = input('masukan nama kolom ')
            global inptkolom2
            inptkolom2 = input('value :')
            data_album [updtid][inptkolom] = inptkolom2
        else:
            print('salah')
    while True:
        dataUpdate = input('Apakah data akan disimpan [y/n]: ').upper()
        if dataUpdate == 'Y':
            print('Data Terupadte')
            subtambahalbum()
        elif dataUpdate == 'N':
            print('Data Tidak Terupdate')
            tambahalbum()
        else:
            print(f'Pilihan {dataUpdate} tidak tersedia!')
               

def subdeletalbum():
    while True:
        print(''' 
        1. Delete Data Album
        2. Kembali ke Menu Utama
        ''')
        inputdeletalbum = input('Chose wisely (1&2): ')
        if inputdeletalbum == '1':
            deletalbum()
        elif inputdeletalbum == '2':
            menuawal()
        else:
            print(f'Gaada {subtambahalbum} Jangan aneh2!')

def deletalbum():
    delid= int(input("\masukan id album"))
    for i in range(len(data_album)):
        if delid == data_album[i]['id']:
            print(data_album[delid])
    data_album.pop(delid)
    while True:
        deletedata = input('Apakah data akan dihapus [y/n]: ').upper()
        if deletedata == 'Y':
            print('Data Terhapus')
            subdeletalbum()
        elif deletedata == 'N':
            print('Data Tidak Terhapus')
            deletalbum()
        else:
            print(f'Pilihan {deletedata} tidak tersedia!')
    
pin()
