#python program to count a particular character in a file

import os
import unidecode

directory='/sample/directory'

def iterate_dir_and_count():
    global directory
    no_of_files=0
    count_of_dot=0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename)) as file1:
                for line in file1:
                    words=line.split()
                    for i in words:
                        for letter in i:
                            if(letter=='.'):
                                count_of_dot=count_of_dot+1
                               

                no_of_files=no_of_files+1
                file1.close()
    print(no_of_files,"number of files in directory")
    print(count_of_dot)

if __name__ == "__main__":
    iterate_dir_and_count()
