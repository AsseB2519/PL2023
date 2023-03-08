import json
import csv
import os

def ex1(filename):
    with open(filename, 'r') as f:
        linhas = f.readlines()

    cabeca = linhas[0] # guardar header
    linhas.pop(0) # eliminar header
    if "{" not in cabeca:
        colunas = cabeca.split(",")
        colunas[-1] = colunas[-1].rstrip("\n")

        final = []

        for linha in linhas:
            cols = linha.split(",")
            cols[-1] = cols[-1].rstrip("\n")
            tmp = {} # create a new dictionary in every iteration
            ii = 0
            for i in colunas:
                tmp[i] = cols[ii]
                ii += 1
            final.append(tmp)

        y = json.dumps(final, indent=4, ensure_ascii=False) # ensure_ascii=False to correctly handle non-ascii characters

        output_filename = filename.split(".")[0] + ".json"
        with open(output_filename, 'w', encoding='utf-8') as j: # specify encoding to correctly handle non-ascii characters
            j.write(y)

    print(f"Conversion completed. Check {output_filename} for the result.")

def ex2(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        # Extract header
        header = next(reader)

        # Initialize empty list to store records
        records = []

        # Loop through remaining rows
        for row in reader:
            record = {}
            for i, value in enumerate(row):
                # Check if current column corresponds to "Notas" field
                if header[i] == "Notas{5}":
                    notas = []
                    for j in range(i, i + 5):
                        notas.append(int(row[j]))
                    record["Notas"] = notas
                # Skip empty columns
                elif value:
                    record[header[i]] = value
            records.append(record)

    # Rename "Numero" to "Número"
    for record in records:
        if "Numero" in record:
            record["Número"] = record.pop("Numero")

    # Write records to output file
    output_filename = os.path.splitext(filename)[0] + ".json"
    with open(output_filename, 'w', encoding='utf-8') as j:
        json.dump(records, j, ensure_ascii=False, indent=4)

    print("Conversion completed. Check " + output_filename + " for the result.")

def main():
    while True:
        print("Which file do you want to open? Enter 'exit' to quit.")
        filename = input("> ")
        if filename == 'exit':
            print("Exiting the program.")
            break

        with open(filename, 'r') as f:
            header = f.readline()

        if "{" in header:
            ex2(filename)
        else:
            ex1(filename)

if __name__ == "__main__":
    main()
