import re
import json

def frequencia_por_ano(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

        freq_ano = {}

        for linha in linhas:
            ano = re.findall(r'^\d+::(\d{4})-', linha)
            if ano:
                ano = ano[0]
                if ano in freq_ano:
                    freq_ano[ano] += 1
                else:
                    freq_ano[ano] = 1

        freq_ano_s = list(freq_ano.items())
        freq_ano_s.sort(key=lambda x: x[1], reverse=True)

        for key, value in freq_ano_s:
            print(f"{key}: {value}")

def nome_apelido_por_seculo(arquivo):
    nomes = {}
    apelidos = {}
    with open(arquivo, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            campos = line.split('::')
            try:
                nome, apelido = re.findall(r'^(\w+)\s(.+)\s(\w+)\s*$', campos[2])[0][0], re.findall(r'^(\w+)\s(.+)\s(\w+)\s*$', campos[2])[0][2]
                ano = int(campos[1][:4])
                seculo = (ano - 1) // 100 + 1
                if seculo not in nomes:
                    nomes[seculo] = {}
                    apelidos[seculo] = {}
                if nome not in nomes[seculo]:
                    nomes[seculo][nome] = 0
                nomes[seculo][nome] += 1
                if apelido not in apelidos[seculo]:
                    apelidos[seculo][apelido] = 0
                apelidos[seculo][apelido] += 1
            except IndexError:
                # skip lines with incorrect format or missing values
                continue
    for seculo in nomes:
        print(f"--- Século {seculo} ---")
        top_nomes = sorted(nomes[seculo], key=nomes[seculo].get, reverse=True)[:5]
        print(f"Top 5 nomes: {', '.join(top_nomes)}")
        top_apelidos = sorted(apelidos[seculo], key=apelidos[seculo].get, reverse=True)[:5]
        print(f"Top 5 apelidos: {', '.join(top_apelidos)}")


def frequencia_relacoes(arquivo):
    relacoes = {}
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            relacao = re.findall(r'Tio Materno|Tio Paterno|Irmao[s]?|Primo Materno|Primo Paterno|Sobrinho Materno|Sobrinho Paterno|Filho|Pai|Avo Materno|Avo Paterno', linha)
            for r in relacao:
                if r in relacoes:
                    relacoes[r] += 1
                else:
                    relacoes[r] = 1
    sorted_relacoes = sorted(relacoes.items(), key=lambda item: (-item[1], item[0] != 'Avo'))
    return dict(sorted_relacoes)

def converter_para_json(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = []
        for linha in f:
            campos = linha.strip().split('::')
            if len(campos) >= 7:
                registro = {
                    'Pasta': campos[0],
                    'Data': campos[1],
                    'Nome': campos[2],
                    'Pai': campos[3],
                    'Mae': campos[4],
                    'Obs': campos[5],
                    'Obs2': campos[6]
                }
                dados.append(registro)
                if len(dados) == 20:
                    break

    with open('processos.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def main():
    arquivo = 'processos.txt'

    while True:
        print('Escolha uma opção:')
        print('1 - Frequência de processos por ano')
        print('2 - Frequência de nomes próprios e apelidos por século')
        print("3 - Frequência de relações")
        print("4 - Converter os 20 primeiros registros para JSON")
        print('5 - Sair')
        opcao = input("Opção: ")

        if opcao == '1':
            print("\n")
            frequencia_por_ano(arquivo)
        elif opcao == '2':
            print("\n")
            nome_apelido_por_seculo(arquivo)
        elif opcao == '3':
            print("\n")
            freq_relacoes = frequencia_relacoes(arquivo)
            for relacao, freq in freq_relacoes.items():
                print(f'{relacao}: {freq}')
        elif opcao == '4':
            converter_para_json(arquivo)
            print("Feito!")
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')
        print("\n")

if __name__ == '__main__':
    main()
