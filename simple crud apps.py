##################################### BAGIAN DEF FUNCTION #####################################
## FUNGSI INTRO MENU
def intromenu():
    status_intromenu = False
    while status_intromenu == False:
        try:
            input_menu_utama = int(input("Selamat Datang di Mini Apps V 2.0 \nDaftar Menu: \n 1. Register \n 2. Login \n 3. Exit Aplikasi\nSilahkan Input Pilihan Aktivitas Anda: "))
            if input_menu_utama > 3:
                print("Pilihan Menu Anda Diluar Jangkauan")
                print("")
            elif input_menu_utama < 0:
                print("Pilihan Menu Anda Diluar Jangkauan")
                print("")
            elif input_menu_utama == 1:
                status_intromenu = True
                menu_utama1()
            elif input_menu_utama == 2:
                status_intromenu = True
                menu_utama2()
            elif input_menu_utama == 3:
                status_intromenu = True
                menu_utama3()
        except:
            print("Input Anda Harus Berupa Bilangan Bulat")
            print("")

## FUNGSI APPS MINI V1.0 TOKO BUAH
def crud2():
    data = {
        "Jeruk":1,
        "Apel":2, 
        "Pisang":3,
        "Anggur":5
        }

    ####Syntax Untuk Menu Utama
    # menu_universal = ""
    def PilihanMenu():
        status = "True"
        while status == "True":
            print("")
            print("Selamat Datang di Menu Mini Aplikasi Toko Subur")
            print("")
            print("1. Cetak Isi Daftar Barang")
            print("2. Menambah Data Barang")
            print("3. Mengubah Data Barang")
            print("4. Menghapus Data Barang")
            print("5. Keluar Aplikasi")
            print("")
            try:
                user_input = int(input("Masukkan Pilihan Menu yang Ingin Anda Akses :"))
                if user_input == 1:
                    print("")
                    print("Anda Memilih Pilihan Menu 1 (Cetak Isi Daftar Barang)")
                    menu_1()
                    mini_menu(user_input)
                    status = "False"
                elif user_input == 2:
                    print("")
                    print("Anda Memilih Pilihan Menu 2 (Menambah Data Barang)")
                    menu_2()
                    mini_menu(user_input)
                    status = "False"
                elif user_input == 3:
                    print("")
                    print("Anda Memilih Pilihan Menu 3 (Mengubah Data Barang)")
                    menu_3()
                    mini_menu(user_input)
                    status = "False"
                elif user_input == 4:
                    print("")
                    print("Anda Memilih Pilihan Menu 4 (Menghapus Data Barang)")
                    menu_4()
                    mini_menu(user_input)
                    status = "False"
                elif user_input == 5:
                    print("")
                    print("Anda Memilih Pilihan Menu 5 (Exit)")
                    print("Terima Kasih")
                    status = "False"
                else:
                    print("")
                    print("Anda Harus Memasukkan Angka yang Terdapat Dalam Menu")
            except:
                print("")
                print("Maaf, Anda Harus Memasukkan Angka Untuk Memilih Menu")
        return user_input


    #### Syntax Untuk Menu 1
    def menu_1():
        print("")
        print("Selamat Datang Di Menu 1 Mencetak Daftar Barang")
        if data == {}:
            print("Maaf, Daftar Barang Masih Kosong")
        else:
            print("Terlampir data yang anda punya", data)
            print(" ")

    #### Syntax Untuk Menu 2
    def menu_2():
        print("")
        print("Selamat Datang Di Menu 2 Menambah Daftar Barang")

        loop2=True
        while loop2:
            buahbaru = str(input('Masukkan Nama Buah Baru Yang Ingin Anda Masukkan: ')).capitalize()
            user_replace = buahbaru.replace(' ','')
            
            if user_replace.isalpha():
                if buahbaru in data.keys():
                    print('Tidak Bisa Input Data Yang Sudah Terdaftar')
                    print("")
                else:
                    loop3 = True
                    while loop3:
                        input_stock = input("Masukkan Jumlah Stok Barang :")
                        if input_stock.isdigit():
                            input_stock = int(input_stock)
                            data[buahbaru] = input_stock
                            break
                        else:
                            print("Anda Harus Memasukan Angka Bulat Untuk Stok Barang")
                            print("")
            else:
                print('Format Nama Buah Yang Anda Masukkan harus Alphabet')
                print("")
            break
        

    #### Syntax Untuk Menu 3
    def menu_3():
        print("")
        print("Selamat Datang Di Menu 3 Update Barang")
        status = "True"
        while status == "True":
            print("1. Mengubah Nama Data Barang")
            print("2. Mengubah Stok Barang")
            try:
                inputupdate = int(input("Masukkan Opsi yang Anda Inginkan: "))
                if inputupdate == 1:
                    barang = str(input("Masukan Nama Barang Lama yang Ingin Diganti: ")).capitalize()
                    if barang in data.keys():
                        inputbarangbaru = input("Masukkan Nama Barang Baru: ").capitalize()
                        data[inputbarangbaru] = data[barang]
                        data.pop(barang)
                        status = "False"
                    else:
                        print("Barang yang Akan Diganti Tidak Terdaftar")
                        print("")
                elif inputupdate == 2:
                    statusupdatebarang = True
                    while statusupdatebarang == True:
                        barang = str(input("Masukan Nama Barang yang Akan Diupdate Stok: ")).capitalize()
                        if barang in data.keys():
                            status_update_stok = True
                            statusupdatebarang = False
                            while status_update_stok == True:
                                try:
                                    stokbaru = int(input("Masukkan Jumlah Tambahan Stok Barang Baru: "))
                                    if data[barang] + stokbaru < 0:
                                        print("Angka Stok Barang Tidak Bisa Negatif")
                                    else:
                                        data[barang] = data[barang] + stokbaru
                                        status_update_stok = False
                                        status = "False"
                                except:
                                    print("Anda Harus Memasukan Angka Bulat Untuk Stok Barang")
                                    print("")
                        else:
                            print("Barang yang Akan Diupdate Tidak Terdaftar Dalam List Barang")
                            print("")
            except:
                print("Pilihan yang Anda Masukkan Salah. Hanya menerima 1 atau 2")
                print("")

                
    #### Syntax Untuk Menu 4
    def menu_4():
        print("")
        print("Selamat Datang di Menu 4 Hapus Data")
        print("")
        status = "True"
        while status == "True":
            print("1. Menghapus Seluruh Data")
            print("2. Menghapus Sebagian Data")
            try:
                inputhapus = int(input("Masukkan Pilihan Anda: "))
                if inputhapus == 1:
                    data.clear()
                    status = 'False'
                elif inputhapus == 2:
                    statushapusbarang = True
                    while statushapusbarang == True:
                        baranghapus = str(input("Masukan Nama Barang yang Akan Dihapus Stoknya: ")).capitalize()
                        if baranghapus in data.keys():
                            del data[baranghapus]
                            print(f'{baranghapus} Berhasil Dihapus')
                            print('')
                            statushapusbarang = False                    
                        else:
                            print('Barang Tidak Ditemukan')
                            print("")
                    status = 'False'
            except:
                print("Pilihan yang Anda masukkan salah. Hanya menerima 1 atau 2")
                print("")


    #### Syntax Untuk Mini_Menu
    def mini_menu(x):
        status = "True"
        while status == "True":
            print("")
            print("Silahkan Pilih Aktivitas Anda Berikutnya")
            print("1. Kembali Melakukan Menu ini")
            print("2. Kembali Ke Menu Utama")
            print("")
            try:
                user_input_mini_menu = int(input("Masukkan Pilihan Mini Menu yang Ingin Anda Akses :"))
                if user_input_mini_menu == 1:
                    if x == 1:
                        menu_1()
                        mini_menu(1)
                        status = "False"
                    elif x == 2:
                        menu_2()
                        mini_menu(2)
                        status = "False"
                    elif x == 3:
                        menu_3()
                        mini_menu(3)
                        status = "False"
                    elif x == 4:
                        menu_4()
                        mini_menu(4)
                        status = "False"
                elif user_input_mini_menu == 2:
                    PilihanMenu()
                    status = "False"
                else:
                    print("")
                    print("Anda Harus Memasukkan Angka yang Terdapat Dalam Menu")
            except:
                print("")
                print("Maaf, Anda Harus Memasukkan Angka Untuk Memilih Menu")

    PilihanMenu()

## FUNGSI SUB MENU (KEMBALI KE MENU UTAMA ATAU re-access APLICATION)
def sub_menu_loop():
    status = False
    while status == False:
        try: 
            input_submenu_loop = int(input("Apakah Anda Tetap Ingin Menggunakan Sub-Menu Ini?: \n 1 = Ya  \n 2 = Tidak \n Pilihan Anda: "))
            if input_submenu_loop == 1:
                return 1
                status = True
            elif input_submenu_loop == 2:
                return 2
                status = True
            elif input_submenu_loop < 1 :
                print("Pilihan Diluar Jangkauan")
            elif input_submenu_loop > 2:
                print("Pilihan Diluar Jangkauan")
        except:
            print("Input Harus Berupa Angka")
            print("")
            
## FUNGSI MENU LOGIN
def printmenuandgetresponse():
    status_menu_login = False
    while status_menu_login == False:
        try:
            print("Daftar List Aplikasi Mini Apps V 2.0")
            print("1. User Profile")
            print("2. Kalkulator")
            print("3. Konversi Romawi")
            print("4. Konversi Kode Morse")
            print("5. Kalkulator Hari")
            print("6. Kamus Hari")
            print("7. Konversi Jumlah Hari ke Tahun, Bulan, Minggu, Hari")
            print("8. Kalkulator Faktorial")
            print("9. Jumlah dan Deret Fibonnaci")
            print("10. Caesar Cipher")
            print("11. Setting User")
            print("12. Menu CRUD")
            print("13. Logout")
            input_menu_login = int(input("Silahkan Input Pilihan Aplikasi Anda: "))
            if input_menu_login > 13:
                print("Pilihan Menu Anda Diluar Jangkauan")
                print("")
            elif input_menu_login < 0:
                print("Pilihan Menu Anda Diluar Jangkauan")
                print("")
            elif input_menu_login == 1:
                status_menu_login = True
                return 1
            elif input_menu_login == 2:
                status_menu_login = True
                return 2
            elif input_menu_login == 3:
                status_menu_login = True
                return 3
            elif input_menu_login == 4:
                status_menu_login = True
                return 4
            elif input_menu_login == 5:
                status_menu_login = True
                return 5
            elif input_menu_login == 6:
                status_menu_login = True
                return 6
            elif input_menu_login == 7:
                status_menu_login = True
                return 7
            elif input_menu_login == 8:
                status_menu_login = True
                return 8
            elif input_menu_login == 9:
                status_menu_login = True
                return 9
            elif input_menu_login == 10:
                status_menu_login = True
                return 10
            elif input_menu_login == 11:
                status_menu_login = True
                return 11
            elif input_menu_login == 12:
                status_menu_login = True
                return 12
            elif input_menu_login == 13:
                status_menu_login = True
                return 13
        except:
            print("Input Anda Harus Berupa Bilangan Bulat")
            print("")

## FUNGSI FILTER USERNAME
def FilterUsername(user_id_input):
    if user_id_input.isalnum() and not user_id_input.isalpha() and not user_id_input.isdigit():
        if user_id_input in personal_info["UserID"]:
            return "Username Sudah Terpakai"
        else:
            if len(user_id_input) > 20:
                return "Username Tidak Boleh Lebih dari 20 karakter"
            elif len(user_id_input) < 6:
                return "Username Tidak Boleh Kurang dari 6 karakter"
            else:
                return "Username: ({}) tersedia ".format(user_id_input)
    else:
        return "Username Harus Hanya Kombinasi Huruf dan Angka"

## FUNGSI VALIDASI EMAIL
import re
def validate_email(email):
    ## Jumlah @ hanya boleh 1
    if email.count("@") > 1:
        return "Format Email Anda Tidak Valid (Jumlah @ hanya boleh 1)"
    elif email.count("@") <1 :
        return "Format Email Anda Tidak Valid (Email Harus Mengandung @)"
    else:
        ##Check user checker if first character is number or alphabet
        split_user_and_hosting = email.split("@")
        #Check existance of username
        if split_user_and_hosting[0] == "" :
            return "Format Email Anda Tidak Valid (Anda Belum Memasukkan Username)"
        else:
            #Check existance of hosting and extension
            if split_user_and_hosting[-1] == "":
                return 'Format Email Anda Tidak Valid (Anda Belum Memasukkan Hosting dan Extension)'
            else:
                #Check existance of extension
                character_after_username = split_user_and_hosting[1]
                if "." not in character_after_username:
                    return 'Format Email Anda Tidak Valid (Anda Belum Memasukkan Extension)'
                if ".." in character_after_username:
                    return 'Format Email Anda Tidak Valid (Extension Anda Salah)'
                else:

                    split_hosting_and_extension = character_after_username.split(".")
                    extension_only = split_hosting_and_extension[1:]
                    user_only_character = split_user_and_hosting[0]

                    #Check first digit of username
                    if list(email)[0].isalnum() == True:
                        #Check username only receive alphabet, number, underscore, and dot
                        if re.match("^[A-Za-z0-9_.]*$", user_only_character):
                            #Check hosting
                            hosting_only = split_hosting_and_extension[0]
                            if re.match("^[0-9]*$", hosting_only):
                                return "Format Email Anda Tidak Valid (Hosting Tidak Bisa Hanya Numerik)"

                            elif re.match("^[A-Za-z0-9]*$", hosting_only):
                                #check ext
                                if len(extension_only)>2:
                                    return "Format Email Anda Tidak Valid (Extension Lebih dari 2)"
                                else:
                                    ext_merge = "".join(extension_only)
                                    if ext_merge.isalpha() == False:
                                        return 'Format Email Anda Tidak Valid (Extension Tidak Menerima Angka)'
                                    else:
                                        extension_only.sort(key = len, reverse= True)
                                        for x in extension_only:
                                            if len(x) >= 6 :
                                                return "Format Email Anda Tidak Valid (Format Extension Anda Salah)"
                                                
                                            else:
                                                return "{} bisa dipakai".format(email)
                                
                            else:
                                return "Format Email Anda Tidak Valid (nama hosting hanya boleh huruf atau kombinasi dengan angka)"
                        else:
                            return "Format Email Anda Tidak Valid (username hanya menerima alfabet, nomor, underscore dan dot)"
                    else:
                        return "Format Email Anda Tidak Valid (elemen pertama username hanya boleh angka dan huruf)"

## FUNGSI KALKULATOR
def fungsi_kalkulator():
    def penjumlahan(x,y):
        return x + y 

    def pengurangan(x,y):
        return x - y

    def perkalian(x,y):
        return x * y 

    def pembagian (x,y):
        if y == 0:
            return "Infinite"
        return x / y ### Belum handling infiniti

    angka1_input = input("Masukkan Angka Pertama :")
    angka2_input = input("Masukan Angka Kedua :")

    try:
        angka1 = float(angka1_input)
        angka2 = float(angka2_input)
        operator = input("Masukkan Operator (+ or / or - or *) :")

        if operator == "+":
            print("Hasil Penjumlahan", angka1, "dan", angka2, "adalah", penjumlahan(angka1, angka2))        
        elif operator == "-":
            print("Hasil Pengurangan", angka1, "dan", angka2, "adalah", pengurangan(angka1, angka2)) 
        elif operator == "*":
            print("Hasil Perkalian", angka1, "dan", angka2, "adalah", perkalian(angka1, angka2))
        elif operator == "/":
            print("Hasil Pembagian", angka1, "dan", angka2, "adalah", pembagian(angka1, angka2))
        else: 
            print("Operator yang Anda Masukkan Salah")
    except:
        print("Anda Harus Memasukan Angka")

## FUNGSI TRANSLATOR HARI
def fungsi_translator_hari():
    hari = {
        "senin" : "monday",
        "selasa" : "tuesday",
        "rabu" : "wednesday",
        "kamis" : "thursday",
        "jumat" : "friday",
        "sabtu" : "saturday",
        "minggu" : "sunday"
    }

    hari_input = input("Masukkan Nama Hari (Please Input Name Of Day):")
    hari_input = hari_input.replace(" ", "")

    for i in hari_input:
        if i.isalpha() == False:
            print("Maaf, tidak menerima input selain String (Sorry, we don't accept input other than string)")
            break
    else:   
        for i, j in hari.items():
            if hari_input.lower() == i:
                print("Hari yang anda pilih", i.capitalize() , "dalam Bahasa Inggris adalah", j.capitalize())
                break
            elif hari_input.lower() == j:
                print("The day that you choose is", j.capitalize(), "in Bahasa means", i.capitalize())
                break
        else:
            print("Maaf nama hari yang anda masuskkan tidak terdaftar (Sorry name of day that you input is out of range)")

## FUNGSI KALKULATOR HARI 
def fungsi_kalkulator_hari():
    daftar_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    input_hari = input("Masukkan Nama Hari :")
    input_jumlah = input("Masukkan Jumlah Hari :")

    try: 
        hari = str(input_hari)
        jumlah = int(input_jumlah)

        hari_capitalize = hari.capitalize()
        jumlah_abs = abs(jumlah)
        
        if hari_capitalize not in daftar_hari:
            print("Nama Hari Tidak Terdaftar")
        else:
            index_baru = daftar_hari.index(hari_capitalize) + jumlah
            while index_baru > 6:
                index_baru -= 7
            while index_baru < 0:
                index_baru += 7
            if jumlah >= 0:
                print("Hari ini", hari_capitalize, ",", jumlah, "hari lagi hari", daftar_hari[index_baru])
            else:
                print("Hari ini", hari_capitalize, ",", jumlah_abs, "hari yang lalu adalah", daftar_hari[index_baru])
    except:
        print("Angka yang anda masukkan salah")

## FUNGSI KONVERSI HARI 
def fungsi_konversi_hari():
    try: 
        jumlah_hari = int(input("Masukkan Jumlah Hari:"))

        if (jumlah_hari > 4000):
            print("Jumlah hari diatas batas")
        elif (jumlah_hari < 0):
            print("Jumlah hari dibawah batas")
        else:
            tahun = jumlah_hari // 365
            bulan = (jumlah_hari % 365) // 30
            minggu = ((jumlah_hari % 365) % 30) // 7
            hari = (((jumlah_hari % 365) % 30) % 7)
            print("{:0>2d}".format(tahun), "tahun", "{:0>2d}".format(bulan), "bulan", "{:0>2d}".format(minggu), "minggu", "{:0>2d}".format(hari), "hari")
    except:
        print("Jumlah hari yang anda masukkan salah")

## FUNGSI KALKULATOR FAKTORIAL
def fungsi_kalkulator_faktorial():
    status = False
    while status == False:
        try:
            input_factorial = int(input("Silahkan Masukkan Angka yang Ingin Anda Faktorial : "))
            if input_factorial < 0:
                print("Maaf, Faktorial Tidak Menerima Angka Negatif")
            elif input_factorial == 0:
                print("Hasil Faktorial 0 adalah 1")
                status = True
            else:
                nilai_factorial = 1
                for i in range(1, input_factorial + 1):
                    nilai_factorial = nilai_factorial * i 
                print("Hasil Faktorial adalah", nilai_factorial)
                status = True
        except:
            print("Angka Yang Anda Masukkan Harus Angka Bulat")

## FUNGSI KONVERTER ROMAWI
def fungsi_konversi_romawi():
    roman_dic= {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
        }

    def int_rom(Q):
        arabic = {}
        for i, j in roman_dic.items():
            arabic[j] = i
        roman = ""
        for i in arabic.keys():
            count = int(Q / i)
            roman += arabic[i] * count
            Q -= i * count
        return roman

    def rom_int(Q):
        i = 0
        number = 0
        while i < len(Q): 
            if i<len(Q) and Q[i:i+2] in roman_dic: 
                number+=roman_dic[Q[i:i+2]]
                i+=2
            else:
                number+=roman_dic[Q[i]]
                i+=1
        if int_rom(number) != Q:
            return "Angka romawi tidak valid"
        else:
            return number

    angka=input("Masukan angka romawi atau integer : ")
    try:
        if angka.isalpha():
            angka=angka.upper()
            for i in angka:
                if not(i == 'I' or i =='V' or i == 'X' or i=='L' or i=='C' or i =='D' or i=='M'):
                    print('angka romawi salah')
                    break
                else:
                    continue
            print(rom_int(angka)) 
        else:
            angka=int(angka)
            if angka < 0 :
                print('gak boleh negatif')
            else:
                print(int_rom(angka))
    except:
        print("tidak menerima float")

## FUNGSI MORSE
def fungsi_morse():
    morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
    }

    Input = input("Masukkan kalimat/kode Morse : ")
    inputnya_itu_kalimat = False

    ## Pengecekkan Input adalah Kalimat atau Kode Morse
    for i in Input:
        if i != "." and i != "-" and i != " " and i != "/":
            inputnya_itu_kalimat = True
            break
    else: ## Konversi Kode Morse ke Kalimat
        try:
            # morse2 = dict((y,x) for x,y in morse.items())
            morse2 = {}
            for i,j in morse.items():
                morse2[j] = i
            # kalimat = []
            for x in Input.split(" "):
                huruf = ""
                kode_kata = x.split("/")
                # if kode_kata[-1] == "":
                #     kode_kata.pop(-1) # Menghapus karakter "" akibat splitting
                for y in kode_kata:
                    huruf = huruf + morse2[y]
                # kalimat.append(huruf)
            print(f"Kode Morse yg anda masukkan {Input} Hasil konversi menjadi kata-kata adalah :")
            print(huruf)
            # print(" ".join(kalimat).capitalize())
        except:
            print("Format Kode Morse Salah / Kode Morse Tidak Ada")

    ## Konversi Kalimat ke Kode Morse
    if inputnya_itu_kalimat == True:
        for x in Input.split(" "): ## Mengecek kalimat hanya alfa + num + space
            if x.isalnum() != True:
                print("Hanya menerima Alfabet, Angka dan Spasi")
                break
        else:
            katakata = Input.lower().split() # List kata - kata
            morse_kalimat = []
            # for kata in katakata:
            #     morse_kata = ""
            #     for huruf in kata:
            #         morse_kata = morse_kata + morse[huruf] + "/" 
            #     morse_kalimat.append(morse_kata)
            # print(" ".join(morse_kalimat))
            for kata in katakata:
                morse_kata = []
                for huruf in kata:
                    morse_kata.append(morse[huruf]) 
                morse_kalimat.append("/".join(morse_kata))
            print(f"Kalimat yg anda masukkan adalah '{Input}'. Kode Morsenya adalah :")
            print(" ".join(morse_kalimat))

## FUNGSI DERET FIBONACI
def fungsi_fibonnaci():
    
    def FFibonaci(x):
        angka_akses = x
        deret_fibonaci = []

        for i in range(0, angka_akses+1):
            if i == 0 or i == 1:
                deret_fibonaci.append(i)
            else:
                angka_berikutnya = deret_fibonaci[i-2] + deret_fibonaci[i-1]
                deret_fibonaci.append(angka_berikutnya)
        return deret_fibonaci
        
    try:
        input_deret_fibonaci = int(input("Masukkan Angka :"))
        if input_deret_fibonaci < 0:
            print("Maaf, Anda Harus Memasukan Angka Positif")
        else:
            list_deret_fibonaci = list(FFibonaci(input_deret_fibonaci))
            from functools import reduce 
            print(input_deret_fibonaci, "Angka Pertama dari Deret Fibonaci adalah", list_deret_fibonaci, "dan jumlahnya", reduce(lambda x, y : x + y, list_deret_fibonaci))
    except:
        print("Maaf, Anda Harus Memasukkan Angka Bulat")

## FUNGSI CAESAR CHIPER
def fungsi_caesar_chiper():
    def CaesarCipher(x,y):
        alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        kata_baru = []
        kata = x.lower()
        angka = y

        for i in kata:
            index = alfabet.index(i)
            index_baru = (index + angka) % 26
            kata_baru.append(alfabet[index_baru])
        return "".join(kata_baru)

    try:
        kata = input("Masukkan Kata :")
        angka = int(input("Masukan Angka :"))
        if " " in kata:
            print("Tidak menerima kalimat")
        elif kata.isalpha() == False:
            print("Kata yang diinput salah, hanya menerima alfabet dan tidak menerima kalimat")
        else:
            print(CaesarCipher(kata,angka))
    except:
        print("Angka yang dimasukkan salah, hanya menerima angka bulat")

##################################### BAGIAN DATABASE SYSTEM #####################################

personal_info = {"UserID":['tesloginlogin12',],
"Password" : ['Fajar_123'],
"Email":['login@gmail.com'],
"Nama": ['tes login'],
"Gender": ['male'],
"Usia":['25'],
"Pekerjaan":['Data Science'],
"Hobi": [['Main Game','Olahraga','Baca Buku']],
"Alamat":{
    "Kota": ['Jakarta'],
    "RT" : ['008'],
    "RW" : ['009'],
    "Zipcode" :['13410'],
    "Geo": {
        "Latitude" : ['6.2088°'],
        "Longitude": ['106.8456°']
        }
    },
"No HP": ['0821291378']
}

#################### FUNGSI MENU UTAMA NO 1(REGISTER) ########################  
def menu_utama1():
    print("")
    print("=================Registrasi=================")
    #### VALIDASI USERNAME
    test_username = False
    while test_username == False:
        user_id_input = input("Masukkan UserID: ").lower()
        validatinguser = FilterUsername(user_id_input)
        print(validatinguser)
        if validatinguser == "Username: ({}) tersedia ".format(user_id_input):
            test_username = True
        else:
            test_username = False

    #### VALIDASI PASSWORD
    initial_test_password = False
    while initial_test_password == False:
        password_input = input("Masukkan Password: ")

        jumlah_angka = 0
        jumlah_huruf_kecil = 0
        jumlah_huruf_besar = 0
        jumlah_karakter_khusus = 0

        import string

        for i in password_input:
            cek_digit = i.isdigit()
            if cek_digit == True:
                jumlah_angka += 1

            cek_huruf_kecil = i.islower()
            if cek_huruf_kecil == True:
                jumlah_huruf_kecil +=1
            
            cek_huruf_besar = i.isupper()
            if cek_huruf_besar == True:
                jumlah_huruf_besar +=1
            
            if i in string.punctuation:
                jumlah_karakter_khusus +=1

        if len(password_input) < 8:
            print("Password Minimal 8 Karakter")
        elif jumlah_angka == 0:
            print("Password Harus Mengandung Angka")
        elif jumlah_huruf_besar == 0:
            print("Password Harus Mengandung 1 Huruf Kapital")
        elif jumlah_huruf_kecil == 0:
            print("Password Harus Mengandung 1 Huruf Kecil")
        elif jumlah_karakter_khusus == 0:
            print("Password Harus Mengandung 1 Karakter Khusus")
        else:
            initial_test_password = True
    
    ####VALIDASI EMAIL
    initial_test_email = False
    while initial_test_email == False:
        email = input("Masukkan Email: ")
        validating = validate_email(email)
        print(validating)
        if validating == "{} bisa dipakai".format(email):
            personal_info["Email"].append(email)
            initial_test_email = True
        else:
            print("Anda Perlu Menginput Ulang Dengan Format yang Benar")
            initial_test_email = False
    
    ####VALIDASI NAMA
    testnama = False       
    while testnama == False:
        nama_input = input("Masukkan Nama Anda: ").capitalize()
        namaspasi = nama_input.replace(" ", "")
        if namaspasi.isalpha():
            testnama = True
        else:
            print("Input Nama Harus berupa Alfabet")
            testnama = False

    #### VALIDASI GENDER
    gender_input = input("Masukkan Gender Anda (Hanya Male atau Female): ").capitalize()
    while gender_input != "Male" and gender_input != "Female":
        print("Gender Hanya Bisa Diisi Male/Female")
        gender_input = input("Masukkan Gender Anda (Hanya Male atau Female): ").capitalize()
    
    #### VALIDASI USIA
    initial_test_usia = False
    while initial_test_usia == False:
        try:
            usia = int(input("Masukkan Usia Anda: "))
            if usia < 17:
                print("Minimal Input Usia 17 tahun")
                initial_test_usia = False
            elif usia > 80:
                print("Maksimal Input Usia 80 tahun")
                initial_test_usia = False
            else:
                initial_test_usia = True
        except:
            print("Input Umur Hanya Boleh Berupa Angka Bulat ")
        
    #### VALIDASI PEKERJAAN
    initial_test_pekerjaan = False       
    while initial_test_pekerjaan == False:
        pekerjaan_input = input("Masukkan Pekerjaan Anda: ").capitalize()
        pekerjaan_spasi = pekerjaan_input.replace(" ", "")
        if pekerjaan_spasi.isalpha():
            initial_test_pekerjaan = True
        else:
            print("Input Pekerjaan Harus berupa Alfabet")
            initial_test_pekerjaan = False

    #### VALIDASI HOBI
    hobiloop=True
    while hobiloop:
        hobi_input_1 = input("Masukkan Hobi Anda: ").capitalize()
        if not hobi_input_1.isalpha():
            print('Hobi Hanya Boleh Diisi Alphabet')
            continue
        else:
            hobi_input_2 = input("Masukkan Hobi Lain: ").capitalize()
            if not hobi_input_2.isalpha():
                print('Hobi Hanya Boleh Diisi Alphabet')
                continue
            
        kosong = []
        kosong.append(hobi_input_1)
        kosong.append(hobi_input_2)
        
        while True:
            ask = input("Apakah Anda Mau Memasukkan Hobi Lain? (Y/N): ").upper()
            
            if ask == 'Y':
                hobi_lain = input("Masukkan Hobi Lain: ").capitalize()
                if not hobi_lain.isalpha():
                    print('Hobi Hanya Boleh Diisi Alphabet')
                else:
                    kosong.append(hobi_lain)
            elif ask == 'N':
                break
            else:
                print('Maaf, Anda Harus Masukkan Y atau N')              
        break
        
    
    #### VALIDASI KOTA
    initial_test_kota = False       
    while initial_test_kota == False:
        Kota_input = input("Masukkan Kota: ").capitalize()
        kota_spasi = Kota_input.replace(" ", "")
        if kota_spasi.isalpha():
            initial_test_kota = True
        else:
            print("Input Kota Harus Berupa Alfabet")
            initial_test_kota = False   

    #### VALIDASI RT
    testRT = False       
    while testRT == False:
        try:
            RT_input = int(input("Masukkan Nomor RT: "))
            if RT_input > 999 or RT_input < 0: 
                print("Nomor RT yang Anda Masukkan Salah")
            else:
                RT_input = "%03d" % RT_input
                testRT = True 
        except:
            print("Nomor RT Hanya Menerima Angka")
    
    #### VALIDASI RW
    testRW = False       
    while testRW == False:
        try:
            RW_input = int(input("Masukkan Nomor RW: "))
            if RW_input > 999 or RW_input < 0: 
                print("Nomor RW yang Anda Masukkan Salah")
            else:
                RW_input = "%03d" % RW_input
                testRW = True 
        except:
            print("Nomor RW Hanya Menerima Angka")

    #### VALIDASI ZIPCODE
    Zipcode_input = input("Masukkan Kode Pos: ")
    while Zipcode_input.isdigit() == False:
        print("Kode Pos Hanya Dapat Diisi Angka")
        Zipcode_input = input("Masukkan Kode Pos: ")

    Latitude_input = input("Masukkan Latitude : ")
    Longitude_input = input("Masukkan Longitude : ")
    
    #### VALIDASI NO HP
    hpinput = True
    while hpinput:
        No_HP_input = input("Masukkan Nomor Handphone Anda : ")
        if 10<len(No_HP_input)<14:
            if No_HP_input.isdigit():
                break
            else:
                print('No HandPhone Harus Berupa Angka')
        else:
            print('No HandPhone Harus berjumlah 11 - 13 Karakter')

    while True:
        simpan_data = input("Apakah Anda Ingin Menyimpan Data (Y/N): ").upper()
        if simpan_data == "Y":
            personal_info["UserID"].append(user_id_input)
            personal_info["Password"].append(password_input)
            personal_info["Nama"].append(nama_input)
            personal_info["Gender"].append(gender_input)
            personal_info["Usia"].append(usia)
            personal_info["Pekerjaan"].append(pekerjaan_input)
            personal_info["Hobi"].append(kosong)
            personal_info["Alamat"]["RT"].append(RT_input)
            personal_info["Alamat"]["RW"].append(RW_input)
            personal_info["Alamat"]["Kota"].append(Kota_input)
            personal_info["Alamat"]["Zipcode"].append(int(Zipcode_input))
            personal_info["Alamat"]["Geo"]["Latitude"].append(Latitude_input)
            personal_info["Alamat"]["Geo"]["Longitude"].append(Longitude_input)
            personal_info["No HP"].append(No_HP_input)
            break
        elif simpan_data == "N":
            print("Data Tidak Tersimpan")
            print("")
            personal_info["Email"].remove(email)
            break
        else:
            print('Anda harus masukkan Y/N')
    intromenu()

    #################### FUNGSI MENU NO 2(LOGIN) ########################  
def menu_utama2():
    print("")
    print("=================Login=================")

    coba = 1
    password1 = False
    while coba <6 and password1 == False:
        input_userid = input("Masukkan UserID: ")
        password= input("Masukkan Password: ")
        if input_userid not in personal_info["UserID"]:
            print("Username Anda Tidak Terdaftar")
            print(f'Sisa Kesempatan Login Anda: {5 - coba}')
            coba = coba +1
            
        else:
            akses = personal_info["UserID"].index(input_userid)
            #if input_userid in personal_info["UserID"][akses]:
            if password != personal_info["Password"][akses]:
                print("Username Anda Benar, Tetapi Password Anda Salah")
                print(f'Sisa Kesempatan Login Anda: {5 - coba}')
                coba = coba + 1
                
            else:
                print("")
                print("Selamat Anda Berhasil Login!")
                print("Silahkan Pilih Aplikasi Yang Ingin Anda Gunakan")
                print("")
                password1 = True
                ################### MASUK MENU LOGIN ###################
                menu_login = printmenuandgetresponse()
                while menu_login != 13:

                ####### MENU 1 USER PROFILE
                    if menu_login == 1:
                        print("")
                        print("Terlampir Data personal Anda:")
                        print("")
                        print("Nama :", personal_info["Nama"][akses])
                        print("Email :", personal_info["Email"][akses])
                        print("Gender :", personal_info["Gender"][akses])
                        print("Usia :", personal_info["Usia"][akses])
                        print("Pekerjaan :", personal_info["Pekerjaan"][akses])
                        print("Hobi :", personal_info["Hobi"][akses])
                        print("Alamat, Nama Kota :", personal_info["Alamat"]["Kota"][akses])
                        print("Alamat, RT :", personal_info["Alamat"]["RT"][akses])
                        print("Alamat, RW :", personal_info["Alamat"]["RW"][akses])
                        print("Alamat, Zip Code :", personal_info["Alamat"]["Zipcode"][akses])
                        print("Alamat, Geo, Latitude :", personal_info["Alamat"]["Geo"]["Latitude"][akses])
                        print("Alamat, Geo, Longitude :", personal_info["Alamat"]["Geo"]["Longitude"][akses])
                        print("No HP :", personal_info["No HP"][akses])
                    
                    ####### MENU 2 KALKULATOR
                    elif menu_login == 2:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Kalkulator Mini Apps V 2.0")
                            fungsi_kalkulator()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 3 KONVERSI ROMAWI
                    elif menu_login == 3:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Konversi Romawi Mini Apps V 2.0")
                            fungsi_konversi_romawi()
                            print("")
                            sub_menu = sub_menu_loop()
                    
                    ####### MENU 4 KONVERSI KODE MORSE
                    elif menu_login == 4:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Konversi Kode Morse Mini Apps V 2.0")
                            fungsi_morse()
                            print("")
                            sub_menu = sub_menu_loop()
                    
                    ####### MENU 5 KALKULATOR HARI
                    elif menu_login == 5:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Kalkulator Hari Mini Apps V 2.0")
                            fungsi_kalkulator_hari()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 6 TRANSLATOR HARI
                    elif menu_login == 6:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Kamus Hari Mini Apps V 2.0")
                            fungsi_translator_hari()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 6 KONVERSI HARI
                    elif menu_login == 7:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Konversi Jumlah Hari ke Tahun, Bulan, Minggu, Hari Mini Apps V 2.0")
                            fungsi_konversi_hari()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 8 KALKULATOR FAKTORIAL
                    elif menu_login == 8:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Kalkulator Nilai Faktorial Mini Apps V 2.0")
                            fungsi_kalkulator_faktorial()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 9 JUMLAH DAN DERET FIBONACI
                    elif menu_login == 9:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Jumlah dan Deret Fibonnaci Mini Apps V 2.0")
                            fungsi_fibonnaci()
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 10 CAESAR CIPHER
                    elif menu_login == 10:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Caesar Cipher Mini Apps V 2.0")
                            fungsi_caesar_chiper()
                            print("")
                            sub_menu = sub_menu_loop()
                    
                    ####### MENU 11 SETTING USER
                    elif menu_login == 11:
                        sub_menu = 1
                        while sub_menu == 1:
                            print("")
                            print("Selamat Datang Di Setting User Mini Apps V 2.0")
                            print(f'User ID: {personal_info["UserID"][akses]}')
                            print(f'Password: {personal_info["Password"][akses]}')
                            print(f'Email: {personal_info["Email"][akses]}')
                            print("")
                            sub_menu = sub_menu_loop()

                    ####### MENU 12 CRUD TOKO BUAH V.2
                    elif menu_login == 12:
                        sub_menu = 1
                        while sub_menu == 1:
                            crud2()
                            sub_menu = sub_menu_loop()
                    
                    print("")
                    menu_login = printmenuandgetresponse()
                print("")
                print("Anda Berhasil Log Out")
    
    intromenu()

    #################### FUNGSI MENU NO 3(EXIT) ########################                  
def menu_utama3():
    print("Sampai Jumpa Lagi!")

##################################### BAGIAN PROGRAM SYSTEM #####################################
intromenu()
