
def create_password(event):
    global x
    check1()

    try:
        x = int(x) - 1
        passw = ""
    except:
        messagebox.showerror("Ошибка!", "Введите количество символов цифрами!")
        return

    if int(x) > 999:
        messagebox.showerror("Ошибка!", "Максимальное число 1000")
        return
    if int(x) < -1:
        messagebox.showerror("Ошибка!", "Длина не может быть меньше нуля!")
        return
    if str(x) == "-1":
        messagebox.showerror("Ошибка!", "Длина не может нулем!")
        return

    lt1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
           "v", "b", "n", "m", ]
    lt2 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C",
           "V", "B", "N", "M"]
    lt3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lt4 = ["`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "/", "|", ";",
           ":", "'", ",", ".", "<", ">", "?"]

    if v0 == "0":
        if v1 == "0":
            if v2 == "0":
                if v3 == "0":
                    messagebox.showerror("Ошибка!", "Выберите из чего \nсоздать пароль")
    if v0 == "1":
        if v1 == "1":
            if v2 == "1":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt2 + lt3 + lt4)

    if v0 == "1":
        if v1 == "0":
            if v2 == "0":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt3)
    if v0 == "0":
        if v1 == "1":
            if v2 == "0":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt2)
    if v0 == "0":
        if v1 == "0":
            if v2 == "1":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt1)
    if v0 == "0":
        if v1 == "0":
            if v2 == "0":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt4)
    if v0 == "0":
        if v1 == "1":
            if v2 == "1":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt2 + lt4)
    if v0 == "0":
        if v1 == "0":
            if v2 == "1":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt2 + lt4)
    if v0 == "1":
        if v1 == "0":
            if v2 == "0":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt3 + lt4)
    if v0 == "0":
        if v1 == "1":
            if v2 == "0":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt2 + lt4)
    if v0 == "1":
        if v1 == "0":
            if v2 == "1":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt3 + lt1)
    if v0 == "0":
        if v1 == "1":
            if v2 == "1":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt2)
    if v0 == "1":
        if v1 == "1":
            if v2 == "1":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt2 + lt3)
    if v0 == "0":
        if v1 == "1":
            if v2 == "1":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt2 + lt4)
    if v0 == "1":
        if v1 == "0":
            if v2 == "1":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt1 + lt3 + lt4)
    if v0 == "1":
        if v1 == "1":
            if v2 == "0":
                if v3 == "1":
                    while len(passw) <= int(x):
                        passw += choice(lt2 + lt3 + lt4)
    if v0 == "1":
        if v1 == "1":
            if v2 == "0":
                if v3 == "0":
                    while len(passw) <= int(x):
                        passw += choice(lt2 + lt3)
    if copy1 == "1":
        root.clipboard_clear()
        root.clipboard_append(passw)
    text1.delete("1.0", END)
    text1.insert("1.0", passw)

