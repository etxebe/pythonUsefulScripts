import argparse


def read_column(filename, column_number):
    """
    Returns the column values separated by | sign (without first two rows - they are headlines).
    :param filename: the path to file to read
    :param column_number: number of column
    :return: column values
    """
    file_pts = open(filename, 'r')
    columns = []
    for i, line in enumerate(file_pts):
        if i >= 2:
            columns.append(line.split('|')[column_number-1])
    file_pts.close()
    return columns


def check_empty(arr):
    """
    Checks if they are some empty ('') items in an array.
    :param arr: an array to check
    :return: true if they are some empty item, false if not
    """
    for item in arr:
        if item == '':
            return True
    return False


def remove_empty(arr):
    """
    Removes empty (=='') items from an array.
    :param arr: an array of which we want to remove empty items
    :return: a new array without empty items
    """
    return [item for item in arr if item != '']


def are_repeats(arr):
    """
    Checks if they are repetitions in given array.
    :param arr: an array we want to check
    :return: False if they are NOT repetitions and a set if they are
    """
    if check_empty(arr):
        res = remove_empty(arr)
    else:
        res = arr
    check = [item for item in res if res.count(item)>1]
    if len(check) > 0:
        return set(check)
    else:
        return False


def return_results(filename, columns_arr):
    """
    Final function. Prints the final result of checking.
    :param filename: filename to check
    :param columns_arr: an array of columns to check
    """
    flag = True
    for col in columns_arr:
        col_repeats = are_repeats(read_column(filename, col))
        if col_repeats:
            print("W kolumnie", col, "sa zduplikowane rekordy:", col_repeats)
            flag = False
    if flag:
        print("Brak zduplikowanych rekordow w kolumnach: ", columns_arr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks whether are duplicated values in column 3 and 8 (separately")
    parser.add_argument("filename", help="the file you want to check")
    parser.parse_args()
    args = parser.parse_args()
    return_results(args.filename, [3, 8])

