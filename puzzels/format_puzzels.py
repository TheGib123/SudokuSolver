import pandas as pd
import csv

df = pd.read_csv('puzzels.csv')

def write_puzzle(sudoku, file_name):
    with open(file_name, 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(sudoku)
        print('created ' + file_name)

def format_puzzle(puzzle):
    sudoku = []
    sudoku_row = []

    for i in puzzle:
        if (i == '.'):
            sudoku_row.append('0')
        else:
            sudoku_row.append(i)
        
        if (len(sudoku_row) == 9):
            sudoku.append(sudoku_row)
            sudoku_row = []

    return sudoku

def output_puzzle(difficulty):
    tempdf = df[df['Difficulty'] == difficulty].reset_index()
    for index, row in tempdf.iterrows():
        sudoku = format_puzzle(row['Puzzle'])
        file_name = str(row['Difficulty']) + '-' + str(index+1) + '.csv'
        write_puzzle(sudoku, file_name)

if (__name__ == "__main__"):
    print('Type in puzzle difficulty exactly as listed below')
    print('Simple')
    print('Easy')
    print('Intermediate')
    print('Expert')
    print('')
    ans = input()
    output_puzzle(ans)