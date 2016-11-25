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


def get_additional_info(not_matched_items, items_notin_third, third_col2, third_col6):
    """
    Gets additional info from a third file (sixth column) for not matched trades but present in third file.
    :param not_matched_items: an array with not matched trades
    :param items_notin_third: an array with not matched trades and not present in third file
    :param third_col2: a second column from third file
    :param third_col6: a sixth column from third file
    :return: an array with additional info (third_col6) without repetitions
    """
    res = {}
    for item in not_matched_items:
        if item not in items_notin_third:
            idx = third_col2.index(item)
            if third_col6[idx].rstrip() not in res.values():
                res[item] = third_col6[idx].rstrip()
    return res


def present_additional_info(dict_items):
    """
    Gets values from a dictionary and put them in a new table.
    :param dict_items: dictionary variable
    :return: an array with dictionary values
    """
    values = []
    for key in dict_items:
        values.append(dict_items[key])
    return values

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checks for not matched trades in two files in corresponding columns")
    parser.add_argument("filename_col1", help="the file with column no.1 to check")
    parser.add_argument("filename_col3", help="the file with column no.3 to check")
    parser.add_argument("filename_third_col2", help="the third file with column no. 2 to check")
    parser.parse_args()
    args = parser.parse_args()

    # third column from file (args.filename_col3) and first column from frile (args.filename_col1)
    first_column = remove_empty(read_column(args.filename_col1, 1, ",", 1))
    third_column = remove_empty(read_column(args.filename_col3, 3, "|", 2))
    third_file_column2 = remove_empty(read_column(args.filename_third_col2, 2, "|", 3))
    third_file_column6 = remove_empty(read_column(args.filename_third_col2, 6, "|", 3))

    # comparing the first and second file
    items_num, items = compare_arrays(first_column, third_column)

    # print("Number of not matched trades between first two files:", items_num)
    print("Not matched trades between first two files:", items)

    # comparing with the third file
    # all not matched trades (items) should be in third file (in second column)
    items_not_in_third = compare_arrays(third_file_column2, items)
    print("Not matched trades not in third file:", items_not_in_third[1])

    additional_info = get_additional_info(items, items_not_in_third[1], third_file_column2, third_file_column6)
    print("Additional info for not matched trades but present in third file:", present_additional_info(additional_info))
