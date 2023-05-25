while True:
    text1 = input('Cole seu texto:\n')
    digitos = {'/': True, '(': True, ')': True, '_': True, ':': True, ';': True, '|': True, '[': True,
               ']': True, '{': True, '}': True, '+': True, '=': True, '!': True, '?': True,
               '-': True, '\t': True, '"': True, "'": True, "”": True, '“': True, '\n': True}
    text = ""
    for caractere in text1:
        if caractere not in digitos:
            text += caractere

    try:
        if text[text.index('@') + 1].isascii():
            text = text.replace('@', ' arroba ')
    except ValueError:
        text += ''
    try:
        if 0 < text.index('&') < len(text) - 1 and text[text.index('&') - 1].isascii() and text[text.index('&') + 1].isascii():
            text = text.replace('&', ' e ')
    except ValueError:
        text += ''
    try:
        if 0 < text.index('$') < len(text) - 1 and text[text.index('$') - 1] == 'R' and text[text.index('$') + 1].isalnum():
            text = text.replace('R$', 'reais ')
        else:
            text = text.replace('R$', '')
    except ValueError:
        text += ''
    try:
        if 0 < text.index(',') < len(text) - 1 and text[text.index(',') - 1].isnumeric() and text[text.index(',') + 1].isnumeric():
            text = text.replace(',', ' e ')
        elif 0 < text.index(',') < len(text) - 1 and text[text.index(',') - 1].isalpha() and text[text.index(',') + 1] == ' ':
            text = text.replace(',', ' ')
    except ValueError:
        text += ''
    try:
        if text.endswith('.'):
            text = text.rstrip('.')
    except ValueError:
        text += ''
    try:
        if 0 < text.index('.') < len(text) - 1 and text[text.index('.') - 1].isalnum() and text[text.index('.') + 1].isalnum():
            text = text.replace('.', ' ponto ')
    except ValueError:
        text = text.replace('.', ' ')
    try:
        if 0 < text.index('.') < len(text) - 1 and text[text.index('.') - 1].isascii() and text[text.index('.') + 1] == ' ':
            text = text.replace('.', ' ')
    except ValueError:
        text = text.replace('.', ' ')

    spot_comercial = ''
    t = text.split()
    for ext in t:

        if ext.isnumeric():
            unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
            dezenas = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                       'dezenove']
            dezenas2 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
            centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
                        'oitocentos', 'novecentos']


            def numero_por_extenso(ext):
                e = int(ext)
                if e == 0:
                    return unidades[e]
                if e < 0 or e > 999999:
                    return "Número inválido"

                extenso = ""

                if e == 9000:
                    extenso += 'nove mil'
                    e %= 1000

                if e == 8000:
                    extenso += 'oito mil'
                    e %= 1000

                if e == 7000:
                    extenso += 'sete mil'
                    e %= 1000

                if e == 6000:
                    extenso += 'seis mil'
                    e %= 1000

                if e == 5000:
                    extenso += 'cinco mil'
                    e %= 1000

                if e == 4000:
                    extenso += 'quatro mil'
                    e %= 1000

                if e == 3000:
                    extenso += 'três mil'
                    e %= 1000

                if e == 2000:
                    extenso += 'dois mil'
                    e %= 1000

                if e == 1000:
                    extenso += 'mil'
                    e %= 1000

                if e > 2000:
                    extenso += numero_por_extenso(e // 1000) + " mil e "
                    e %= 1000
                if e > 1000:
                    extenso += " mil e "
                    e %= 1000

                if e == 900:
                    extenso += "novecentos "
                    e %= 100
                if e == 800:
                    extenso += "oitocentos "
                    e %= 100
                if e == 700:
                    extenso += "setecentos"
                    e %= 100
                if e == 600:
                    extenso += "seiscentos "
                    e %= 100
                if e == 500:
                    extenso += "quinhentos"
                    e %= 100
                if e == 400:
                    extenso += "quatrocentos"
                    e %= 100
                if e == 300:
                    extenso += "trezentos"
                    e %= 100
                if e == 200:
                    extenso += "duzentos "
                    e %= 100
                if e == 100:
                    extenso += "cem "
                    e %= 100
                if e > 100:
                    extenso += centenas[e // 100 - 1] + " e "
                    e %= 100

                if e == 90:
                    extenso += 'noventa'
                    e %= 10
                if e == 80:
                    extenso += 'oitenta'
                    e %= 10
                if e == 70:
                    extenso += 'setenta'
                    e %= 10
                if e == 60:
                    extenso += 'sessenta'
                    e %= 10
                if e == 50:
                    extenso += 'cinquenta'
                    e %= 10
                if e == 40:
                    extenso += 'quarenta'
                    e %= 10
                if e == 30:
                    extenso += 'trinta'
                    e %= 10
                if e == 20:
                    extenso += 'vinte'
                    e %= 10

                if e >= 10:
                    if e < 20:
                        extenso += dezenas[e - 10] + " "
                        e = 0
                    else:
                        extenso += dezenas2[e // 10 - 2] + " e "
                        e %= 10

                if e > 0:
                    extenso += unidades[e] + " "

                return extenso.strip()
            extense = ext.replace(ext, numero_por_extenso(ext))
            spot_comercial += extense
        elif ext.isalpha():
            spot_comercial += ext
        elif ext == '%':
            spot_comercial += 'por cento'
        elif ext == '4x4' or ext == '4X4':
            spot_comercial +='quatro por quatro'
        else:
            break
    print(spot_comercial)


#    numbers = len(spot_comercial)
#
#    if numbers == 0:
#        print(f'Digite novamente.')
#    elif numbers <= 72:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 5 segundos.')
#    elif numbers <= 144:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 10 segundos.')
#    elif numbers <= 216:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 15 segundos.')
#    elif numbers <= 288:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 20 segundos.')
#    elif numbers <= 432:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 30 segundos.')
#    elif numbers <= 648:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 45 segundos.')
#    elif numbers <= 864:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de até 60 segundos.')
#    elif numbers >= 864:
#        print(f'O texto tem {numbers} caracteres e corresponde a um spot de mais de 60 segundos.')
#    else:
#        print(f'Digite novamente.')

    continuar = input('Deseja Contar Novamente? S/N')
    if continuar == 'S' or continuar == 's':
        continue

    break
