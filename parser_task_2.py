import re
import pandas as pd


# ---------------------------------------------------#
#        SOLUTION 1 WITH EXCESS PYTHON LOGICS       #
# ---------------------------------------------------#


def translator(line, code={' ': '', ',': '', '|': ';'}):
    line = line.lstrip('|').rstrip('|\n')
    return line.translate(str.maketrans(code))


def solution1():
    with open("forParsing_task.xls", "r") as f:
        messy_data = f.readlines()
        to_be_removed = messy_data[0:9]  # Extracting the unwanted rows

        # Cleaning the columns as per requirement.
        columns = re.sub(r'\s*\|\s*', ';', to_be_removed[-2].lstrip('|').rstrip('|\n').strip())

        # Iterating & cleaning the rows as per requirement.
        final_data = [columns] + [translator(line) for line in messy_data if line not in to_be_removed]

        # Transpose the Columns into rows
        df = pd.DataFrame([final_data]).T
        df.to_csv('cleaned_solution1.csv', index=False, header=False)


# ---------------------------------------------------#
#        SOLUTION 2 WITH PANDAS MANIPULATIONS       #
# ---------------------------------------------------#


def solution2():
    # Assign column names
    col_names = ['Stat', 'Account', 'No', 'Date', 'Net due dt', 'LC amnt', 'DD', 'CCAr', 'PayT', 'Type']
    tmp_name = ['tmp1'] + col_names + ['tmp2']

    data = pd.read_csv("forParsing_task.xls", names=tmp_name, skiprows=7, sep='|', skipinitialspace=True,
                       on_bad_lines='skip')
    data = data[col_names]

    # Skipintialspace failed to remove the spaces around 'Stat' column
    # so removed the spaces explicitly from 'Stat' columns
    data['Stat'] = data['Stat'].str.strip()

    # Remove rows which are headers of repeated data or dummy rows
    data = data[~((data.Stat == 'Stat') | (data.Stat.str.contains('----')) | (data.Stat.isna()))]

    # String manipulation to fix trailing '-', remove comma to convert into float
    data['LC amnt'] = data['LC amnt'].str.replace(',', '').apply(
        lambda x: ('-' + x[:len(x) - 1]) if x.endswith('-') else x).astype('float')

    data.to_csv("cleaned_solution2.csv", index=False, sep=';')


if __name__ == '__main__':
    solution2()  # preferred
    solution1()
