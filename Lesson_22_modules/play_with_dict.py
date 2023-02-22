dic = {'a': 'x', 'b': 'y'}
new_dic = {}

for key, value in dic.items():
    new_dic[value] = key
dic = new_dic
print(dic)