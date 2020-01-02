import os
import time

class numPlace:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# sudoku puzzle in matrix form
'''
sudoku = [
[ 0, 0, 3, 0, 5, 8, 0, 0, 9, ],
[ 0, 0, 9, 7, 4, 0, 0, 6, 2, ],
[ 0, 0, 0, 2, 0, 0, 5, 3, 8, ],

[ 4, 0, 2, 0, 0, 0, 0, 1, 3, ],
[ 9, 0, 0, 3, 0, 4, 0, 8, 7, ],
[ 6, 0, 8, 0, 7, 0, 2, 5, 0, ],

[ 3, 0, 0, 0, 0, 5, 0, 2, 0, ],
[ 0, 0, 5, 0, 3, 7, 0, 9, 0, ],
[ 0, 1, 7, 0, 0, 0, 3, 4, 0, ]
]
'''
'''
sudoku = [
    [ 0, 9, 7, 6, 8, 0, 2, 4, 5, ],
    [ 0, 0, 8, 4, 0, 0, 0, 3, 0, ],
    [ 0, 4, 2, 9, 1, 0, 0, 0, 0, ],
    [ 0, 0, 5, 0, 0, 2, 0, 9, 7, ],
    [ 7, 0, 0, 0, 0, 0, 0, 0, 6, ],
    [ 0, 1, 9, 0, 0, 4, 5, 8, 0, ],
    [ 0, 0, 3, 2, 0, 6, 8, 0, 0, ],
    [ 0, 5, 1, 0, 0, 0, 7, 6, 0, ],
    [ 0, 0, 0, 0, 7, 1, 3, 5, 4, ]
]
'''
'''
sudoku = [
[ 0, 4, 0, 0, 0, 0, 8, 6, 5, ],
[ 6, 0, 0, 5, 8, 0, 3, 0, 0, ],
[ 3, 5, 0, 7, 4, 0, 0, 2, 0, ],
[ 0, 0, 5, 8, 1, 0, 2, 0, 0, ],
[ 0, 7, 0, 3, 9, 0, 5, 8, 0, ],
[ 9, 8, 1, 0, 6, 0, 7, 0, 3, ],
[ 0, 0, 0, 4, 7, 0, 0, 5, 0, ],
[ 0, 0, 7, 0, 5, 0, 0, 0, 2, ],
[ 0, 2, 4, 6, 3, 0, 0, 0, 0, ]
]
'''
sudoku = [
    [ 0, 0, 0, 4, 0, 0, 0, 0, 0, ],
    [ 0, 5, 0, 7, 0, 0, 0, 0, 9, ],
    [ 0, 0, 0, 9, 0, 8, 6, 0, 1, ],
    [ 9, 6, 4, 0, 0, 0, 0, 8, 0, ],
    [ 0, 0, 7, 0, 0, 0, 9, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 3, 1, 0, 0, 0, 2, 0, 0, 0, ],
    [ 0, 0, 0, 8, 0, 0, 0, 0, 7, ],
    [ 2, 0, 0, 0, 0, 0, 1, 0, 3, ]
]


# used for checking 3x3 boxes
section = {
    0:['00','01','02','10','11','12','20','21','22'],
    1:['03','04','05','13','14','15','23','24','25'],
    2:['06','07','08','16','17','18','26','27','28'],

    3:['30','31','32','40','41','42','50','51','52'],
    4:['33','34','35','43','44','45','53','54','55'],
    5:['36','37','38','46','47','48','56','57','58'],

    6:['60','61','62','70','71','72','80','81','82'],
    7:['63','64','65','73','74','75','83','84','85'],
    8:['66','67','68','76','77','78','86','87','88'],
}

# contains a row and col for each place that equals a 0
emptyPlaces = []

# prints the puzzle to the console
def printSudoku():
    os.system('clear')
    print (" -----------------------")
    for row in range(len(sudoku)):
        r = "| "
        if (row == 3 or row == 6):
            print (" -----------------------")
        for col in range(len(sudoku)):
            if (col == 3 or col == 6):
                r = r + "| "
            r = r + str(sudoku[row][col]) + " "
        r = r + "|"
        print(r)
    print (" -----------------------")
    print()
    time.sleep(.03)

# fills emptyPlaces list
def CollectEmptySpots():
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if (sudoku[row][col] == 0):
                x = numPlace(row,col)
                emptyPlaces.append(x)

# checks if the 3x3 is valid 
def checkThreeByThree(num, row, col):
    sectionNum = None
    rowcol = str(row) + str(col)
    for k,v in section.items():
        for i in v:
            if (i == rowcol):
                sectionNum = k
    for i in section[sectionNum]:
        if (sudoku[int(i[0])][int(i[1])] == num):
            return False

# checks if rows and colums add up correctly
def checkPlacement(num, row, col):
    # checks rows
    for i in sudoku[row]:
        if (i == num):
            return False
    # checks columns 
    for crow in range(len(sudoku)):
        if (sudoku[crow][col] == num):
            return False
    # checks 3x3's
    if (checkThreeByThree(num, row, col) == False):
        return False
    return True

# checks if the puzzle is solved
def Finished():
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if (sudoku[row][col] == 0):
                return False
    return True

# the recursion function 
def Start():
    for emptyPlace in emptyPlaces:
        if (Finished() == True):
            print ('finished')
            printSudoku()
            return True
        elif (sudoku[emptyPlace.row][emptyPlace.col] == 0):
            for i in range(1,10):
                if (checkPlacement(i, emptyPlace.row, emptyPlace.col) == True):
                    sudoku[emptyPlace.row][emptyPlace.col] = i
                    printSudoku()
                    if (Start() == True):
                        return True
                else:
                    sudoku[emptyPlace.row][emptyPlace.col] = i
                    printSudoku()
            sudoku[emptyPlace.row][emptyPlace.col] = 0
            return False



CollectEmptySpots()
Start()