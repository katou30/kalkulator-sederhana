from tkinter import *

main = Tk() # Tampilan utama
main.geometry("312x324")  # Ukuran utama
main.resizable(0, 0)  # Mencegah tampilan utama dapat di resizable(fullscreen)
main.title("Kalkulator") # Judul

# Fungsi
# btn_click -> Fungsi ini berguna untuk selalu menambah 
#              angka ke tampilan setiap kita klik angka

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# bt_clear -> Fungsi yang berguna untuk membersihkan tampilan 

def btn_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
    
def btn_del():
    '''
    global input_text
    input_text = input_field.delete(0, 'end')
    return
    '''
    global expression 
    expression = input_text.set(input_field.get()[0:-1])
    expression = str(expression)
    return
    
        
#def backspace_b():
    #global expression
    #input_text.pop()
    #input_text = input_text[:-1]
    
# bt_equal -> Fungsi untuk menjumlahkan angka yang di inputkan
 
def btn_equal():
    global expression
    result = str(eval(expression)) # eval -> digunakan untuk mengevaluasi ekspresi(trigger) string secara langsung
    input_text.set(result)
    expression = ""
 
expression = ""
 
# StringVar() -> berfungsi untuk mendapat contoh tampilan input(angka yang di input)
input_text = StringVar()
 
# frame untuk tampilan angka yang dimasukan
input_frame = Frame(main, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
 
# berfungsi untuk isi dari frame yang menampilkan angka yang dimasukan
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # ipady -> berfungsi untuk menambah tinggi frame penginputan
 
# frame untuk dibawah frame penginputan, atau frame yang digunakan untuk kumpulan tombol
btns_frame = Frame(main, width=312, height=272.5, bg="grey")
btns_frame.pack()
 
# Baris pertama                                                                  
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
backspase = Button(btns_frame, text = "<-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_del()).grid(row = 0, column = 0, padx = 1, pady = 1)
pembagian = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# Baris ke dua 
tujuh = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
delapan = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
sembilan = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
pengkalian = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# Baris ke tiga
empat = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
lima = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
enam = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
pengurangan = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# Baris ke empat 
satu = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
dua = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
tiga = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
penambahan = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# Baris ke empat
nol = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
titik = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
sama_dengan = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

main.mainloop()