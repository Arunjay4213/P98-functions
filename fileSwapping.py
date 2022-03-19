def fileSwapData():
    file1 = input("enter the original file's contents: ")
    file2 = input("enter the contents of the file to be swapped: ")

    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()

        with open(file1, 'w+') as a:
            a.write(data_b)
        with open(file2, 'w+') as b:
            b.write(data_a)
fileSwapData()
print("The contents of the files have been swapped")