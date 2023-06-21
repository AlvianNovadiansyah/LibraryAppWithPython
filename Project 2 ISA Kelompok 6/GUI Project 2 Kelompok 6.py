import tkinter as tk
from tkinter import messagebox
from datetime import date
from tkinter import *
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Book Lending App")
window.geometry("1080x720")
window.resizable(False, False)

book = []
member = []
peminjaman = []
pengembalian = []


file = open("Book list.txt", "r+")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

file = open("Member List.txt", "r+")
Member_count = 0
for line in file:
    if line != "\n":
        Member_count += 1
file.close()

file = open("Arsip Peminjaman.txt", "r+")
Peminjam_count = 0
for line in file:
    if line != "\n":
        Peminjam_count += 1
file.close()

file = open("Arsip Pengembalian.txt", "r+")
Pengembalian_count = 0
for line in file:
    if line != "\n":
        Pengembalian_count += 1
file.close()

today = date.today()
d1 = today.strftime("%d/%m/%Y")
d1_month = d1[3:5]
d1_year = d1[6:]
d1_day = d1[:2]

month = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


def joinmember():
    window1 = Toplevel(window)
    window1.title("Join New Member")
    window1.geometry("1080x720")
    window1.resizable(False, False)
    Tmember = {"Member_ID": "", "Nama": "", "Alamat": "", "NIM": "", "Umur": "", "Telp.": ""}

    def addmember():
        Tmember["Member_ID"] = "M" + str(d1_day) + str(d1_year) + str(month[int(d1_month) - 1]) + "000" + \
                               str(Member_count)
        Tmember["Nama"] = nama_entry.get()
        Tmember["Alamat"] = alamat_enrty.get()
        Tmember["NIM"] = nim_entry.get()
        Tmember["Umur"] = umur_entry.get()
        Tmember["Telp."] = telp_entry.get()
        member.append(Tmember)

        filemember = open("Member List.txt", "a+")
        a = filemember.write("\n")
        w = filemember.write(str(Tmember))
        filemember.close()

        messagebox.showinfo('Signup', "Sucessfully sign up")

    def keluar():
        window1.destroy()

    Label(window1, text="Join New Member Form", font="arial 25").pack(pady=50)
    Label(window1, text="Nama*", font=("Serif", 14)).place(x=100, y=150)
    Label(window1, text="NIM*", font=("Serif", 14)).place(x=100, y=200)
    Label(window1, text="Alamat*", font=("Serif", 14)).place(x=100, y=250)
    Label(window1, text="Umur*", font=("Serif", 14)).place(x=100, y=300)
    Label(window1, text="No. Telepon*", font=("Serif", 14)).place(x=100, y=350)

    def on_enter(e):
        nama_entry.delete(0, "end")

    def on_leave(e):
        if nama_entry.get() == "":
            nama_entry.insert(0, "Masukan Nama Anda")

    nama_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                        font=("Microsoft Yauheni UI Light", 11))
    nama_entry.place(x=300, y=150)
    nama_entry.insert(0, "Masukan Nama Anda")
    nama_entry.bind("<FocusIn>", on_enter)
    nama_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        nim_entry.delete(0, "end")

    def on_leave(e):
        if nim_entry.get() == "":
            nim_entry.insert(0, "Masukan Nim anda")

    nim_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                         font=("Microsoft Yauheni UI Light", 11))
    nim_entry.place(x=300, y=200)
    nim_entry.insert(0, "Masukan NIM anda")
    nim_entry.bind("<FocusIn>", on_enter)
    nim_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        alamat_enrty.delete(0, "end")

    def on_leave(e):
        if alamat_enrty.get() == "":
            alamat_enrty.insert(0, "Masukan Alamat Anda")

    alamat_enrty = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                            font=("Microsoft Yauheni UI Light", 11))
    alamat_enrty.place(x=300, y=250)
    alamat_enrty.insert(0, "Masukan Alamat anda")
    alamat_enrty.bind("<FocusIn>", on_enter)
    alamat_enrty.bind("<FocusOut>", on_leave)

    def on_enter(e):
        umur_entry.delete(0, "end")

    def on_leave(e):
        if umur_entry.get() == "":
            umur_entry.insert(0, "Masukan Umur Anda")

    umur_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    umur_entry.place(x=300, y=300)
    umur_entry.insert(0, "Masukan Umur Anda")
    umur_entry.bind("<FocusIn>", on_enter)
    umur_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        telp_entry .delete(0, "end")

    def on_leave(e):
        if telp_entry .get() == "":
            telp_entry .insert(0, "Masukan No. Telepon")

    telp_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                       font=("Microsoft Yauheni UI Light", 11))
    telp_entry.place(x=300, y=350)
    telp_entry.insert(0, "Masukan No. Telepon")
    telp_entry.bind("<FocusIn>", on_enter)
    telp_entry.bind("<FocusOut>", on_leave)

    Button(window1, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=addmember).place(x=350,
                                                                                                                y=430)
    Button(window1, width=39, pady=7, text="Back to Menu", border=0, command=keluar).place(x=350, y=480)


def tambahbuku():
    window1 = Toplevel(window)
    window1.title("Adding New Book")
    window1.geometry("1080x720")
    window1.resizable(False, False)
    Tbook = {"kode_buku": "", "judul_buku": "", "tahun_terbit": "", "pengarang": "", "penerbit": ""}

    def addbook():
        Tbook["kode_buku"] = "KB" + str(d1_year) + str(month[int(d1_month) - 1]) + "000" + str(line_count)
        Tbook["judul_buku"] = judul_entry.get()
        Tbook["tahun_terbit"] = Terbit_entry.get()
        Tbook["pengarang"] = pengarang_enrty.get()
        Tbook["penerbit"] = penerbit_entry.get()
        book.append(Tbook)

        filebook = open("Book list.txt", "a+")
        a = filebook.write("\n")
        w = filebook.write(str(Tbook))
        filebook.close()

        messagebox.showinfo('Signup', "Sucessfully sign up")

    def keluar():
        window1.destroy()

    Label(window1, text="ADDING Book List Form", font="arial 25").pack(pady=50)
    Label(window1, text="Judul Buku*", font=("Serif", 14)).place(x=100, y=150)
    Label(window1, text="Tahun Terbit Buku*", font=("Serif", 14)).place(x=100, y=200)
    Label(window1, text="Nama Pengarang*", font=("Serif", 14)).place(x=100, y=250)
    Label(window1, text="Nama Penerbit*", font=("Serif", 14)).place(x=100, y=300)

    def on_enter(e):
        judul_entry.delete(0, "end")

    def on_leave(e):
        if judul_entry.get() == "":
            judul_entry.insert(0, "Judul Buku")

    judul_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                        font=("Microsoft Yauheni UI Light", 11))
    judul_entry.place(x=300, y=150)
    judul_entry.insert(0, "Judul Buku")
    judul_entry.bind("<FocusIn>", on_enter)
    judul_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        Terbit_entry.delete(0, "end")

    def on_leave(e):
        if Terbit_entry.get() == "":
            Terbit_entry.insert(0, "Tahun Terbit Buku")

    Terbit_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                         font=("Microsoft Yauheni UI Light", 11))
    Terbit_entry.place(x=300, y=200)
    Terbit_entry.insert(0, "Tahun Terbit Buku")
    Terbit_entry.bind("<FocusIn>", on_enter)
    Terbit_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        pengarang_enrty.delete(0, "end")

    def on_leave(e):
        if pengarang_enrty.get() == "":
            pengarang_enrty.insert(0, "Nama Pengarang Buku")

    pengarang_enrty = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                            font=("Microsoft Yauheni UI Light", 11))
    pengarang_enrty.place(x=300, y=250)
    pengarang_enrty.insert(0, "Nama Pengarang Buku")
    pengarang_enrty.bind("<FocusIn>", on_enter)
    pengarang_enrty.bind("<FocusOut>", on_leave)

    def on_enter(e):
        penerbit_entry.delete(0, "end")

    def on_leave(e):
        if penerbit_entry.get() == "":
            penerbit_entry.insert(0, "Nama Penerbit Buku")

    penerbit_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    penerbit_entry.place(x=300, y=300)
    penerbit_entry.insert(0, "Nama Penerbit Buku")
    penerbit_entry.bind("<FocusIn>", on_enter)
    penerbit_entry.bind("<FocusOut>", on_leave)

    Button(window1, width=39, pady=7, text="ADD Book", bg="#57a1f8", fg="white", border=0, command=addbook).place(x=350,
                                                                                                                  y=380)
    Button(window1, width=39, pady=7, text="Back to Menu", border=0, command=keluar).place(x=350, y=430)


def deletebuku():
    window1 = Toplevel(window)
    window1.title("Adding New Book")
    window1.geometry("1080x720")
    window1.resizable(False, False)

    a_file = open("Book list.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    Label(window1, text="Deleted Book from Book List", font="arial 25").pack(pady=50)
    Label(window1, text="Judul Buku atau Kode Buku*", font=("Serif", 16)).place(x=400, y=200)

    def on_enter(e):
        hapus_enrty.delete(0, "end")

    def on_leave(e):
        if hapus_enrty.get() == "":
            hapus_enrty.insert(0, "Buku yang ingin dihapus")

    hapus_enrty = Entry(window1, width=50, fg="black", border=0, bd=2, bg="white",
                        font=("Microsoft Yauheni UI Light", 11))
    hapus_enrty.place(x=300, y=250)
    hapus_enrty.insert(0, "Buku yang ingin dihapus")
    hapus_enrty.bind("<FocusIn>", on_enter)
    hapus_enrty.bind("<FocusOut>", on_leave)

    def hapus():
        new_file = open("Book list.txt", "w+")
        kunci = hapus_enrty.get()
        for line in lines:
            if line.find(kunci) == -1:
                new_file.write(line)
        new_file.close()

    def keluar():
        window1.destroy()

    Button(window1, width=39, pady=7, text="Delete Book", bg="#57a1f8", fg="white", border=0, command=hapus).place(
        x=350, y=380)
    Button(window1, width=39, pady=7, text="Back to Menu", border=0, command=keluar).place(x=350, y=430)


def password():
    pass


def listbuku():
    window1 = Toplevel(window)
    window1.title("Adding New Book")
    window1.geometry("1080x720")
    window1.resizable(False, False)

    fframe = Frame(window1)
    fframe.pack(pady=10)
    my_frame = Frame(window1)
    my_frame.pack(pady=10)

    scroll_v = Scrollbar(my_frame)
    scroll_v.pack(side=RIGHT, fill=BOTH)

    scroll_h = Scrollbar(my_frame, orient=HORIZONTAL)
    scroll_h.pack(side=BOTTOM, fill="x")

    def keluar():
        window1.destroy()

    Label(fframe, text="Book List", font="arial 25").pack(pady=5)
    my_text = Listbox(my_frame, width=80, height=15, font=("Brunch Script MT", 15), bg="SystemButtonFace", bd=0,
                      fg="#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
    my_text.pack(pady=10)

    my_text.config(yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set)
    scroll_h.config(command=my_text.yview)
    scroll_v.config(command=my_text.xview)

    list_file = open("Book list.txt", "r+")
    stuff = list_file.readlines()
    for line in stuff:
        my_text.insert(END, line)
    list_file.close()

    Button(window1, width=39, pady=7, text="Back to Menu", border=0, bd=0, fg="#464646", highlightthickness=0,
           command=keluar).place(x=400, y=600)


def peminjamanbuku():
    window1 = Toplevel(window)
    window1.title("Peminjaman Buku")
    window1.geometry("1080x720")
    window1.resizable(False, False)
    Tpeminjaman = {"Kode_Peminjam": "", "Nama": "", "Alamat": "", "Tanggal": "", "Buku yang Dipinjam": "", "Telp.": ""}

    def addpeminjam():
        Tpeminjaman["Kode_Peminjam"] = "PB" + str(d1_day) + str(d1_year) + str(month[int(d1_month) - 1]) + "000" + \
                               str(Peminjam_count)
        Tpeminjaman["Nama"] = nama_entry.get()
        Tpeminjaman["Alamat"] = alamat_enrty.get()
        Tpeminjaman["Tanggal"] = d1
        Tpeminjaman["Buku yang Dipinjam"] = bukuP_entry.get()
        Tpeminjaman["Telp."] = telp_entry.get()
        peminjaman.append(Tpeminjaman)

        filepeminjam = open("Arsip Peminjaman.txt", "a+")
        a = filepeminjam.write("\n")
        w = filepeminjam.write(str(Tpeminjaman))
        filepeminjam.close()

        messagebox.showinfo('Peminjaman', "Sucessfully Melakukan Peminjaman")

        def tampilan():
            thank = Toplevel(window1)
            thank.geometry("720x640")
            label1 = Label(thank, text="Terima Kasih, berikut kode peminjaman anda", font="arial 16", bg="white",
                           border=0)
            label1.pack(pady=20)
            label2 = Label(thank, text=Tpeminjaman["Kode_Peminjam"], font="arial 25", border=0, bg="white")
            label2.pack(pady=20)
        tampilan()

    def keluar():
        window1.destroy()

    Label(window1, text="Form Peminjaman Buku", font="arial 25").pack(pady=50)
    Label(window1, text="Nama*", font=("Serif", 14)).place(x=100, y=150)
    Label(window1, text="Alamat*", font=("Serif", 14)).place(x=100, y=200)
    Label(window1, text="Buku yang Dipinjam*", font=("Serif", 14)).place(x=100, y=250)
    Label(window1, text="No. Telepon*", font=("Serif", 14)).place(x=100, y=300)

    def on_enter(e):
        nama_entry.delete(0, "end")

    def on_leave(e):
        if nama_entry.get() == "":
            nama_entry.insert(0, "Masukan Nama Anda")

    nama_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                        font=("Microsoft Yauheni UI Light", 11))
    nama_entry.place(x=300, y=150)
    nama_entry.insert(0, "Masukan Nama Anda")
    nama_entry.bind("<FocusIn>", on_enter)
    nama_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        alamat_enrty.delete(0, "end")

    def on_leave(e):
        if alamat_enrty.get() == "":
            alamat_enrty.insert(0, "Masukan Alamat Anda")

    alamat_enrty = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                            font=("Microsoft Yauheni UI Light", 11))
    alamat_enrty.place(x=300, y=200)
    alamat_enrty.insert(0, "Masukan Alamat anda")
    alamat_enrty.bind("<FocusIn>", on_enter)
    alamat_enrty.bind("<FocusOut>", on_leave)

    def on_enter(e):
        bukuP_entry.delete(0, "end")

    def on_leave(e):
        if bukuP_entry.get() == "":
            bukuP_entry.insert(0, "Masukan Buku yang ingin Dipinjam")

    bukuP_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    bukuP_entry.place(x=300, y=250)
    bukuP_entry.insert(0, "Masukan Buku yang ingin Dipinjam")
    bukuP_entry.bind("<FocusIn>", on_enter)
    bukuP_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        telp_entry .delete(0, "end")

    def on_leave(e):
        if telp_entry .get() == "":
            telp_entry .insert(0, "Masukan No. Telepon")

    telp_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                       font=("Microsoft Yauheni UI Light", 11))
    telp_entry.place(x=300, y=300)
    telp_entry.insert(0, "Masukan No. Telepon")
    telp_entry.bind("<FocusIn>", on_enter)
    telp_entry.bind("<FocusOut>", on_leave)

    Button(window1, width=39, pady=7, text="Lakukan Peminjaman", bg="#57a1f8", fg="white", border=0,
           command=addpeminjam).place(x=350, y=430)
    Button(window1, width=39, pady=7, text="Back to Menu", border=0, command=keluar).place(x=350, y=480)


def pengembalianbuku():
    window1 = Toplevel(window)
    window1.title("Pengembalian Buku")
    window1.geometry("1080x720")
    window1.resizable(False, False)
    Tpengembalian = {"Kode_Pengembalian": "", "Kode_peminjam": "", "Nama": "", "Tanggal": "", "Buku yang Dikembalikan":
        "", "Telp.": "", "Keterangan": ""}

    def addpengembalian():
        Tpengembalian["Kode_Pengembalian"] = "SB" + str(d1_day) + str(d1_year) + str(month[int(d1_month) - 1]) + "000" \
                                             + str(Pengembalian_count)
        Tpengembalian["Nama"] = nama_entry.get()
        Tpengembalian["Kode_peminjam"] = kode_enrty.get()
        Tpengembalian["Tanggal"] = d1
        Tpengembalian["Buku yang Dikembalikan"] = bukuP_entry.get()
        Tpengembalian["Telp."] = telp_entry.get()
        Tpengembalian["Keterangan"] = ket_entry.get()
        pengembalian.append(Tpengembalian)

        filepeminjam = open("Arsip Pengembalian.txt", "a+")
        a = filepeminjam.write("\n")
        w = filepeminjam.write(str(Tpengembalian))
        filepeminjam.close()

        messagebox.showinfo('Pengembalian', "Sucessfully Melakukan Pengembalian")

    def keluar():
        window1.destroy()

    Label(window1, text="Form Pengembalian Buku", font="arial 25").pack(pady=50)
    Label(window1, text="Nama*", font=("Serif", 14)).place(x=100, y=150)
    Label(window1, text="Kode Peminjam*", font=("Serif", 14)).place(x=100, y=200)
    Label(window1, text="Buku yang Dipinjam*", font=("Serif", 14)).place(x=100, y=250)
    Label(window1, text="No. Telepon*", font=("Serif", 14)).place(x=100, y=300)
    Label(window1, text="Keterangan", font=("Serif", 14)).place(x=100, y=350)

    def on_enter(e):
            nama_entry.delete(0, "end")

    def on_leave(e):
        if nama_entry.get() == "":
            nama_entry.insert(0, "Masukan Nama Anda")

    nama_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    nama_entry.place(x=300, y=150)
    nama_entry.insert(0, "Masukan Nama Anda")
    nama_entry.bind("<FocusIn>", on_enter)
    nama_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        kode_enrty.delete(0, "end")

    def on_leave(e):
        if kode_enrty.get() == "":
            kode_enrty.insert(0, "Masukan Kode Peminjaman Anda")

    kode_enrty = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                             font=("Microsoft Yauheni UI Light", 11))
    kode_enrty.place(x=300, y=200)
    kode_enrty.insert(0, "Masukan Kode Peminjaman anda")
    kode_enrty.bind("<FocusIn>", on_enter)
    kode_enrty.bind("<FocusOut>", on_leave)

    def on_enter(e):
        bukuP_entry.delete(0, "end")

    def on_leave(e):
        if bukuP_entry.get() == "":
            bukuP_entry.insert(0, "Masukan Buku yang ingin Dikembalikan")

    bukuP_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                            font=("Microsoft Yauheni UI Light", 11))
    bukuP_entry.place(x=300, y=250)
    bukuP_entry.insert(0, "Masukan Buku yang ingin Dikembalikan")
    bukuP_entry.bind("<FocusIn>", on_enter)
    bukuP_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        telp_entry.delete(0, "end")

    def on_leave(e):
        if telp_entry.get() == "":
            telp_entry.insert(0, "Masukan No. Telepon")

    telp_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    telp_entry.place(x=300, y=300)
    telp_entry.insert(0, "Masukan No. Telepon")
    telp_entry.bind("<FocusIn>", on_enter)
    telp_entry.bind("<FocusOut>", on_leave)

    def on_enter(e):
        ket_entry.delete(0, "end")

    def on_leave(e):
        if ket_entry.get() == "":
            ket_entry.insert(0, "Masukan Keterangan")

    ket_entry = Entry(window1, width=35, fg="black", border=0, bd=2, bg="white",
                           font=("Microsoft Yauheni UI Light", 11))
    ket_entry.place(x=300, y=350)
    ket_entry.insert(0, "Masukan Keterangan")
    ket_entry.bind("<FocusIn>", on_enter)
    ket_entry.bind("<FocusOut>", on_leave)

    Button(window1, width=39, pady=7, text="Lakukan Pengembalian", bg="#57a1f8", fg="white", border=0,
               command=addpengembalian).place(x=350, y=430)
    Button(window1, width=39, pady=7, text="Back to Menu", border=0, command=keluar).place(x=350, y=480)


def mainmenu():
    def menumember():
        OpButton.destroy()
        MemButton.destroy()
        EButton.destroy()
        labe1.destroy()
        labe2.destroy()

        def joinm():
            joinmember()

        def listbook():
            listbuku()

        def peminjaman():
            peminjamanbuku()

        def pengembalian():
            pengembalianbuku()

        def back():
            buttonm1.destroy()
            buttonm2.destroy()
            buttonm3.destroy()
            buttonm4.destroy()
            buttonm5.destroy()
            labe3.destroy()
            mainmenu()

        labe3 = Label(window, text="Member Menu", font="arial 25")
        labe3.pack(pady=30)
        buttonm1 = Button(window, text="Join Member", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=joinm)
        buttonm2 = Button(window, text="List a Book", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=listbook)
        buttonm3 = Button(window, text="Peminjaman Buku", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=peminjaman)
        buttonm4 = Button(window, text="Pengembalian Buku", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=pengembalian)
        buttonm5 = Button(window, text="MAIN MENU", font=("Times New Roman", 15), width=40, command=back)

        buttonm1.pack(pady=10)
        buttonm2.pack(pady=10)
        buttonm3.pack(pady=10)
        buttonm4.pack(pady=10)
        buttonm5.pack(pady=10)

    def menuop():
        OpButton.destroy()
        MemButton.destroy()
        EButton.destroy()
        labe1.destroy()
        labe2.destroy()

        def back():
            buttonm1.destroy()
            buttonm2.destroy()
            buttonm3.destroy()
            buttonm4.destroy()
            labe3.destroy()
            mainmenu()

        def addbook():
            tambahbuku()

        def deletebook():
            deletebuku()

        def listbook():
            listbuku()

        labe3 = Label(window, text="Operator Menu", font="arial 25")
        labe3.pack(pady=30)
        buttonm1 = Button(window, text="ADD a Book", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                          width=40, command=addbook)
        buttonm2 = Button(window, text="Delete a Book", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=deletebook)
        buttonm3 = Button(window, text="List of Book", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=listbook)
        buttonm4 = Button(window, text="MAIN MENU", font=("Times New Roman", 15), width=40, command=back)

        buttonm1.pack(pady=10)
        buttonm2.pack(pady=10)
        buttonm3.pack(pady=10)
        buttonm4.pack(pady=10)

    photo = ImageTk.PhotoImage(Image.open("Logo Library.png"))
    labe1 = Label(window, image=photo, bg="white", border=0)
    labe1.image = photo
    labe1.pack(pady=10)
    labe2 = Label(window, text="Lending Book APP", font="arial 25")
    labe2.pack(pady=30)
    OpButton = Button(window, text="1. Operator", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                      width=40, command=menuop)
    OpButton.pack(pady=10)
    MemButton = Button(window, text="2. Member", font=("Times New Roman", 15), bg="#57a1f8", fg="white", border=0,
                       width=40, command=menumember)
    MemButton.pack(pady=10)
    EButton = Button(window, text="3. Exit", font=("Times New Roman", 15), width=40, command=window.quit)
    EButton.pack(pady=10)


mainmenu()
window.mainloop()
