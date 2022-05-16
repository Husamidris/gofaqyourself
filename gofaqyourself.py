from tkinter import *
fields = 'Die Frage:', 'Die Antwort:', 'Erfasst vom:', 'Datum:','Suche:'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=11, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=50, pady=7)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='speichern',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='suchen', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='alle anzeigen', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   b4 = Button(root, text='löschen', command=root.quit)
   b4.pack(side=LEFT, padx=5, pady=5)
   b5 = Button(root, text='schließen', command=root.quit)
   b5.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
