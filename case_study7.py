
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

        a = text
        b = []
        for i in a:
            i = str(i)
            if i in b:
                continue
            else:
                b.append(i)
        diction = {}
        for e in b:
            diction[e] = []
        for t in diction:
            for q in a[0:-1]:
                if q == t:
                    w = a.index(q)
                    w += 1
                    k = a[w]
                    diction[t].append(k)
                    a.remove(q)

        number = int(input('Number of sentences generated: '))
        j = sorted(diction.keys())
        j_1 = j[-1]

        # d_1 = diction.pop(j_1)
        print(diction)

        for i in range(number):
            first_word = random.choice(start_words)
            f_l = diction[first_word]
            r = random.choice(f_l)
            print(first_word, end = ' ')
            le = 0
            qw = 1
            while qw < 19 and le == 0:
                key_word = r
                a_w_l = diction[key_word]
                add_word = random.choice(a_w_l)
                if key_word in stop_words:
                    if qw >= 5:
                        le = 1
                    if qw < 5:
                        while key_word in stop_words:
                            key_word = random.choice(j)
                            a_w_l = diction[key_word]
                            add_word = random.choice(a_w_l)
                if key_word in stop_words:
                    print(key_word, end=' ')
                else:
                    print(key_word, end=' ')
                qw += 1
                r = add_word
            if le == 0:
                last_word = random.choice(stop_words)
                print(last_word, end=' ')

except FileNotFoundError:
    print('File {} not found.'.format(file))