import csv
read_dataset = 'Conectividad_Internet.csv'
write_dataset = 'Conectividad_Internet_proc.csv'

def check_connect(line_proc):
    if line_proc['FIBRAOPTICA'] == '--':
        line_proc['posee_conectividad'] = 'NO'
    else:
        line_proc['posee_conectividad'] = 'SI'
    return line_proc

# Utilizo try except para evitar el corte del programa en caso de problemas
try :
    with open(read_dataset, mode='r', encoding='utf-8') as read_file:
        write_file = open(write_dataset, mode='w', encoding='utf-8')
        reader = csv.DictReader(read_file)
        # Reader de tipo csv.DictReader
        print(type(reader))
        fieldnames = reader.fieldnames + ['posee_conectividad']
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        writer.writeheader()

        for line in reader:
            line = check_connect(line)
            writer.writerow(line)
    write_file.close()

# Si el archivo no  se encontro   
except FileNotFoundError:
    print('El archivo no fue encontrado')
# Si hay problema con el formato
except csv.Error:
    print('Problema con el formato csv del archivo')
else: 
  print('Todo se ejecuto correctamente')
