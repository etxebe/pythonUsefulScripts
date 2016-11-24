import argparse


# czyta zadany plik i zwraca liste danych z zadanej kolumny (bez dwoch pierwszych bo to naglowki)
def read_column(filename, column_number, sep, headerslines):
    file_pts = open(filename, 'r')
    columns = []
    for i, line in enumerate(file_pts):
        if i >= headerslines:
            columns.append(line.split(sep)[column_number-1])
    file_pts.close()
    return columns


# usuwa wszystkie '' z podanej listy
def remove_empty(arr):
    return [item for item in arr if item != '']


def compare_arrays(arr1, arr2):
    res = [x for x in arr2 if x not in arr1]
    return len(res)
    # res = set(arr1) & set(arr2)
    # if len(res) > 0:
    #     print(res)
    # else:
    #     return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks for not matched trades in two files in corresponding columns")
    parser.add_argument("filename_col3", help="the file with column no.3 to check")
    parser.add_argument("filename_col1", help="the file with column no.1 to check")
    parser.parse_args()
    args = parser.parse_args()

    # trzecia kolumna z pliku pts (args.filename_col3) i 1 kolumna (args.filename_col1)
    third_column = remove_empty(read_column(args.filename_col3, 3, "|", 2))
    first_column = remove_empty(read_column(args.filename_col1, 1, ",", 1))

    print("Liczba nie-zmatchowanych tradow:", compare_arrays(third_column, first_column))
