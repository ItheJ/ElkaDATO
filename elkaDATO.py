from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
import os
import sys

tk = Tk()

tk.title("Шифровщик elkaDATO")
tk["bg"] = "#ffe993"
tk.minsize(400,300)
tk.maxsize(400,300)

paths = ["sample.doc"]
encode = ["utf-8"]


def file_create():
    if not text_zone.edit_modified():      
        text_zone.delete('1.0', END)
    else:        
        save_file_as()
          
        text_zone.delete('1.0', END)  
    
    text_zone.edit_modified(0) 

def open_file():
    if not text_zone.edit_modified():       
            try:            
                path = filedialog.askopenfile(filetypes = (("Шифр формата Новой Империи Ёлок", "*.ffne"),("Все файлы", "*.*"))).name

                paths.clear()
                paths.append(path)       
            
                with open(paths[0], 'r', encoding=encode[0]) as f:             
                    content = f.read()
                    text_zone.delete('1.0', END)
                    text_zone.insert('1.0', content)
                                
                    text_zone.edit_modified(0)

                tk.title('Открыт шифр - ' + paths[0])
             
            except UnicodeDecodeError:
                msg.showwarning(title="Ошибка!", message="Упс! Не удалось открыть файл с установленной кодировкой. Файл будет открыт в кодировке Utf 8, после чего она будет установлена за место прошлой установленной кодировки.")
                encode[0] = "utf-8"

                try:
                
                   with open(paths[0], 'r', encoding=encode[0]) as f:             
                       content = f.read()
                       text_zone.delete('1.0', END)
                       text_zone.insert('1.0', content)
                                   
                       text_zone.edit_modified(0)

                   tk.title('Открыт файл - ' + paths[0])
                   
                except UnicodeDecodeError:
                   msg.showwarning(title="Ошибка!", message="Упс! Не удалось открыть файл с кодировкой Utf 8. Похоже, он повреждён или файл не может быть открыт в текстовом режиме")
            except LookupError:
                   msg.showwarning(title="Ошибка!", message="Упс! Вы не установили кодировку при открытии файла! Изначальной кодировкой будет назначена Utf 8")

                   encode[0] = "utf-8"
                   
    else:   
            save_file_as()
        
            text_zone.edit_modified(0)              
            open_file()

def save_file():
    if paths[0] != '':
        
        with open(paths[0], 'w', encoding=encode[0]) as f:
            content = text_zone.get('1.0', END)
            f.write(content)

        tk.title('Сохранён по пути - ' + paths[0])
      
    else:
        save_file_as()   

def save_file_as():
    try:

        paths.clear()
        path = filedialog.asksaveasfile(filetypes = (("Шифр формата Новой Империи Ёлок", "*.ffne"),("Все файлы", "*.*"))).name

        if not "." in path:
            path = path + ".ffne"
        paths.append(path)
            
        tk.title('Сохранён по пути - ' + paths[0])
    
    except:
        return   
    
    with open(path, 'w', encoding=encode[0]) as f:
        f.write(text_zone.get('1.0', END))

def shiphering():
    text = text_zone.get("1.0", END)

    text = text.upper()

    text = text.replace("Ё", "聖誕樹")
    text = text.replace("Л", "松樹")
    text = text.replace("К", "帝國")
    
    text = text.replace("А", "Ёлка")
    text = text.replace("Б", "ёЛка")
    text = text.replace("В", "ёлКа")
    text = text.replace("Г", "ёлкА")
    text = text.replace("Д", "ЁЛка")
    text = text.replace("Е", "ЁлКа")
    text = text.replace("Ж", "ЁлкА")
    text = text.replace("З", "ёЛКа")
    text = text.replace("И", "ёЛкА")
    text = text.replace("Й", "ёлКА")
    text = text.replace("М", "Елка")
    text = text.replace("Н", "ЁЛКа")
    text = text.replace("О", "ЁЛкА")
    text = text.replace("П", "ЁлКА")
    text = text.replace("Р", "ЁЛКА")
    text = text.replace("С", "ёлка")

    
    text = text.replace("Щ", "сосна")
    text = text.replace("Ъ", "Сосна")
    text = text.replace("Ы", "сОсна")
    text = text.replace("Ь", "соСна")
    text = text.replace("Э", "сосНа")
    text = text.replace("Ю", "соснА")
    text = text.replace("Я", "СОсна")

    text = text.replace("Т", "ель")
    text = text.replace("У", "Ель")
    text = text.replace("Ф", "еЛь")
    text = text.replace("Х", "елЬ")
    text = text.replace("Ц", "ЕЛь")
    text = text.replace("Ч", "ЕлЬ")
    text = text.replace("Ш", "еЛЬ")

    text = text.replace("0", "🌲🌲")
    text = text.replace("1", "🎄🎄")
    text = text.replace("2", "🌲🎄🌲")
    text = text.replace("3", "🌲🎄🎄")
    text = text.replace("4", "🎄🌲🎄")
    text = text.replace("5", "🌲🌲🌲")


    text = text.replace("6", "🎄🎄🎄")
    text = text.replace("7", "🎄🎄🌲")
    text = text.replace("8", "🌲🎄🌲🎄")
    text = text.replace("9", "🎄🌲🎄🌲")

    text_zone.delete('1.0', END)
    text_zone.insert('1.0', text)
    

def deshiphering():
    text = text_zone.get("1.0", END)

    text = text.replace("聖誕樹", "Ё")
    text = text.replace("松樹", "Л")
    text = text.replace("帝國", "К")


    text = text.replace("🌲🎄🌲🎄", "8")
    text = text.replace("🎄🌲🎄🌲", "9")
    
    text = text.replace("🌲🎄🌲", "2")
    text = text.replace("🌲🎄🎄", "3")
    text = text.replace("🎄🌲🎄", "4")
    text = text.replace("🌲🌲🌲", "5")


    text = text.replace("🎄🎄🎄", "6")
    text = text.replace("🎄🎄🌲", "7")
    

    text = text.replace("🌲🌲", "0")
    text = text.replace("🎄🎄", "1")

    text = text.replace("сосна", "Щ")
    text = text.replace("Сосна", "Ъ")
    text = text.replace("сОсна", "Ы")
    text = text.replace("соСна", "Ь")
    text = text.replace("сосНа", "Э")
    text = text.replace("соснА", "Ю")
    text = text.replace("СОсна", "Я")

    text = text.replace("ель", "Т")
    text = text.replace("Ель", "У")
    text = text.replace("еЛь", "Ф")
    text = text.replace("елЬ", "Х")
    text = text.replace("ЕЛь", "Ц")
    text = text.replace("ЕлЬ", "Ч")
    text = text.replace("еЛЬ", "Ш")

    text = text.replace("Ёлка", "А")
    text = text.replace("ёЛка", "Б")
    text = text.replace("ёлКа", "В")
    text = text.replace("ёлкА", "Г")
    text = text.replace("ЁЛка", "Д")
    text = text.replace("ЁлКа", "Е")
    text = text.replace("ЁлкА", "Ж")
    text = text.replace("ёЛКа", "З")
    text = text.replace("ёЛкА", "И")
    text = text.replace("ёлКА", "Й")
    text = text.replace("Елка", "М")
    text = text.replace("ЁЛКа", "Н")
    text = text.replace("ЁЛкА", "О")
    text = text.replace("ЁлКА", "П")
    text = text.replace("ЁЛКА", "Р")
    text = text.replace("ёлка", "С")

    text_zone.delete('1.0', END)
    text_zone.insert('1.0', text)

def about():
    toplvl = Toplevel()

    toplvl.title("О шифровщике elkaDATO")
    
    toplvl.minsize(400,300)
    toplvl.maxsize(400,300)

    canvas = Canvas(toplvl, bg="#ffe993", width=420, height=320)
    canvas.pack()

    img = PhotoImage(file="Tree.png")

    canvas.create_image(10, 10, anchor=NW, image=img)

    
    canvas.create_text(125, 25, anchor=NW, font = "Haettenschweiler 16", text="ElkaDATO ver. 1.0", fill="#000000")
    canvas.create_text(125, 70, anchor=NW, font = "Haettenschweiler 16", text="Основа - ElkaDATOKernel 'FT' 1.2, \nPSB Notepad ver. 2.0", fill="#000000")
    canvas.create_text(125, 140, anchor=NW, font = "Haettenschweiler 16", text="Все права сохранены, \nпредоставляется всем \nуправленцам Ёлочных государств и \nпросто людям", fill="#000000")
    canvas.create_text(10, 250, anchor=NW, font = "Haettenschweiler 16", text="PSB ent., elkaDATO©, 2025", fill="#000000")

    toplvl.mainloop()

def exit_session():
    if msg.askyesno("Шифровщик elkaDATO", "Вы действительно хотите закрыть программу? Все несохранённые данные будут утеряны!"):
        msg.showinfo("Шифровщик elkaDATO", "Завершение работы...")
        tk.destroy()
        sys.exit(0)
    else:
        msg.showinfo("Шифровщик elkaDATO", "Завершение работы отменено")
        

menubar = Menu(tk)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Создать шифр", command=file_create)

filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Открыть шифр...", command=open_file)

filemenu3 = Menu(menubar, tearoff=0)
filemenu3.add_command(label="Сохранить шифр", command=save_file)
filemenu3.add_command(label="Сохранить шифр как...", command=save_file_as)

filemenu5 = Menu(menubar, tearoff=0)
filemenu5.add_command(label="Зашифровать в новом стиле", command=shiphering)
filemenu5.add_command(label="Расшифровать в новом стиле", command=deshiphering)

filemenu_about = Menu(menubar, tearoff=0)
filemenu_about.add_command(label="О шифраторе", command=about)
filemenu_about.add_command(label="Завершить сессию", command=exit_session)


menubar.add_cascade(label="Создать...", menu=filemenu)
menubar.add_cascade(label="Открыть...", menu=filemenu2)
menubar.add_cascade(label="Сохранить...", menu=filemenu3)
menubar.add_cascade(label="Шифр...", menu=filemenu5)
menubar.add_cascade(label="Шифратор", menu=filemenu_about)

text_zone = Text(tk, bg = "#ffe993", font = ("Haettenschweiler", 20, "normal"))
text_zone.pack(expand = YES, fill = BOTH, side = LEFT)
scrollbar = ttk.Scrollbar(tk, orient=VERTICAL, command=text_zone.yview)
scrollbar.pack(fill=Y, side=RIGHT)
text_zone['yscrollcommand'] = scrollbar.set

tk.config(menu=menubar)
tk.mainloop()
