from os import chdir
chdir("/Users/maximin/Desktop/Euler/linked_files/")

with open("p096_sudoku.txt", 'r') as f:

    count = 1
    for i in f:
        if i[0] == "G":
            print()
            print(count)
            count += 1
        else:
            for nb in i[:-1]:
                if nb != "0":
                    print(nb, end="")
                else:
                    print("_", end="")
            print()
