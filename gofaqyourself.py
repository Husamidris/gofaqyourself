# https://github.com/spyridongeorgiou/gofaqyourself

import tkinter as tk # Für GUI
import pandas as pd # Für die Datenbank in JSON/CSV/XML für eins Entscheiden --> JSON

Frage = str([]) # Frage in eine leere Liste und dann in str() konvertieren
##FrageDict = {"Frage": Frage} # 
FrageID = str([])
##IDDict = {"ID": ID}
faqdata = [
    {"FrageID":FrageID,"Frage":Frage,}
]

fields = 'Frage', 'Antwort', 'Beantwortet durch', 'Eintrittsdatum'
def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 
def makeform(root, fields):
   entries = []
   for field in fields:
      row = tk.Frame(root)
      lab = tk.Label(row, width=15, text=field, anchor='w')
      ent = tk.Entry(row)
      row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
      lab.pack(side=tk.LEFT)
      ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
      entries.append((field, ent))
   return entries
if __name__ == '__main__': # Führt nur den Code aus wenn dunder Methode __name__ den Wert "__main__" zurückgibt
   root = tk.Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = tk.Button(root, text='Speichern',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=tk.LEFT, padx=5, pady=5)
   b2 = tk.Button(root, text='Quit', command=root.quit)
   b2.pack(side=tk.LEFT, padx=5, pady=5)
   root.mainloop()