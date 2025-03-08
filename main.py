import tkinter as tk
from tkinter import messagebox

def login () :
    username =  username_entry.get ()
    password = pasword_entry.get ()

    if username == "Azril" :
     if password == "170708" :
        messagebox.showinfo ("Login berhasil", "Selamat datang")
        frame_login.destroy ()
        frame_kasir.pack (padx=20,pady=20)
     
     else : 
        messagebox.showerror ("Login Gagal", "Password salah")
    else :
       messagebox.showerror ("Login gagal", "Username salah")

def Buka_kasir () :
   nama_pembeli = str (nama_entry.get())
   nama_barang  = str (namabrg_entry.get())
   jumlah_produk = int (jumlah_entry.get())
   harga_produk = int (harga_entry.get())
   uang_pemveli = int (uang_entry.get())

   total = harga_produk * jumlah_produk
   kembali = uang_pemveli - total

   pesan_invoice = f"""
    Nama Pembeli = {nama_pembeli}
    =======================================
    Nama Barang = {nama_barang}
    jumlah Barang = {jumlah_produk}
    harga Rp. {harga_produk}
    =======================================
    Total = Rp. {total}
    Tunai = Rp. {uang_pemveli}
    ----------------------------
    Kembali = Rp. {kembali}

    Terimakasih Telah Berbalnja!!
    """
   
   messagebox.showinfo ("invoice",message=pesan_invoice)

mulai = tk.Tk ()

frame_login = tk.Frame (mulai)
frame_login.pack (padx=20,pady=20)

input_username = tk.Label (frame_login, text= "Username :")
input_username.grid (padx=5,pady=5)
username_entry = tk.Entry (frame_login)
username_entry.grid (row=0,column=1,padx=5,pady=5)

input_password = tk.Label (frame_login,text= "Password : ")
input_password.grid (row=1,padx=5,pady=5)
pasword_entry = tk.Entry (frame_login, show="*")
pasword_entry.grid (row=1,column=1,padx=5,pady=5)

tombol_login = tk.Button (frame_login,text="Login",command= login)
tombol_login.grid (columnspan=2, padx= 5, pady=5, sticky= "we")

frame_kasir = tk.Frame (mulai)

input_nama = tk.Label (frame_kasir,text= "Nama Pembeli : ")
input_nama.pack (padx=5,pady=5)
nama_entry = tk.Entry (frame_kasir)
nama_entry.pack (padx=5,pady=5)

input_namabrg = tk.Label (frame_kasir,text= "Nama Barang : ")
input_namabrg.pack (padx=5,pady=5)
namabrg_entry = tk.Entry (frame_kasir)
namabrg_entry.pack (padx=5,pady=5)

input_jumlahbrg = tk.Label (frame_kasir,text= "Jumlah Produk : (Angka) ")
input_jumlahbrg.pack (padx=5,pady=5)
jumlah_entry = tk.Entry (frame_kasir)
jumlah_entry.pack (padx=5,pady=5)

input_harga = tk.Label (frame_kasir,text= "Harga Produk : (Angka) ")
input_harga.pack (padx=5,pady=5)
harga_entry = tk.Entry (frame_kasir)
harga_entry.pack (padx=5,pady=5)

input_uang = tk.Label (frame_kasir,text= "Uang Pembeli : (Angka) ")
input_uang.pack (padx=5,pady=5)
uang_entry = tk.Entry (frame_kasir)
uang_entry.pack (padx=5,pady=5)

Tombol_total = tk.Button (frame_kasir,text="Total",command=Buka_kasir)
Tombol_total.pack(padx=5,pady=5)

mulai.mainloop()