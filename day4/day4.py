import re

xmas_length = 4
XMAS = "XMAS"
SAMX = "SAMX"

def search_xmas_revert(string):
    occurrences = re.findall(SAMX, string)
    return len(occurrences)

def search_xmas(string):
    occurrences = re.findall(XMAS, string)
    return len(occurrences)

def extract_columns(data_splitted):
    extracted_column = ""
    column_list = []
    index_line = 0

    for column in range(0, line_width):
        for line in data_splitted:
            extracted_column = extracted_column + line[column]
            index_line += 1
        column_list.append(extracted_column)
        extracted_column = ""
    return column_list

def extract_diagonal(data_splitted):
    extracted_diagonal = ""
    column = column_width
    current_line = 0


    for index_column in reversed(range(column_width)):
        target_diag_pos = line_width - current_line

        for index_line in reversed(range(target_diag_pos, line_width)):
            print(f"{index_column}-{index_line}")


        current_line +=1
        print(target_diag_pos)

    pass
    # for line in reversed(range(line_width)):
        # extracted_diagonal = extracted_diagonal + data_splitted[line][column]
        # column -= 1
        # print(extracted_diagonal)
        # extracted_diagonal = ""



if __name__ == '__main__':

    f = open("day4/example", "r")
    data = f.read()
    data_line_splitted = data.splitlines()
    line_width = len(data_line_splitted[0])
    xmas_count = 0
    data_column_splitted = extract_columns(data_line_splitted)
    column_width = len(data_column_splitted[0])

    extract_diagonal(data_line_splitted)

    for line in data_line_splitted:
        xmas_count = xmas_count + search_xmas(line)
        xmas_count = xmas_count + search_xmas_revert(line)

    for column in data_column_splitted:
        xmas_count = xmas_count + search_xmas(column)
        xmas_count = xmas_count + search_xmas_revert(column)

    pass
