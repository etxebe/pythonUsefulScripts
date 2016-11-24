import argparse


def read_column(filename, column_number, sep, headerslines):
    """
    Returns the specified column values from file without headlines.
    :param filename: file to read columns from
    :param column_number: number of column to read
    :param sep: separator used in file
    :param headerslines: number of headlines in file
    :return: column values as an array
    """
    file_pts = open(filename, 'r')
    columns = []
    for i, line in enumerate(file_pts):
        if i >= headerslines:
            columns.append(line.split(sep)[column_number-1])
    file_pts.close()
    return columns


def remove_empty(arr):
    """
    Removes all empty ('') items from an array.
    :param arr: an array we want to remove empty items from
    :return: a new array without empty items
    """
    return [item for item in arr if item != '']


def compare_arrays(arr1, arr2):
    """
    Compares items from arr2 with items from arr1. If not present returns them.
    :param arr1: a first array
    :param arr2: a second array
    :return: a new array with items from arr2 that are not present in arr1, numbers of such items
    """
    res = [x for x in arr2 if x not in arr1]
    return len(res), res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks for not matched trades in two files in corresponding columns")
    parser.add_argument("filename_col3", help="the file with column no.3 to check")
    parser.add_argument("filename_col1", help="the file with column no.1 to check")
    parser.parse_args()
    args = parser.parse_args()

    # third column from file (args.filename_col3) and first column from frile (args.filename_col1)
    third_column = remove_empty(read_column(args.filename_col3, 3, "|", 2))
    first_column = remove_empty(read_column(args.filename_col1, 1, ",", 1))

    items_num, items = compare_arrays(third_column, first_column)

    print("Number of not matched trades:", items_num)
    print("Not matched trades:", items)
