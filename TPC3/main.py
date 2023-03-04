import re
import json

import re


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


# def frequencia_nomes_por_seculo(arquivo):
#     # Inicializa o dicionário de frequência por século
#     freq_por_seculo = {}
#
#     # Abre o arquivo de processos para leitura
#     with open(arquivo, 'r') as f:
#         # Lê cada linha do arquivo
#         for linha in f:
#             # Extrai o ano da data usando expressão regular
#             match = re.search(r'^\d+::(\d{4})-', linha)
#             if match:
#                 ano = int(match.group(1))
#
#                 # Calcula o século correspondente ao ano
#                 seculo = (ano - 1) // 100 + 1
#
#                 # Extrai os nomes das partes envolvidas no processo
#                 partes = re.findall(r'\b[A-Z][a-z]+\b', linha)
#                 for parte in partes:
#                     nome = parte.split()[0]
#                     apelido = parte.split()[-1]
#
#                     # Agrupa os nomes por século e calcula a frequência de cada um
#                     if seculo in freq_por_seculo:
#                         freq_por_seculo[seculo]['nomes'].update([nome])
#                         freq_por_seculo[seculo]['apelidos'].update([apelido])
#                     else:
#                         freq_por_seculo[seculo] = {'nomes': Counter([nome]), 'apelidos': Counter([apelido])}
#
#     # Apresenta os 5 nomes mais usados em cada século
#     for seculo in freq_por_seculo:
#         print(f'Século {seculo}:')
#         print('Nomes próprios:')
#         for nome, freq in freq_por_seculo[seculo]['nomes'].most_common(5):
#             print(f'{nome}: {freq}')
#         print('Apelidos:')
#         for apelido, freq in freq_por_seculo[seculo]['apelidos'].most_common(5):
#             print(f'{apelido}: {freq}')
#         print()

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
                    'ID': campos[0],
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
            frequencia_por_ano(arquivo)
        #elif opcao == '2':
            #frequencia_nomes_por_seculo(arquivo)
        elif opcao == '3':
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



