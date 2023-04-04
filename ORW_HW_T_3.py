files = ["file_1.txt", "file_2.txt", "file_3.txt"]


def reading_writening_file():
    files = ["file_1.txt", "file_2.txt", "file_3.txt"]
    a = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            a.append(temp)
        a.sort(key=len)

    new_file = 'new_file.txt'
    with open(new_file, 'w', encoding='utf-8') as f:
        for lines in a:
            for i in lines:
                f.writelines(i + '\n')
    return


reading_writening_file()
