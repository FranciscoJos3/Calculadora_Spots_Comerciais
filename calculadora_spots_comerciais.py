import tkinter as tk

import re


def clean():
    text_entry.delete("1.0", tk.END)


def process():
    text = str(text_entry.get("1.0", tk.END))
    #espCarac = ('/', '(', ')', '+', '=', ':', ';', '[', '{', ']', '}', '|')
    #text = re.sub(espCarac, " ", text)
    text = text.replace("@", " arroba ")
    text = text.replace("#", " hashtag ")
    text = text.replace("%", " por cento ")
    text = text.replace("_", " underline ")
    text = text.replace("4x4", " quatro por quatro ")
    text = text.replace("4X4", " quatro por quatro ")
    text = text.replace('R$', ' reais ')
    text = re.sub(r'(?<=[a-zA-Z0-9])\.(?=[a-zA-Z0-9])', ' ponto ', text)
    text = re.sub(r'(?<=[0-9]),(?=[0-9])', ' e ', text)
    text = text.replace('.', '\n ')
    text = text.replace(',', '\n ')
    text = text.replace('?', '\n ')
    text = text.replace('!', '\n ')
    text = text.replace('-', '\n ')
    t = text.split()
    for ext in t:
        if ext.isnumeric():
            unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                        'oito', 'nove']
            dezenas = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
                       'dezessete', 'dezoito', 'dezenove']
            dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
                        'oitenta', 'noventa']
            centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
                        'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

            def numero_por_extenso(ext):
                e = int(ext)
                if e == 0:
                    return unidades[e]

                extenso = ""
                if e >= 2000000000:
                    extenso += numero_por_extenso(e // 1000000000) + " bilhões "
                    e %= 1000000000
                    if e > 0:
                        extenso += ' e '
                if e >= 1000000000:
                    extenso += numero_por_extenso(e // 1000000000) + " bilhão "
                    e %= 1000000000
                    if e > 0:
                        extenso += ' e '
                if e >= 2000000:
                    extenso += numero_por_extenso(e // 1000000) + " milhões "
                    e %= 1000000
                    if e > 0:
                        extenso += ' e '
                if e >= 1000000:
                    extenso += numero_por_extenso(e // 1000000) + " milhão "
                    e %= 1000000
                    if e > 0:
                        extenso += ' e '
                if e >= 2000:
                    extenso += numero_por_extenso(e // 1000) + " mil "
                    e %= 1000
                    if e > 0:
                        extenso += ' e '
                if e >= 1000:
                    extenso += " mil"
                    e %= 1000
                    if e > 0:
                        extenso += ' e '
                if e >= 100:
                    if e == 100:
                        extenso += 'cem'
                    else:
                        extenso += centenas[e // 100 - 1]
                    e %= 100
                    if e > 0:
                        extenso += ' e '
                if e >= 10:
                    if e < 20:
                        extenso += dezenas[e - 10]
                        e = 0
                    else:
                        extenso += dezenas2[e // 10 - 2] + " "
                        e %= 10
                        if e > 0:
                            extenso += ' e '
                if e > 0:
                    extenso += unidades[e] + " "
                return extenso.strip()
            text = text.replace(ext, numero_por_extenso(ext))

    numbers = len(text)
    seconds = numbers / 80 * 5
    response = 'Transcrição\n\n {}\n\n O texto tem {} caracteres \
e corresponde a um spot de {:.3f} segundos'.format(text, numbers, seconds)

    def end_app():
        sec_window.destroy()
        text_entry.delete("1.0", tk.END)
        mainWindow.destroy()

    def edit_text():
        sec_window.destroy()

    def new_text():
        sec_window.destroy()
        text_entry.delete("1.0", tk.END)
    sec_window = tk.Tk()
    response_widget = tk.Label(sec_window, text=response)
    response_widget.pack()
    ok_button = tk.Button(sec_window, text="FECHAR", command=end_app)
    ok_button.pack()
    edit_button = tk.Button(sec_window, text="EDITAR", command=edit_text)
    edit_button.pack()
    new_button = tk.Button(sec_window, text="NOVO", command=new_text)
    new_button.pack()
    sec_window.geometry("600x300")
    sec_window.title("Contador de Caracteres Para Spots Comerciais - PT/BR")
    sec_window.mainloop()


mainWindow = tk.Tk()

text_widget = tk.Label(mainWindow, text="Digite seu texto aqui:")
text_widget.pack()
text_entry = tk.Text(mainWindow, height=30, width=100)
text_entry.pack()
process_button = tk.Button(mainWindow, text="Processar", command=process)
process_button.pack()
clean_button = tk.Button(mainWindow, text="Limpar", command=clean)
clean_button.pack()
mainWindow.geometry("850x570")
mainWindow.title("Contador de Caracteres Para Spots Comerciais - PT/BR")
mainWindow.mainloop()
