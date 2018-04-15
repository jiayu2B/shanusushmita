import Homework1
from math import log
dic = {}
arr_str = []
filename = 'VLOG'
for i in range(1,443):
    file_name = filename + str(i) + '.txt'
    try:
        _str = Homework1.text_process(file_name)
        ##print( file_name, 'process success')
        arr = _str.split(' ')
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        arr_str.append(arr)
    except FileNotFoundError:
        print(file_name, 'not found')
dic.pop('')
arr_ind = []
key_dic = list(dic.keys())
value_dic = list(dic.values())
for i in range(30):
    tem_max = max(value_dic)
    tem_ind = value_dic.index(tem_max)
    arr_ind.append(key_dic[tem_ind])
    value_dic[tem_ind] = 0
sum_num = 0
for i in dic:
    sum_num += dic[i]
TF = []
for i in range(len(arr_ind)):
    TF.append(dic[arr_ind[i]]/sum_num)
DF = []
for i in arr_ind:
    _sum = 0
    for j in range(len(arr_str)):
        if i in arr_str[j]:
            _sum+=1
    DF.append(_sum)
IDF = []
for i in DF:
    tem = 404/(i + 1)
    IDF.append(log(tem,10))
TF_IDF = []
for i in range(len(TF)):
    TF_IDF.append(TF[i]*IDF[i])
print('The total words number is', sum_num)
print("The unique words number is", len(value_dic))
print("The number of words occurs ones", value_dic.count(1))
print("The average number of words per document is", sum_num/404)
print("The most frequect 30 words:", arr_ind)
print("TF is", TF)
print('IDF is', IDF)
print("TF * IDF is", TF_IDF)
