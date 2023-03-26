a = []
with open('file_1.txt', encoding='utf-8') as f_1, open('file_2.txt', encoding='utf-8') as f_2, \
        open('file_3.txt', encoding='utf-8') as f_3:
    a.append(f_1)
    a.append(f_2)
    a.append(f_3)
    for f in a:
        new_file = {}
        f_ = {f: (len(f.readlines()), f.read())}
        new_file.update(f_)
        print(new_file)
