import os
import random
import string
from tabulate import tabulate

def random_string(panjang:int)->str:
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string

class Kontak:
    def __init__(self, pk, nama, nomor, email):
        self.pk = pk
        self.nama = nama
        self.nomor = nomor
        self.email = email
        return f'{self.pk},{self.nama},{self.nomor},{self.email}\n'

class Dbase(Kontak):
    DATABASE = "data.txt"
    TEMP = "temp.txt"
    
    def __init__(self):
        try:
            with open(self.DATABASE, 'r') as file:
                print("Database tersedia !")
        except:
            print("Database tidak ditemukan, silahkan membuat database baru")
            self.add()
            
    def add(self):
        pk = random_string(6)
        nama = input("Nama\t: ")
        nomor = input("No HP\t: ")
        email = input("e-mail\t: ")
        try:
            with open(self.DATABASE, 'a', encoding="utf-8") as file:
                file.write(super().__init__(pk,nama,nomor,email))
        except:
            print("Error....")
    
    def read(self,**kwargs):
        try:
            with open(self.DATABASE, 'r') as file :
                contact = file.readlines()
                jumlah_kontak = len(contact)
                if "index" in kwargs :
                    index_kontak = kwargs["index"]-1
                    if index_kontak < 0 or index_kontak > jumlah_kontak:
                        return False
                    else:
                        return contact[index_kontak]
                else:
                    return contact
        except:
            print("error")
    
    def display(self):
        data_kontak = self.read()
        contacts = {
            'No' : [],
            'Nama' : [],
            'Nomor' : [],
            'e-mail' : []
        }
        i = 0
        for i, data in enumerate(data_kontak):
            data_break = data.split(",")
            i+=1
            contacts["No"].append(i)
            nama = data_break[1]
            contacts["Nama"].append(nama)
            nomor = data_break[2]
            contacts["Nomor"].append(nomor)
            email = data_break[3]
            contacts["e-mail"].append(email)
                    
        print(tabulate(contacts, headers="keys", tablefmt="fancy_grid"))
            
    def update(self):
        self.display()
        while(True):
            print("Silahkan pilih nomor kontak yang akan di update")
            no_kontak = int(input("Nomor Kontak : "))
            data_kontak = self.read(index=no_kontak)
            if data_kontak:
                break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        
        data_break = data_kontak.split(',')
        pk = data_break[0]
        nama = data_break[1]
        nomor = data_break[2]
        email = data_break[3][:-1]
        
        while(True):
            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Silahkan pilih data apa yang ingin anda ubah")
            print(f"1. Nama\t\t: {nama}")
            print(f"2. Nomor\t: {nomor}")
            print(f"3. e-mail\t: {email}")

            # memilih mode untuk update
            user_option = input("Pilih data [1,2,3]: ")
            print("\n"+"="*100)
            match user_option:
                case "1": nama = input("Nama\t\t: ")
                case "2": nomor = input("Nomor\t: ")
                case "3": email = input("e-mail\t: ")
                case _: print("index tidak cocok")

            print("Data baru anda")
            print(f"1. Nama\t\t: {nama}")
            print(f"2. Nomor\t: {nomor}")
            print(f"3. e-mail\t: {email}")
            is_done = input("Apakah data sudah sesuai(y/n)? ")
            if is_done == "y" or is_done == "Y":
                break
    
        try:
            with open(self.DATABASE,'r') as file, open(self.TEMP,'w',encoding="utf-8") as temp:
                for line in file:
                    contact = line.strip().split(',')
                    if contact[0] == pk:
                        temp.write(super().__init__(pk,nama,nomor,email))
                    else:
                        temp.write(line)
            
            os.remove(self.DATABASE)
            os.rename(self.TEMP,self.DATABASE)
            print("Data berhasil diupdate, berikut adalah data baru anda")
            self.display()
        except:
            print("error dalam update data")
            
    def delete(self):
        self.display()
        while(True):
            print("Silahkan pilih nomor kontak yang akan di hapus")
            no_kontak = int(input("Nomor Kontak : "))
            data_kontak = self.read(index=no_kontak)
            if data_kontak:
                break
            else:
                print("nomor tidak valid, silahkan masukan lagi")
        
        data_break = data_kontak.split(',')
        pk = data_break[0]
        nama = data_break[1]
        nomor = data_break[2]
        email = data_break[3][:-1]
        
        try:
            with open(self.DATABASE,'r') as file, open(self.TEMP,'w',encoding="utf-8") as temp:
                for line in file:
                    contact = line.strip().split(',')
                    if contact[0] == pk:
                        continue
                    
                    temp.write(line)
            
            os.remove(self.DATABASE)
            os.rename(self.TEMP,self.DATABASE)
            print("Data berhasil dihapus, berikut adalah data baru anda")
            self.display()
        except:
            print("error dalam update data")