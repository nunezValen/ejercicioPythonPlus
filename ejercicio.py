import csv
read_dataset = 'Conectividad_Internet.csv'
write_dataset = 'Conectividad_Internet_proc.csv'

def check_connect(line_proc):
    types = ['ADSL','CABLEMODEM','DIALUP','FIBRAOPTICA','SATELITAL','WIRELESS',
            'TELEFONIAFIJA','3G','4G']
    if all(line_proc[column] == '--' for column in types):
        line_proc['posee_conectividad'] = 'NO'
    else:
        line_proc['posee_conectividad'] = 'SI'
    return line_proc

with open(read_dataset, mode = 'r', encoding = 'utf-8') as read_file:
    write_file = open(write_dataset, mode = 'w', encoding = 'utf-8')
    reader = csv.DictReader(read_file)

    fieldnames = reader.fieldnames + ['posee_conectividad']
    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    writer.writeheader()

    for line in reader:
        line = check_connect(line)
        writer.writerow(line)
write_file.close()