import os, time
from pathlib import Path

def file_age(filepath):
    #float((time.time() - os.path.getmtime(filepath)) / 60 / 60)
    st = os.stat(str(filepath))
    mtime = st.st_mtime
    print(mtime)
    return (time.time() - mtime) / 60 / 60


# default age is two months
def cleanup(age = 60 * 24):
    pwd = str(os.getcwd())

    for file_path in Path(pwd).glob('*_start.txt'):
        print(file_path)
        print(file_age(file_path))
        if file_age(file_path) > age:
            print("removing", file_path)
           # os.remove(file_path)

if __name__ == '__main__':  
    cleanup()
    print()
