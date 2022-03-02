from tkinter import Tk, Text

text = '''Здесь должен/а быть метод/функция который/ая будет читать/возвращать текст в файле который мы открыли: text.qip'''
root = Tk()

txt = Text()
txt.pack()
txt.insert(0.1, text)

root.mainloop()