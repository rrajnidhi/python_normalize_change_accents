#python program to find and replace every (comma), with point(.)

import os
import unidecode

directory='/home/nidhiraj/python/data'

def iterate_dir_and_replace():
    global directory
    no_of_files=0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename)) as file1:
                data=file1.read()
                replaced = data.replace(",", ".")
                no_of_files=no_of_files+1
                file1.close()
                with open(os.path.join(directory, filename),'w') as file2:
                    file2.write(replaced)
    print(no_of_files,"number of files in directory")



if __name__ == "__main__":
    iterate_dir_and_replace()
