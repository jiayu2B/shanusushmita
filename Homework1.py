from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
def remove_char(file):
    res = ''
    for i in file:

        if ord(i) <= 122 and ord(i) >= 65 or ord(i) == 32:
            res += i
    return res

def remove_space(_str):
    res = ''
    for i in range(len(_str)-1):
        if _str[i] != ' ':
            res += _str[i]
        elif _str[i] == ' ' and _str[i+1] != ' ':
            res += _str[i]
    return res + _str[-1]

def upper_to_lower(_str):
    res = ''
    for i in _str:
        if i == ' ':
            res += i
        elif ord(i) < 97:
            res += chr(ord(i)+32)
        else:
            res += i
    return res

def remove_stopwords(_str):
    res = ''
    arr = _str.split(' ')
    f = open('stopwords.txt')
    stopword = f.read().split('\n')
    for i in arr:
        if i not in stopword:
            res = res + i + ' ' 
    return res

def stemming(_str):
    res = ''
    arr = _str.split(' ')
    for i in range(len(arr)):
        arr[i] = porter_stemmer.stem(arr[i])
    for i in arr:
        res = res + i + ' '
    return res

def text_process(file):
    f = open(file, errors = 'ignore')
    _str = remove_char(f.read())
    _str = remove_space(_str)
    _str = upper_to_lower(_str)
    _str = remove_stopwords(_str)
    _str = stemming(_str)
    return _str
