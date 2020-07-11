import csv
import sys


def readfile(filename):
    rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
    return rows

def insert_ampersand_between_columns(rows):
    ampersand_rows = []
    for row in rows:
        ampersand_row = []
        for element in row:
            if element is not row[len(row) - 1]:
                ampersand_element = ' ' + str(element) + ' ' + '&'
                ampersand_row.append(ampersand_element)
            else:
                backslash_element = ' ' + str(element) + ' ' + '\\'
                ampersand_row.append(backslash_element)
        ampersand_rows.append(ampersand_row)
    return ampersand_rows

def writefile(rows):
    filename = 'output.txt'
    original_stdout = sys.stdout
    with open(filename,'w') as file_object:
        sys.stdout = file_object
        for row in rows:
            for element in row:
                print(element, end='')
            print('\\')
    sys.stdout = original_stdout

def convert_to_latex_row(filename):
    rows = readfile(filename)
    rows = insert_ampersand_between_columns(rows)
    writefile(rows)

def main():
    filename = "ResultsSynthetic.csv"
    convert_to_latex_row(filename)

if __name__ == "__main__":
    main()
