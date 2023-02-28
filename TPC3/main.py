import re

def frequencia_por_ano(arquivo):
    # inicializa o dicionário de frequência
    freq_anos = {}

    # abre o arquivo de processos para leitura
    with open(arquivo, 'r') as f:
        # lê cada linha do arquivo
        for linha in f:
            # extrai o ano da data usando expressão regular

            # ^ -> indica que a busca deve começar no início da string
            # \d+ -> busca um ou mais dígitos no início da string. Isso serve para ignorar o primeiro elemento da linha, que é o número do processo.
            # :: -> procura por dois pontos consecutivos, que separam o primeiro elemento da data do segundo.
            # (\d{4}) -> é um grupo de captura que busca exatamente 4 dígitos. Esses 4 dígitos correspondem ao ano.
            # - -> procura pelo caractere hífen que segue o ano. Isso serve para ignorar o restante da data, já que estamos interessados apenas no ano.
            match = re.search(r'^\d+::(\d{4})-', linha)
            if match:
                ano = match.group(1)

                # atualiza a frequência de processos para o ano correspondente
                if ano in freq_anos:
                    freq_anos[ano] += 1
                else:
                    freq_anos[ano] = 1

    # retorna a frequência de processos por ano
    return freq_anos

import re
from collections import Counter

def frequencia_nomes_por_seculo(arquivo):
    # Inicializa o dicionário de frequência por século
    freq_por_seculo = {}

    # Abre o arquivo de processos para leitura
    with open(arquivo, 'r') as f:
        # Lê cada linha do arquivo
        for linha in f:
            # Extrai o ano da data usando expressão regular
            match = re.search(r'^\d+::(\d{4})-', linha)
            if match:
                ano = int(match.group(1))

                # Calcula o século correspondente ao ano
                seculo = (ano - 1) // 100 + 1

                # Extrai os nomes das partes envolvidas no processo
                partes = re.findall(r'\b[A-Z][a-z]+\b', linha)
                for parte in partes:
                    nome = parte.split()[0]
                    apelido = parte.split()[-1]

                    # Agrupa os nomes por século e calcula a frequência de cada um
                    if seculo in freq_por_seculo:
                        freq_por_seculo[seculo]['nomes'].update([nome])
                        freq_por_seculo[seculo]['apelidos'].update([apelido])
                    else:
                        freq_por_seculo[seculo] = {'nomes': Counter([nome]), 'apelidos': Counter([apelido])}

    # Apresenta os 5 nomes mais usados em cada século
    for seculo in freq_por_seculo:
        print(f'Século {seculo}:')
        print('Nomes próprios:')
        for nome, freq in freq_por_seculo[seculo]['nomes'].most_common(5):
            print(f'{nome}: {freq}')
        print('Apelidos:')
        for apelido, freq in freq_por_seculo[seculo]['apelidos'].most_common(5):
            print(f'{apelido}: {freq}')
        print()


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
            freq_anos = frequencia_por_ano(arquivo)
            for ano, freq in freq_anos.items():
                print(f'{ano}: {freq}')
        elif opcao == '2':
            frequencia_nomes_por_seculo(arquivo)

        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()


