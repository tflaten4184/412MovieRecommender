import csv
import string

charsToRemove = ".'?\":;-,–()"

infileName = "netflix_titles_nov_2019.csv"

# read csv file
with open(infileName, encoding='utf-8') as infile:
    csv_reader = csv.reader(infile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            original = row[10]
            result = original
            for char in charsToRemove:
                result = result.lower().replace(char, "")
            print("description: ", result)
            line_count += 1
    print(f'Processed {line_count} lines.')

def remove_punctuation(str):

    charsToRemove = ".'?\":;-,–()"

    str = row[10]
    result = str
    for char in charsToRemove:
        result = result.lower().replace(char, "")
    print("description: ", result)
    line_count += 1

    return result




# save output as csv file, as "netflix-cleaned.csv" ?
