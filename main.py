from resources import *
import tkinter as tk
import tkinter.ttk as ttk

class Slistbox(tk.Listbox):
    def __init__(self, *args, **kwargs):
        super().__init__(height = 2, width = 27)
        self.insert(1, "")
        self.insert(2, "")

        
class Kaos(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("JUJUTSU KAISEN KAOS")
        self.geometry("890x400")

#################### FONCTIONS ####################            
        def reset():
            global sdf
            global persos
            sdf.clear()
            for char in persos:
                sdf.append(char)
            for room in rooms:
                room.contenance.clear()
            for liste in listeslieu:
                liste.delete(0, tk.END)
                liste.insert(0, "")
                liste.insert(1, "")
                
        def actualisermove(Listbox, Room):
            if len(Room.contenance) == 0:
                Listbox.delete(0, tk.END)
                Listbox.insert(0, "")
                Listbox.insert(1, "")
            elif len(Room.contenance) == 1:
                Listbox.delete(0, tk.END)
                Listbox.insert(0, f"{Room.contenance[0].name}")
                Listbox.insert(1, "")
            elif len(Room.contenance) == 2:
                Listbox.delete(0, tk.END)
                Listbox.insert(0, f"{Room.contenance[0].name}")
                Listbox.insert(1, f"{Room.contenance[1].name}")

        def actualiser_sdf():
            global sdf
            sdftemp = sorted(sdf, key=lambda Character: Character.name)
            sdf = sdftemp

        def randomize():
            global sdf
            while len(sdf) > 0:
                for room in rooms:
                    if len(room.contenance) == 0:
                        rando = random.choice(sdf)
                        room.movein(rando)
                        sdf.remove(rando)
                    if len(room.contenance) == 1:
                        rando2 = random.choice(sdf)
                        room.movein(rando2)
                        sdf.remove(rando2)
            else:
                hindex = 0
                for liste in listeslieu:
                    listeslieu[hindex].delete(0, tk.END)
                    listeslieu[hindex].insert(0, f"{rooms[hindex].contenance[0].name}")
                    listeslieu[hindex].insert(1, f"{rooms[hindex].contenance[1].name}")
                    hindex = hindex +1

### SCREENS
        def about():
            about_screen = tk.Toplevel(self)
            about_screen.title = "Information screen"
            instructions = tk.LabelFrame(about_screen, text = "How to")
            instructions.grid(row = 0)
            about_it = tk.LabelFrame(about_screen, text = "ABOUT")
            about_it.grid(row = 1)
            instructions = tk.Text(instructions, wrap = "word", height = 5, width = 30, pady = 10, padx = 10)
            instructions.insert("insert", "Pick pairs of characters or let Randomize complete your imagination, then click on Results and bask in the glory of RNG!")
            instructions.grid(row = 1)
            about_that = tk.Text(about_it, wrap = "word", height = 5, width = 30, pady = 10, padx = 10)
            about_that.insert("insert", "Version: 1.0\nAuthor: Senzen Travers\nInsult me: @SenzenT on Twitter\nRead me: Senzen_Travers on AO3")
            about_that.grid()
            
        def results():
            result_screen = tk.Toplevel(self)
            result_screen.title("REJOICE, PLEB, FOR FATE AND/OR RNG HATH SPOKENTH")
            titre = tk.Frame(result_screen)
            titre.grid(columnspan = 6, pady = 3)
            left = tk.Frame(result_screen)
            left.grid(column = 0, rowspan = 6, pady = 8)
            right = tk.Frame(result_screen)
            right.grid(column = 6, rowspan = 6, pady = 8)
            leftpretty = tk.Label(result_screen, text = "  ")
            leftpretty.grid(row = 2)
            rightpretty = tk.Label(result_screen, text = "  ")
            rightpretty.grid(row = 2, column = 7)

            ylieu = 1
            zlieu = 1
            ultlieu = 1
            for room in rooms:
                nomlieu = tk.Label(result_screen, text = f"{room.name}", pady = 5)
                resultlieu = tk.Text(result_screen, wrap = "word", height = 11, width = 28)
                resultlieu.insert("insert", f"{room.interact()}")
                if ylieu < 6:
                    nomlieu.grid(row = 1, column = ylieu)
                    resultlieu.grid(row = 2, column = ylieu, pady = 2, padx = 3)
                    ylieu = ylieu + 1
                elif zlieu < 6:
                    nomlieu.grid(row = 3, column = zlieu)
                    resultlieu.grid(row = 4, column = zlieu, pady = 2, padx = 3)
                    zlieu = zlieu + 1
                elif ultlieu < 6:
                    nomlieu.grid(row = 5, column = ultlieu)
                    resultlieu.grid(row = 6, column = ultlieu, pady = 2, padx = 3)
                    ultlieu = ultlieu + 1




########## CHAR SCREEN

        def gestion_char(self, Listbox, Room):
            selection = Listbox.curselection()
            if selection:
                if len(Listbox.get(selection[0])) == 0:
                    print(f"selected item: {Listbox.get(selection[0])}")
                else:
                    sdf.append(Room.contenance[selection[0]])
                    Room.moveout(Room.contenance[selection[0]])
                    actualisermove(Listbox, Room)
                    actualiser_sdf()
                char_screen = tk.Toplevel(self)
                charlist = tk.Listbox(char_screen, height = 30)
                x = 0
                for char in sdf:
                    charlist.insert(x, char.name)
                    x = x+1                    
                def whozzat(event):
                    selchar = charlist.curselection()
                    if selchar and len(Room.contenance) == 0:
                        Room.movein(sdf[selchar[0]])
                        Listbox.delete(0, tk.END)
                        Listbox.insert(0, f"{Room.contenance[0].name}")
                        Listbox.insert(1, "")
                        sdf.remove(sdf[selchar[0]])
                    elif selchar and len(Room.contenance) == 1:
                        Room.movein(sdf[selchar[0]])
                        Listbox.delete(0, tk.END)
                        Listbox.insert(0, f"{Room.contenance[0].name}")
                        Listbox.insert(1, f"{Room.contenance[1].name}")
                        sdf.remove(sdf[selchar[0]])
                    char_screen.destroy()
                charlist.bind("<Double-1>", whozzat)
                charlist.grid()
        def print_selection(self, listbox):
            selection = listbox.curselection()
            if selection:
                listbox.delete(selection)
                print(f"{sdf[index].name}")
            else:
                print("nothing is selected")


####################### FRAMES ####################
        titreacc = tk.Frame(self)
        titreacc.grid(row = 0, columnspan = 7, pady = 10)
        gaucheacc = ttk.Frame(self, width = 5)
        gaucheacc.grid(row = 1, column = 0, rowspan = 7)
        ihateall = tk.Frame(self)
        ihateall.grid(row = 12, column = 1, columnspan = 6)
        staghfoullah = tk.Frame(self)
        staghfoullah.grid(row = 13, column = 1, columnspan = 6)
## boutons
        randotitle = ["Every year, there are 10k curse victims in Japan and I ship the rest.", "I bled for this foolishness", "Jujutsu Kaisen Kaos", "Jujutsu Kaisen Kaos", "Jujutsu Kaisen Kaos", "Jujutsu Kaisen No Kaos Only Proper Order"]
        mytitle = tk.Label(titreacc, text = f"{random.choice(randotitle)}", font = 30)
        mytitle.grid(columnspan = 7)
        randombutton = tk.Button(ihateall, text = "Randomize", command = randomize)
        randombutton.grid(row = 0, column = 3, pady = 5)
        resetbutton = tk.Button(ihateall, text = "Reset All", command = reset)
        resetbutton.grid(row = 0, column = 4, pady = 5)
        resetbutton = tk.Button(ihateall, text = "About", command = about)
        resetbutton.grid(row = 0, column = 5, pady = 5)
        randombutton = tk.Button(staghfoullah, text = "RESULTS!", command = results, font = 30, bd = 4)
        randombutton.grid(row = 1, column = 4)
        

        

########################### ECRANS
## MAIN HERE
        ylieu = 1
        zlieu = 1
        ultlieu = 1
        for room in rooms:
            nomlieu = tk.Label(self, text = f"{room.name}", pady = 5)
            if ylieu < 6:
                nomlieu.grid(row = 1, column = ylieu)
                ylieu = ylieu + 1
            elif zlieu < 6:
                nomlieu.grid(row = 3, column = zlieu)
                zlieu = zlieu + 1
            elif ultlieu < 6:
                nomlieu.grid(row = 5, column = ultlieu)
                ultlieu = ultlieu + 1


########################################## LISTES LIEUX

## IMPLANTATION DES EVENTS

        def lieu1(event):
            gestion_char(self, sroom1, room1)
        def lieu2(event):
            gestion_char(self, sroom2, room2)
        def lieu3(event):
            gestion_char(self, sroom3, room3)
        def lieu4(event):
            gestion_char(self, sroom4, room4)
        def lieu5(event):
            gestion_char(self, sroom5, room5)
        def lieu6(event):
            gestion_char(self, sroom6, room6)
        def lieu7(event):
            gestion_char(self, sroom7, room7)
        def lieu8(event):
            gestion_char(self, sroom8, room8)
        def lieu9(event):
            gestion_char(self, sroom9, room9)
        def lieu10(event):
            gestion_char(self, sroom10, room10)
        def lieu11(event):
            gestion_char(self, sroom11, room11)
        def lieu12(event):
            gestion_char(self, sroom12, room12)
        def lieu13(event):
            gestion_char(self, sroom13, room13)
        def lieu14(event):
            gestion_char(self, sroom14, room14)
        def lieu15(event):
            gestion_char(self, sroom15, room15)
### IMPLANTATION DES LISTES
        sroom1 = Slistbox(self)
        sroom1.bind('<Double-1>', lieu1)
        sroom1.grid(column = 1, row = 2, padx = 5)
        sroom2 = Slistbox(self)
        sroom2.bind('<Double-1>', lieu2)
        sroom2.grid(column = 2, row = 2, padx = 5)
        sroom3 = Slistbox(self)
        sroom3.bind('<Double-1>', lieu3)
        sroom3.grid(column = 3, row = 2, padx = 5)
        sroom4 = Slistbox(self)
        sroom4.bind('<Double-1>', lieu4)
        sroom4.grid(column = 4, row = 2, padx = 5)
        sroom5 = Slistbox(self)
        sroom5.bind('<Double-1>', lieu5)
        sroom5.grid(column = 5, row = 2, padx = 5)
# RANG 2
        sroom6 = Slistbox(self)
        sroom6.bind('<Double-1>', lieu6)
        sroom6.grid(column = 1, row = 4)
        sroom7 = Slistbox(self)
        sroom7.bind('<Double-1>', lieu7)
        sroom7.grid(column = 2, row = 4)
        sroom8 = Slistbox(self)
        sroom8.bind('<Double-1>', lieu8)
        sroom8.grid(column = 3, row = 4)
        sroom9 = Slistbox(self)
        sroom9.bind('<Double-1>', lieu9)
        sroom9.grid(column = 4, row = 4)
        sroom10 = Slistbox(self)
        sroom10.bind('<Double-1>', lieu10)
        sroom10.grid(column = 5, row = 4)
# RANG 3
        sroom11 = Slistbox(self)
        sroom11.bind('<Double-1>', lieu11)
        sroom11.grid(column = 1, row = 6)
        sroom12 = Slistbox(self)
        sroom12.bind('<Double-1>', lieu12)
        sroom12.grid(column = 2, row = 6)
        sroom13 = Slistbox(self)
        sroom13.bind('<Double-1>', lieu13)
        sroom13.grid(column = 3, row = 6)
        sroom14 = Slistbox(self)
        sroom14.bind('<Double-1>', lieu14)
        sroom14.grid(column = 4, row = 6)
        sroom15 = Slistbox(self)
        sroom15.bind('<Double-1>', lieu15)
        sroom15.grid(column = 5, row = 6)

 ### RANDOM
        listeslieu = [sroom1, sroom2, sroom3, sroom4, sroom5, sroom6, sroom7, sroom8, sroom9, sroom10, sroom11, sroom12, sroom13, sroom14, sroom15]

if __name__ == "__main__":
    kaos = Kaos()
    kaos.mainloop()
