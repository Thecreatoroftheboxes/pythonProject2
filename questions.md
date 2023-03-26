В подсказке было предложено получить список файлов из каталога.
В инете нашла для этого способ:
https://translated.turbopages.org/proxy_u/en-ru.ru.2eccebdb-642014e9-d24746f6-74722d776562/https/www.geeksforgeeks.org/python-list-files-in-a-directory/
import os
print("Python Program to print list the files in a directory.")
 
Direc = input(r"Enter the path of the folder: ") # в примере до этого был путь вида: path = "C://Users//Vanshi//Desktop//gfg"  Но, если применить такой вид и отправить в ГИТ, то при проверке задания не будет ли помехой то, что компы, юзеры называются по-разному?
print(f"Files in the directory: {Direc}")
 
files = os.listdir(Direc)
files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.  # тут не поняла почему делается +'/'+f, наклон слеша здесь и в переменной path имеет значение?
print(*files, sep="\n")

Далее для отбора только файлов с расширением .txt предлагается следующее:
for x in os.listdir():
    if x.endswith(".txt"):
        # Prints only text file present in My Folder
        print(x)

В подсказке говорилось, что можно сделать отбор еще при загрузке списка файлов. Для этого можно было сделать так:
files = [f for f in files if os.path.isfile(Direc+'/'+.txt)]  # так?
