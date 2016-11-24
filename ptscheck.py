import argparse


# czyta zadany plik i zwraca liste danych z zadanej kolumny (bez dwoch pierwszych bo to naglowki)
def read_column(filename, column_number):
    file_pts = open(filename, 'r')
    columns = []
    for i, line in enumerate(file_pts):
        if i >= 2:
            columns.append(line.split('|')[column_number-1])
    file_pts.close()
    return columns


# sprawdza czy w danej tabeli jest jakiś item równy ''
def check_empty(arr):
    for item in arr:
        if item == '':
            return True
    return False


# usuwa wszystkie '' z podanej listy
def remove_empty(arr):
    return [item for item in arr if item != '']


# sprawdza czy sa powtorzenia w danej tabeli
def are_repeats(arr):
    if check_empty(arr):
        res = remove_empty(arr)
    else:
        res = arr
    check = [item for item in res if res.count(item)>1]
    if len(check) > 0:
        return set(check)
    else:
        return False


# zwraca True lub False w zaleznosci czy w ktorejs z kolumn znalezieno zduplikowane rekordy
def return_results(filename, columns_arr):
    flag = True
    for col in columns_arr:
        col_repeats = are_repeats(read_column(filename, col))
        # print(col_repeats)
        if col_repeats:
            print("W kolumnie", col, "sa zduplikowane rekordy:", col_repeats)
            flag = False
    if flag:
        print("Brak zduplikowanych rekordow w kolumnach: ", columns_arr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks whether are duplicated values in column 3 and 8")
    parser.add_argument("filename", help="the file you want to check")
    parser.parse_args()
    args = parser.parse_args()
    return_results(args.filename, [3, 8])

