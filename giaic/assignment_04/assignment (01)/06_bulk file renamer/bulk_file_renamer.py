import os

def main():
    i = 0
    path = input("C:/Users/qasim/OneDrive/Desktop/Python_Projects/assignment (01)/bulk file renamer")
    for file in os.listdir(path):
        my_dest = "image" + str(i) + ".jpg"
        my_source = path + "/" + file  # The file name
        my_dest = path + "/" + my_dest
        os.rename(my_source, my_dest)
        i += 1
    print("All files renamed successfully!")

    if __name__ == "__main__":
        main()

