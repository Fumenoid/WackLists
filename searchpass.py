import mmap

def checkpass(password):
    with open('./WackLists.txt', 'rb', 0) as file, \
         mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(bytes(password, 'utf-8')) != -1:
            return True
        else:
            return False