def ascii_decode(code):
    try:
        encode = ''
        slov = ['NOP', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', '\t', 'LF', 'VT', 'FF', '\n', 'SO', 'SI',
                'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS', 'RS',
                'US', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2',
                '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '[', "\ ", ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL', 'Ђ', 'Ѓ', '‚',
                'ѓ', '„', '…', '†', '‡', '€', '‰', 'Љ', '‹', 'Њ', 'Ќ', 'Ћ', 'Џ', 'ђ', '‘', '’', '“', '”', '•', '–', '—',
                ' ', '™', 'љ', '›', 'њ', 'ќ', 'ћ', 'џ', ' ', 'Ў', 'ў', 'Ћ', '¤', 'Ґ', '¦', '§', 'Ё', '©', 'Є', '«', '¬',
                ' ', '®', 'Ї', '°', '±', 'І', 'і', 'ґ', 'µ', '¶', '·', 'ё', '№', 'є', '»', 'ј', 'Ѕ', 'ѕ', 'ї', 'А', 'Б',
                'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц',
                'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л',
                'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        ascii_dict = dict()
        for i in range(256):
            ascii_dict[i] = slov[i]

        for i in map(int, code):
            encode += ascii_dict[i]

        return encode + "1"

    except Exception:
        return "error"


def funk(n):
    return sum([i for i in range(1, n)])


def read(spisok, koef=0):
    stroka = spisok[0][0]
    flag = True
    for i in range(0, len(spisok[0]) - 1 - koef):
        if flag:
            perem = i + 1
            for x in range(0, i + 2):
                stroka += spisok[x][perem]
                perem -= 1
            flag = not flag
        else:
            perem = i + 1
            for x in range(0, i + 2):
                stroka += spisok[perem][x]
                perem -= 1
            flag = not flag
    return stroka


def sibirsky(simbols):
    try:
        simbols = list(simbols)
        len_side_pyramid = 1

        while funk(len_side_pyramid) < len(simbols):
            len_side_pyramid += 1
        pyromid = []

        if funk(len_side_pyramid) == len(simbols):
            len_side_pyramid -= 1
            flag = 0

            j = len_side_pyramid + 0
            for i in range(len_side_pyramid):
                pyromid.append(simbols[flag:flag + j])
                flag += j
                j -= 1

            return read(pyromid) + '1'

        elif (len_side_pyramid - 1) % 2 == 1:
            len_side_pyramid -= 1
            flag = 0
            how_many = abs(len_side_pyramid - (len(simbols) - funk(len_side_pyramid)))
            backup_how_many = how_many + 0

            p = True
            vremen_perem = len_side_pyramid - 1
            for i in range(len_side_pyramid):
                if how_many > 0:
                    pyromid.append(simbols[flag:flag + vremen_perem])
                    how_many -= 1
                elif p:
                    p = False
                    vremen_perem += 1
                    pyromid.append(simbols[flag:flag + vremen_perem])
                else:
                    pyromid.append(simbols[flag:flag + vremen_perem])
                flag += vremen_perem
                vremen_perem -= 1

            stroka = read(pyromid)
            perem = len(pyromid[0])
            for i in range(0, len_side_pyramid - backup_how_many):
                stroka += pyromid[perem][i]
                perem -= 1

            return stroka + '1'

        elif (len_side_pyramid - 1) % 2 == 0:
            len_side_pyramid -= 1
            flag = 0
            how_many = (len(simbols) - funk(len_side_pyramid))
            backup_how_many = how_many + 0

            p = True
            for i in range(len_side_pyramid - 1):
                if how_many > 0:
                    how_many -= 1
                    pyromid.append(simbols[flag:flag + len_side_pyramid])
                elif p:
                    p = not p
                    len_side_pyramid -= 1
                    pyromid.append(simbols[flag:flag + len_side_pyramid])
                else:
                    pyromid.append(simbols[flag:flag + len_side_pyramid])
                flag += len_side_pyramid
                len_side_pyramid -= 1

            stroka = read(pyromid, 1)
            perem = len(pyromid[0]) - 1
            for i in range(backup_how_many):
                stroka += pyromid[i][perem]
                perem -= 1

            return stroka + '1'

    except Exception:
        return "error"


def xeming_decoder(code):
    try:
        tmp = [int(i, 2) for i in code]
        encode = []
        for i in code:
            encode.append(str(i)[2:3] + str(i)[4:7] + str(i)[8:])
        return ' '.join(encode)

    except Exception:
        return "error"


def get_interval(simbols):
    kol = 0
    while simbols[0] != '1':
        simbols = simbols[1:]
        kol += 1

    return kol


def elias_decoder(stroka):
    try:
        leading_unit = stroka[0]
        if leading_unit == '1':
            flag = True
        else:
            flag = False

        stroka = stroka[1:]
        elements = []

        while stroka:
            kol_leading_zero = get_interval(list(stroka))
            elements.append(stroka[:kol_leading_zero * 2 + 1])
            stroka = stroka[kol_leading_zero * 2 + 1:]

        int_elements = []
        for elem in elements:
            if flag:
                int_elements.append(''.join(['1' for i in range(int(elem, 2))]))
                flag = not flag
            else:
                int_elements.append(''.join(['0' for i in range(int(elem, 2))]))
                flag = not flag

        final_stroka = ''.join(int_elements)
        final_stroka = final_stroka[get_interval(str(final_stroka)):]
        delen_stroka = []
        if len(final_stroka) != len(final_stroka) // 8 * 8:
            for i in range(len(final_stroka) // 8 + 1):
                delen_stroka.append(final_stroka[:8])
                final_stroka = final_stroka[8:]
        else:
            for i in range(len(final_stroka) // 8):
                delen_stroka.append(final_stroka[:8])
                final_stroka = final_stroka[8:]

        return " ".join(delen_stroka)

    except Exception:
        return "error"