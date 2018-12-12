""" Case-study №7
Developers:
Zelenskaya A. , Zolotykh M. , Sherubneva A.
"""


import string, random
file = input('Enter name of file: ')
try:
    with open(file) as f_in:
        text = f_in.read()
        text = text.replace('\n',' ')
        for s in string.punctuation:
            if s != '.' and s != ',' and s != '!' and s != '?':
                text = text.replace(s,'')
            else:
                text = text
        text = text.replace(' !', '!')
        text = text.replace(' ?', '?')
        text = text.replace(' .','.')
        text = text.replace(' ,', ',')
        text = text.replace('...', '')
        text = text.replace('«', '')
        text = text.replace('»', '')
        text = text.split()
        letter = 'АЕЁИОУЫЭЮЯБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
        char = '.!?'
        start_words =[]
        stop_words = []
        for i in text:
            if i[-1] in char:
                i = i.replace(i[-1],'')
                if i[0] in letter:
                    start_words.append(i)
            else:
                if i[0] in letter:
                    start_words.append(i)
        for q in text:
            if q[-1] in char:
                stop_words.append(q)
        number = int(input('Number of sentences generated: '))
        for i in range(number):
            first_word = random.choice(start_words)
            last_word = random.choice(stop_words)

        # часть кода со словарем
        a = text
        b = []
        for i in a:
            i = str(i)
            if i in b:
                continue
            else:
                b.append(i)
        dict = {}
        for e in b:
            dict[e] = []
        print(dict)
        for t in dict:
            for q in a[0:-1]:
                if q == t:
                    w = a.index(q)
                    w += 1
                    k = a[w]
                    dict[t].append(k)
                    a.remove(q)
        print(dict)



except FileNotFoundError:
    print('File {} not found.'.format(file))