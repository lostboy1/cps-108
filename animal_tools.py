import csv

def load():
    return csv.reader(open('Data/state-animals.csv'))

def field_equals(field, value, rows):
    matches = []
    for row in rows:
        if row[field] == value:
            matches.append(row)
    return matches

def field_endswith(field, value, rows):
    matches = []
    for row in rows:
        if row[field].endswith(value):
            matches.append(row)
    return matches

def print_field(i, rows):
    for row in rows:
        print(row[i])
