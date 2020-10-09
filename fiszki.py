import tkinter as tk
from tkinter import W, E, S, N
import pandas as pd
import numpy as np
from tkinter import messagebox

import os

directory = os.getcwd()


dt1 = pd.read_excel(os.path.join(directory, 'database/1.xlsx'))
dt2 = pd.read_excel(os.path.join(directory, 'database/2.xlsx'))
dt3 = pd.read_excel(os.path.join(directory, 'database/3.xlsx'))
dt4 = pd.read_excel(os.path.join(directory, 'database/4.xlsx'))
dt5 = pd.read_excel(os.path.join(directory, 'database/5.xlsx'))


class Mainapp:
    def __init__(self, master):
        #master window  default definitions
        self.master = master
        self.master.geometry('300x400+850+300')
        self.master.title('Fiszki')
        self.master.iconbitmap(r'icon.ico')


        # Create labels, entries,buttons
        self.label_1 = tk.Label(self.master, text="Aplikacja Fiszki\nCreated by Cezary Angielczyk")
        self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=75)

        #frame 1
        self.frame_1 = tk.LabelFrame(self.master,text="Nowe fiszki",pady=10)
        self.frame_1.grid(row=1, column=0, columnspan=2,sticky=W+E)

        #button add flashcard
        self.button_addfc = tk.Button(self.frame_1, text="Dodaj nowe fiszki",
                                      width=30, bd=2,
                                      command=lambda: self.button_click(1))
        self.button_addfc.grid(row=0, column=2, padx=35, sticky=W+E)

        # frame 2
        self.frame_2 = tk.LabelFrame(self.master, text="Ucz się fiszek", pady=10)
        self.frame_2.grid(row=2, column=0, columnspan=2, sticky=W + E)

        #buttons flashcards
        self.button_fc1 = tk.Button(self.frame_2, text="Fiszki 1", width=30,
                                    bd=2, command=lambda: self.button_click(2))
        self.button_fc2 = tk.Button(self.frame_2, text="Fiszki 2", width=30,
                                    bd=2, command=lambda: self.button_click(3))
        self.button_fc3 = tk.Button(self.frame_2, text="Fiszki 3", width=30,
                                    bd=2, command=lambda: self.button_click(4))
        self.button_fc4 = tk.Button(self.frame_2, text="Fiszki 4", width=30,
                                    bd=2, command=lambda: self.button_click(5))
        self.button_fc5 = tk.Button(self.frame_2, text="Fiszki 5", width=30,
                                    bd=2, command=lambda: self.button_click(6))

        #buttons grid
        self.button_fc1.grid(row=0, column=0,columnspan=2,padx=35, pady=5,
                             sticky=W+E)
        self.button_fc2.grid(row=1, column=0, columnspan=2, padx=35, pady=5,
                             sticky=W + E)
        self.button_fc3.grid(row=2, column=0, columnspan=2, padx=35, pady=5,
                             sticky=W + E)
        self.button_fc4.grid(row=3, column=0, columnspan=2, padx=35, pady=5,
                             sticky=W + E)
        self.button_fc5.grid(row=4, column=0, columnspan=2, padx=35, pady=5,
                             sticky=W + E)

        #exit button
        self.button_exit = tk.Button(self.master, text="Wyjdź z programu",
                                     command= self.master.destroy)
        self.button_exit.grid(row=3, column=1, pady=30)


    def button_click(self, button_number):
        if button_number==1:
            Window_afc()

        if button_number==2:
            try:
                Window_fc1()
            except:
                messagebox.showwarning("Brak słówek", "Brak słówek do nauki, dodaj nowe słówka")
        if button_number==3:
            try:
                Window_fc2()
            except:
                messagebox.showwarning("Brak słówek",
                                       "Brak słówek do nauki, dodaj nowe słówka")
        if button_number==4:
            try:
                Window_fc3()
            except:
                messagebox.showwarning("Brak słówek",
                                       "Brak słówek do nauki, dodaj nowe słówka")
        if button_number==5:
            try:
                Window_fc4()
            except:
                messagebox.showwarning("Brak słówek",
                                       "Brak słówek do nauki, dodaj nowe słówka")
        if button_number==6:
            try:
                Window_fc5()
            except:
                messagebox.showwarning("Brak słówek",
                                       "Brak słówek do nauki, dodaj nowe słówka")


class Window_afc(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Dodaj nową fiszke')
       self.master.iconbitmap(r'icon.ico')



       #sterujace
       self.f_slowo = ""
       self.s_slowo = ""


        #UI
       self.label_1 = tk.Label(self.master,
                               text="Dodawaj nowe fiszki\nnajpierw podaj słówko po polsku\n"
                                    "a następnie podaj tłumaczenie")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=60)
       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Dodaj Słówko", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       #slowko
       self.slowko = tk.Entry(self.frame, width=40)
       self.slowko.pack()
       self.slowko.insert(0,"Podaj polskie słówko: ")
       #zmmienna sterująca
       self.slowko_state = "PL"


       #button do slowka
       self.slowko_button = tk.Button(self.master, text='Dodaj slowko',
                                      padx=60, command=self.get_text)
       self.slowko_button.grid(row=2, column=0, pady=30, sticky=W + E, padx=40)

       # button invoke
       self.master.bind('<Return>', self.get_text)

        #exit button
       self.exit_button = tk.Button(self.master, text='Powrót',
                                    command=self.master.destroy, padx=60)
       self.exit_button.grid(row=3, column=0, pady=150, sticky=W + E, padx=40)

    #funkcje


   def get_text(self,event=None):
       '''Funkcja odpowiedzialna za działanie buttona do zapisu słowka
       korzysta ze zmiennej sterującej slowko.state, która wskazuje
       gdzie wpisany tekst ma zostac zapisany czy jako slowko(PL) czy jako
       tlumaczenie slowka(EN)'''
       global dt1
       if self.slowko_state == "PL":

           slowko_1 = self.slowko.get()
           self.f_slowo = slowko_1[22:]

           if len(self.f_slowo)==0:
               messagebox.showwarning(title="Uwaga",
                                      message="Wprowadzono błędne słowo")
               self.master.destroy()

           self.slowko_state = "EN"
           self.slowko.delete(0, tk.END)
           self.slowko.insert(0, "Podaj angielskie słówko: ")
       elif self.slowko_state == "EN":
           slowko_2 = self.slowko.get()
           self.slowko.delete(0, tk.END)
           self.s_slowo = slowko_2[25:]
           if len(self.s_slowo)==0:
               messagebox.showwarning(title="Uwaga",
                                      message="Wprowadzono błędne słowo")
               self.master.destroy()
           slownik = {'Slowo': self.f_slowo,
          'Tlumaczenie': self.s_slowo}
           dt1 = dt1.append(slownik, ignore_index=True)

           dt1.to_excel('database/1.xlsx', index=False)
           self.slowko_state = "PL"
           self.slowko.delete(0, tk.END)
           self.slowko.insert(0, "Podaj polskie słówko: ")




class Window_fc1(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Fiszki 1')
       self.master.iconbitmap(r'icon.ico')


       #zmienne sterujące
       self.var_slowko = dt1['Slowo'][0]
       self.var_dobrze_zle = "-----"

       #UI
       self.label_1 = tk.Label(self.master,
                      text="Fiszki pudełko 1\nTutaj znajduja sie nowe fiszki\n"
                           "Jest to pierwszy etap nauki")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=75)

       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Słówko po polsku", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       self.slowko = tk.Label(self.frame, text=self.var_slowko)
       self.slowko.pack()

       # frame 2 tlumaczenie
       self.frame2 = tk.LabelFrame(self.master, text="Wpisz tłumaczenie",
                                   pady=10)
       self.frame2.grid(row=2, column=0, columnspan=2, sticky=W + E)

       self.tlumaczenie = tk.Entry(self.frame2)
       self.tlumaczenie.pack()

       # frame 3 wynik

       self.frame3 = tk.LabelFrame(self.master, text="Wynik", pady=10)
       self.frame3.grid(row=4, column=0, columnspan=2, sticky=W + E)

       self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
       self.wynik.pack()

       # sprawdz button

       self.check_button = tk.Button(self.master, text='Sprawdz słówko', padx=60,
                                     command=self.check_click)
       self.check_button.grid(row=3, column=0, pady=30, sticky=W + E, padx=30)

       # button invoke
       self.master.bind('<Return>', self.check_click)

       # exit button
       self.exit_button = tk.Button(self.master, text='Powrót', command=self.master.destroy,
                            padx=60)
       self.exit_button.grid(row=5, column=0, pady=30, sticky=W + E, padx=30)

    #funkcje
   def check_click(self, event=None):
       global dt1
       global dt2
       try:
           en = dt1['Tlumaczenie'][0]
           x = self.tlumaczenie.get()
           if x.lower() == en.lower():
               dt2 = dt2.append(dt1.loc[0, :])
               dt1 = dt1.drop(0)
               dt1.reset_index(inplace=True, drop=True)
               dt2.reset_index(inplace=True, drop=True)
               dt1.to_excel('database/1.xlsx', index=False)
               dt2.to_excel('database/2.xlsx', index=False)

               #update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle="Dobrze"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               #update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt1['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               #update entry
               self.tlumaczenie.delete(0, tk.END)

           else:
               dt1 = dt1.append(dt1.loc[0, :], ignore_index=True)
               dt1 = dt1.drop(0)
               dt1.reset_index(inplace=True, drop=True)
               dt1.to_excel('database/1.xlsx', index=False)

               #update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Zle"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               #update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt1['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               #update entry
               self.tlumaczenie.delete(0, tk.END)
       except:
           messagebox.showinfo("Brak słówek", "Nie ma więcej słówek"
                                              " w Fiszkach 1 dodaj nowe słówka"
                                              " albo rób fiszki 2")
           self.master.destroy()






class Window_fc2(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Fiszki 2')
       self.master.iconbitmap(r'icon.ico')

       # zmienne sterujące
       self.var_slowko = dt2['Slowo'][0]
       self.var_dobrze_zle = "-----"

       # UI
       self.label_1 = tk.Label(self.master,
                               text="Fiszki pudełko 2\nDrugi etap nauki\n"
                                    "Powtarzaj słówka, których się nauczyłeś\n"
                                    "z pierwszego etapu")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Słówko po polsku", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       self.slowko = tk.Label(self.frame, text=self.var_slowko)
       self.slowko.pack()

       # frame 2 tlumaczenie
       self.frame2 = tk.LabelFrame(self.master, text="Wpisz tłumaczenie",
                                   pady=10)
       self.frame2.grid(row=2, column=0, columnspan=2, sticky=W + E)

       self.tlumaczenie = tk.Entry(self.frame2)
       self.tlumaczenie.pack()

       # frame 3 wynik

       self.frame3 = tk.LabelFrame(self.master, text="Wynik", pady=10)
       self.frame3.grid(row=4, column=0, columnspan=2, sticky=W + E)

       self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
       self.wynik.pack()

       # sprawdz button

       self.check_button = tk.Button(self.master, text='Sprawdz słówko',
                                     padx=60, command=self.check_click)
       self.check_button.grid(row=3, column=0, pady=30, sticky=W + E, padx=30)

       # button invoke
       self.master.bind('<Return>', self.check_click)

       # exit button
       self.exit_button = tk.Button(self.master, text='Powrót',
                                    command=self.master.destroy, padx=60)
       self.exit_button.grid(row=5, column=0, pady=20, sticky=W + E, padx=30)

       # funkcje

   def check_click(self, event=None):
       global dt2
       global dt3
       try:
           en = dt2['Tlumaczenie'][0]
           x = self.tlumaczenie.get()
           if x.lower() == en.lower():
               dt3 = dt3.append(dt2.loc[0, :])
               dt2 = dt2.drop(0)
               dt2.reset_index(inplace=True, drop=True)
               dt3.reset_index(inplace=True, drop=True)
               dt2.to_excel('database/2.xlsx', index=False)
               dt3.to_excel('database/3.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Dobrze"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt2['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)

           else:
               dt2 = dt2.append(dt2.loc[0, :], ignore_index=True)
               dt2 = dt2.drop(0)
               dt2.reset_index(inplace=True, drop=True)
               dt2.to_excel('database/2.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Zle"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt2['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)
       except:
           messagebox.showinfo("Brak słówek", "Nie ma więcej słówek"
                                              " w Fiszkach 2 dodaj nowe słówka"
                                              " albo rób fiszki 3")
           self.master.destroy()


class Window_fc3(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Fiszki 3')
       self.master.iconbitmap(r'icon.ico')



       # zmienne sterujące
       self.var_slowko = dt3['Slowo'][0]
       self.var_dobrze_zle = "-----"

       # UI
       self.label_1 = tk.Label(self.master,
                               text="Fiszki pudełko 3\nTrzeci etap nauki\n"
                                    "Powtarzaj słówka, których się nauczyłeś\n"
                                    "z drugiego etapu")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Słówko po polsku", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       self.slowko = tk.Label(self.frame, text=self.var_slowko)
       self.slowko.pack()

       # frame 2 tlumaczenie
       self.frame2 = tk.LabelFrame(self.master, text="Wpisz tłumaczenie",
                                   pady=10)
       self.frame2.grid(row=2, column=0, columnspan=2, sticky=W + E)

       self.tlumaczenie = tk.Entry(self.frame2)
       self.tlumaczenie.pack()

       # frame 3 wynik

       self.frame3 = tk.LabelFrame(self.master, text="Wynik", pady=10)
       self.frame3.grid(row=4, column=0, columnspan=2, sticky=W + E)

       self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
       self.wynik.pack()

       # sprawdz button

       self.check_button = tk.Button(self.master, text='Sprawdz słówko',
                                     padx=60, command=self.check_click)
       self.check_button.grid(row=3, column=0, pady=30, sticky=W + E, padx=30)

       # button invoke
       self.master.bind('<Return>', self.check_click)

       # exit button
       self.exit_button = tk.Button(self.master, text='Powrót',
                                    command=self.master.destroy, padx=60)
       self.exit_button.grid(row=5, column=0, pady=30, sticky=W + E, padx=30)

       # funkcje

   def check_click(self, event=None):
       global dt3
       global dt4
       try:
           en = dt3['Tlumaczenie'][0]
           x = self.tlumaczenie.get()
           if x.lower() == en.lower():
               dt4 = dt4.append(dt3.loc[0, :])
               dt3 = dt3.drop(0)
               dt3.reset_index(inplace=True, drop=True)
               dt4.reset_index(inplace=True, drop=True)
               dt3.to_excel('database/3.xlsx', index=False)
               dt4.to_excel('database/4.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Dobrze"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt3['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)

           else:
               dt3 = dt3.append(dt3.loc[0, :], ignore_index=True)
               dt3 = dt3.drop(0)
               dt3.reset_index(inplace=True, drop=True)
               dt3.to_excel('database/3.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Zle"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt3['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)
       except:
           messagebox.showinfo("Brak słówek", "Nie ma więcej słówek"
                                              " w Fiszkach 3 dodaj nowe słówka"
                                              " albo rób fiszki 4")
           self.master.destroy()


class Window_fc4(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Fiszki 4')
       self.master.iconbitmap(r'icon.ico')



       # zmienne sterujące
       self.var_slowko = dt4['Slowo'][0]
       self.var_dobrze_zle = "-----"

       # UI
       self.label_1 = tk.Label(self.master, text="Fiszki pudełko 4\n"
                                                 "Czwarty przedostatni etap nauki\n"
                                                 "Powtarzaj słówka, których się nauczyłeś\n"
                                                 "z trzeciego etapu")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Słówko po polsku", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       self.slowko = tk.Label(self.frame, text=self.var_slowko)
       self.slowko.pack()

       # frame 2 tlumaczenie
       self.frame2 = tk.LabelFrame(self.master, text="Wpisz tłumaczenie",
                                   pady=10)
       self.frame2.grid(row=2, column=0, columnspan=2, sticky=W + E)

       self.tlumaczenie = tk.Entry(self.frame2)
       self.tlumaczenie.pack()

       # frame 3 wynik

       self.frame3 = tk.LabelFrame(self.master, text="Wynik", pady=10)
       self.frame3.grid(row=4, column=0, columnspan=2, sticky=W + E)

       self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
       self.wynik.pack()

       # sprawdz button

       self.check_button = tk.Button(self.master, text='Sprawdz słówko',
                                     padx=60, command=self.check_click)
       self.check_button.grid(row=3, column=0, pady=30, sticky=W + E, padx=30)

       # button invoke
       self.master.bind('<Return>', self.check_click)

       # exit button
       self.exit_button = tk.Button(self.master, text='Powrót',
                                    command=self.master.destroy, padx=60)
       self.exit_button.grid(row=5, column=0, pady=30, sticky=W + E, padx=30)

       # funkcje

   def check_click(self, event=None):
       global dt4
       global dt5
       try:
           en = dt4['Tlumaczenie'][0]
           x = self.tlumaczenie.get()
           if x.lower() == en.lower():
               dt5 = dt5.append(dt4.loc[0, :])
               dt4 = dt4.drop(0)
               dt4.reset_index(inplace=True, drop=True)
               dt5.reset_index(inplace=True, drop=True)
               dt4.to_excel('database/4.xlsx', index=False)
               dt5.to_excel('database/5.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Dobrze"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt4['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)

           else:
               dt4 = dt4.append(dt4.loc[0, :], ignore_index=True)
               dt4 = dt4.drop(0)
               dt4.reset_index(inplace=True, drop=True)
               dt4.to_excel('database/4.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Zle"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt4['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)
       except:
           messagebox.showinfo("Brak słówek", "Nie ma więcej słówek"
                                              " w Fiszkach 4 dodaj nowe słówka"
                                              " albo rób fiszki 5")
           self.master.destroy()


class Window_fc5(tk.Toplevel):
   def __init__(self):
       self.master = tk.Toplevel()
       self.master.geometry('300x400+850+300')
       self.master.title('Fiszki 5')
       self.master.iconbitmap(r'icon.ico')


       # zmienne sterujące
       self.var_slowko = dt5['Slowo'][0]
       self.var_dobrze_zle = "-----"

       # UI
       self.label_1 = tk.Label(self.master, text="Fiszki pudełko 5\n"
                                                 "Ostatni etap nauki\n"
                                                 "Powtarzaj słówka, których się nauczyłeś\n"
                                                 "z czwartego etapu")
       self.label_1.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

       # frame 1 slowko
       self.frame = tk.LabelFrame(self.master, text="Słówko po polsku", pady=10)
       self.frame.grid(row=1, column=0, columnspan=2, sticky=W + E)

       self.slowko = tk.Label(self.frame, text=self.var_slowko)
       self.slowko.pack()

       # frame 2 tlumaczenie
       self.frame2 = tk.LabelFrame(self.master, text="Wpisz tłumaczenie",
                                   pady=10)
       self.frame2.grid(row=2, column=0, columnspan=2, sticky=W + E)

       self.tlumaczenie = tk.Entry(self.frame2)
       self.tlumaczenie.pack()

       # frame 3 wynik

       self.frame3 = tk.LabelFrame(self.master, text="Wynik", pady=10)
       self.frame3.grid(row=4, column=0, columnspan=2, sticky=W + E)

       self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
       self.wynik.pack()

       # sprawdz button

       self.check_button = tk.Button(self.master, text='Sprawdz słówko',
                                     padx=60, command=self.check_click)
       self.check_button.grid(row=3, column=0, pady=30, sticky=W + E, padx=30)

       # button invoke
       self.master.bind('<Return>', self.check_click)

       # exit button
       self.exit_button = tk.Button(self.master, text='Powrót',
                                    command=self.master.destroy, padx=60)
       self.exit_button.grid(row=5, column=0, pady=20, sticky=W + E, padx=30)

       # funkcje

   def check_click(self, event=None):
       global dt5
       try:
           en = dt5['Tlumaczenie'][0]
           x = self.tlumaczenie.get()
           if x.lower() == en.lower():
               dt5 = dt5.drop(0)
               dt5.reset_index(inplace=True, drop=True)
               dt5.to_excel('database/5.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Dobrze"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt5['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)

           else:
               dt5 = dt5.append(dt5.loc[0, :], ignore_index=True)
               dt5 = dt5.drop(0)
               dt5.reset_index(inplace=True, drop=True)
               dt5.to_excel('database/5.xlsx', index=False)

               # update wynik
               self.wynik.pack_forget()
               self.var_dobrze_zle = "Zle"
               self.wynik = tk.Label(self.frame3, text=self.var_dobrze_zle)
               self.wynik.pack()
               # update slowko
               self.slowko.pack_forget()
               self.var_slowko = dt5['Slowo'][0]
               self.slowko = tk.Label(self.frame, text=self.var_slowko)
               self.slowko.pack()
               # update entry
               self.tlumaczenie.delete(0, tk.END)
       except:
           messagebox.showinfo("Brak słówek", "Nie ma więcej słówek"
                                              " w Fiszkach 5 dodaj nowe słówka"
                                              " Bo te już umiesz perfekcyjnie")
           self.master.destroy()




def main(): #run mianloop
    root = tk.Tk()
    app = Mainapp(root)
    root.mainloop()

if __name__ == '__main__':
    main()