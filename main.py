import os
from Class import Dbase

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
            
    print("SELAMAT DATANG DI PROGRAM")
    print("MANAJEMEN KONTAK")
    print("=========================")
    
    database = Dbase()
        
    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("MANAJEMEN KONTAK")
        print("=========================")
        
        print(f"1. Tampilkan Kontak")
        print(f"2. Tambah Kontak")
        print(f"3. Edit Kontak")
        print(f"4. Hapus Kontak")
        print(f"5. Keluar\n")
        
        user_option = input("Masukkan opsi: ")
        
        match user_option:
            case "1": database.display()
            case "2": 
                database.add()
                print("\n berikut adalah data baru anda : ")
                database.display()
            case "3": database.update()
            case "4": database.delete()
            case "5": break
            case _: print("Opsi tidak valid, silahkan pilih opsi [1-5]")
        
        is_done = input("Apakah selesai (y/n) ? ")
        if is_done.lower() == "y":
            break
        
    print("Program Berakhir")
