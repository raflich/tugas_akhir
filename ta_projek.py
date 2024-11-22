import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
from PIL import Image, ImageTk, ImageSequence

#Modul 5 OOP(CLASS)
class Pokemon:

#Modul 4 Function Method
    def __init__(self, nama, hp, skill1, skill2):
        self.nama = nama
        self.hp = hp
        self.skill1 = skill1
        self.skill2 = skill2
        self.defending = False  #Modul 1 Boolean

#Modul 2 Pengondisian
    def lakukan_serangan(self, lawan, serangan):
        if serangan == "Bola Bayangan":
            damage = random.choice([10, 30])
        elif serangan == "Tumbukan":
            damage = random.choice([5, 15])
        elif serangan == "Ledakan":
            damage = random.choice([12, 25])
        elif serangan == "Api":
            damage = random.choice([10, 20])
        elif serangan == "Semburan Api":
            damage = random.choice([15, 35])
        else:
            damage = 0

        if lawan.defending:
            damage = damage // 2
            lawan.defending = False  #Modul 1 Boolean

        lawan.hp -= damage
        if lawan.hp < 0:
            lawan.hp = 0
        return damage

    def defend(self):
        self.defending = True

    def regenerate(self):
        regen_amount = random.randint(10, 20)
        self.hp += regen_amount
        if self.hp > 100:
            self.hp = 100
        return regen_amount

def display():
    label_pokemon1.config(text=f"{pokemon1.nama} - HP: {pokemon1.hp}")
    label_pokemon2.config(text=f"{pokemon2.nama} - HP: {pokemon2.hp}")
    if pokemon1.hp <= 0 or pokemon2.hp <= 0:
        if pokemon1.hp <= 0:
            result_label.config(text=f"{pokemon2.nama} menang!")
            change_background("charmander_win.png") #Background Bot menang
        else:
            result_label.config(text=f"{pokemon1.nama} menang!")
            change_background("gengar_win.png") #Background User menang

        #Menghapus Button dan Text
        label_pokemon1.place_forget()
        label_pokemon2.place_forget()
        result_label.place_forget()
        serangan_label.place_forget()
        frame_tombol.place_forget()


def pilih_serangan(serangan):
    if pokemon1.hp > 0 and pokemon2.hp > 0:
        damage = pokemon1.lakukan_serangan(pokemon2, serangan)
        result_label.config(text=f"{pokemon1.nama} menggunakan serangan {serangan} dan menyebabkan {damage} damage!")
        display()
        if pokemon2.hp > 0: 
            serangan_bot()
            #root.after(1500, serangan_bot()) #Gagal Delay

def pilih_defense():
    pokemon1.defend()
    result_label.config(text=f"{pokemon1.nama} memilih untuk bertahan!")
    display()
    root.after(1500, serangan_bot)

def pilih_regeneration():
    regen_amount = pokemon1.regenerate()
    result_label.config(text=f"{pokemon1.nama} melakukan regenerasi dan mendapatkan {regen_amount} HP!")
    display()
    root.after(1500, serangan_bot)

def serangan_bot():
    if pokemon2.hp > 0:
        serangan_bot = random.choice([pokemon2.skill1, pokemon2.skill2])
        damage = pokemon2.lakukan_serangan(pokemon1, serangan_bot)
        result_label.config(text=f"{pokemon2.nama} menggunakan serangan {serangan_bot} dan menyebabkan {damage} damage!")
        display()

def mulai_permainan():
    start_frame.pack_forget()  #Sembunyikan display starter
    main_frame.pack(fill="both", expand=True)
    animate_background(canvas, bg_image_item, bg_gif_frames)  #Ganti BG pertarungan (GIF)

def show_coming_soon():
    messagebox.showinfo("Coming Soon", "Fitur VS 2 akan datang segera!")

#Fungsi GIF
def load_gif_frames(path):
    img = Image.open(path)
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(img)]
    return frames

#Fungsi BG Pertarungan (GIF)
def animate_background(canvas, item, frames, idx=0):
    frame = frames[idx]
    canvas.itemconfig(item, image=frame)
    root.after(100, animate_background, canvas, item, frames, (idx + 1) % len(frames)) #Modul 3 Perulangan

#Fungsi Mengganti Background
def change_background(image_path):
    new_bg_image = PhotoImage(file=image_path)
    canvas.create_image(0, 0, anchor=tk.NW, image=new_bg_image) #Untuk menampilkan background
    canvas.image = new_bg_image #Untuk menyimpan gambar

#Window
root = tk.Tk()
root.title("Pertarungan Pokémon")
root.geometry("1040x500")
root.resizable(False, False)

#Modul 8 GUI
#Opening Frame
start_frame = tk.Frame(root, width=1040, height=500)
start_frame.pack(fill="both", expand=True)

start_canvas = tk.Canvas(start_frame, width=1040, height=500)
start_canvas.pack(fill="both", expand=True)

start_bg_image = PhotoImage(file="starter.png")
start_canvas.create_image(0, 0, anchor=tk.NW, image=start_bg_image)

start_button = tk.Button(start_canvas, text="Mulai Permainan (BOT)", font=("Arial", 14), command=mulai_permainan, bg="steelblue", fg="white")
start_canvas.create_window(520, 250, window=start_button)

vs2_button = tk.Button(start_canvas, text="VS 2", font=("Arial", 14), command=show_coming_soon, bg="steelblue", fg="white")
start_canvas.create_window(520, 300, window=vs2_button)

#Frame utama
main_frame = tk.Frame(root, width=1040, height=500)
canvas = tk.Canvas(main_frame, width=1040, height=500)
canvas.pack()

#Menambahkan GIF latar belakang
bg_gif_frames = load_gif_frames("pertarungan.gif")
bg_image_item = canvas.create_image(0, 0, anchor=tk.NW, image=bg_gif_frames[0])

#Dict Pokemon
pokemon1 = Pokemon("Gengar", 100, "Bola Bayangan", "Ledakan")
pokemon2 = Pokemon("Charmander", 100, "Api", "Semburan Api")

label_pokemon1 = tk.Label(main_frame, text=f"{pokemon1.nama} - HP: {pokemon1.hp}", font=("Arial", 12), bg="steelblue")
label_pokemon1.place(x=210, y=100)

label_pokemon2 = tk.Label(main_frame, text=f"{pokemon2.nama} - HP: {pokemon2.hp}", font=("Arial", 12), bg="steelblue")
label_pokemon2.place(x=700, y=100)

result_label = tk.Label(main_frame, text="Pilih serangan!", font=("Arial", 12), bg="lightblue")
result_label.place(x=240, y=420)

#Tombol serangan (GUI)
frame_tombol = tk.Frame(main_frame, bg="lightgrey")
frame_tombol.place(x=240, y=450)

tombol_bola = tk.Button(frame_tombol, text="Serangan Bola Bayangan", font=("Arial", 10), command=lambda: pilih_serangan("Bola Bayangan"))
tombol_bola.grid(row=0, column=0, padx=5)

tombol_tumbukan = tk.Button(frame_tombol, text="Serangan Tumbukan", font=("Arial", 10), command=lambda: pilih_serangan("Tumbukan"))
tombol_tumbukan.grid(row=0, column=1, padx=5)

tombol_ledakan = tk.Button(frame_tombol, text="Serangan Ledakan", font=("Arial", 10), command=lambda: pilih_serangan("Ledakan"))
tombol_ledakan.grid(row=0, column=2, padx=5)

tombol_defense = tk.Button(frame_tombol, text="Bertahan", font=("Arial", 10), command=pilih_defense)
tombol_defense.grid(row=0, column=3, padx=5)

tombol_regeneration = tk.Button(frame_tombol, text="Regeneration", font=("Arial", 10), command=pilih_regeneration)
tombol_regeneration.grid(row=0, column=4, padx=5)


#List serangan user dan bot
serangan_label = tk.Label(main_frame, text="Daftar Serangan dan Damage:\n"
                                           "Bola Bayangan: 10 / 30 damage\n"
                                           "Tumbukan: 5 / 15 damage\n"
                                           "Ledakan: 12 / 25 damage\n"
                                           "Api: 10 / 25 damage\n"
                                           "Semburan Api: 15 / 35 damage\n"
                                           "Regeneration: 10 / 20 HP", font=("Arial", 9), bg="steelblue")
serangan_label.place(x=10, y=10)

root.mainloop()