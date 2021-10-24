import os

def renamer():
    i = 0 #initiate/iterate over files lists
    path = 'C:\\Users\\USER\\Desktop\\img\\'
    for filename in os.listdir(path):
        names = f"image {i}.jpg"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1

if __name__ == "__main__":
    renamer()