import json

def read_file_and_convert_to_json(filename):
    with open(filename, 'r') as f:
        linhas = f.readlines()

    cabeca = linhas[0] # guardar header
    linhas.pop(0) # eliminar header
    if "{" not in cabeca:
        colunas = cabeca.split(",")
        colunas[-1] = colunas[-1].rstrip("\n")

        final = []
        tmp = {}

        for linha in linhas:
            cols = linha.split(",")
            cols[-1] = cols[-1].rstrip("\n")
            ii = 0
            for i in colunas:
                tmp[i] = cols[ii]
                ii += 1
            final.append(tmp)

        y = json.dumps(final, indent=4)

        with open('output.json', 'w') as j:
            j.write(y)

    print("Conversion completed. Check output.json for the result.")

def convert_csv_to_json(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    header = lines[0].split(',')
    for i in range(len(header)):
        if '{' in header[i]:
            n_cols = int(header[i].split('{')[1].split('}')[0])
            header[i] = header[i].split('{')[0]
            for j in range(n_cols - 1):
                header.insert(i+1, '')

    header = [h.strip() for h in header]
    lines = [l.strip().split(',') for l in lines[1:]]

    data = []
    for line in lines:
        item = {}
        start = 0
        for i in range(len(header)):
            if i < len(header)-1 and not header[i+1]:
                end = start + n_cols
                item[header[i]] = line[start:end]
                start = end
            else:
                item[header[i]] = line[start] if start < len(line) else ''
                start += 1
        data.append(item)

    with open('output.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Conversion completed. Check output.json for the result.")

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
            convert_csv_to_json(filename)
        else:
            read_file_and_convert_to_json(filename)

if __name__ == "__main__":
    main()
