import re
from collections import Counter
import json

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

# def frequencia_nomes_por_seculo(arquivo):2
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
    return relacoes

# def ler_registros(arquivo):
#     """
#     Lê os registros do arquivo e retorna uma lista de strings, uma para cada registro.
#     """
#     with open(arquivo, 'r', encoding='utf8') as f:
#         registros = f.read().split('\n\n')
#     return registros
#
# def registro_para_dict(registro):
#     """
#     Converte um registro (string) em um dicionário com as informações do registro.
#     """
#     campos = registro.split('::')
#     return {
#         'num_processo': int(campos[0]),
#         'data_nascimento': campos[1],
#         'nome': campos[2],
#         'nome_pai': campos[3],
#         'nome_mae': campos[4],
#         'nome_avo1': campos[5] if len(campos) >= 6 else '',
#         'nome_avo2': campos[6] if len(campos) >= 7 else '',
#         'relacao_avo1': campos[7] if len(campos) >= 8 else '',
#         'relacao_avo2': campos[8] if len(campos) >= 9 else ''
#     }
#
# def converter_para_json(arquivo, num_registros=20, nome_arquivo_saida='output.json'):
#     registros = ler_registros(arquivo)[:num_registros]
#     json_registros = [registro_para_dict(registro) for registro in registros]
#
#     with open(nome_arquivo_saida, 'w') as f:
#         json.dump(json_registros, f, indent=4)
#
#     print(f'Os primeiros {num_registros} registros foram convertidos para JSON e salvos em {nome_arquivo_saida}.')


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
        #elif opcao == '2':
            #frequencia_nomes_por_seculo(arquivo)
        elif opcao == '3':
            freq_relacoes = frequencia_relacoes(arquivo)
            for relacao, freq in freq_relacoes.items():
                print(f'{relacao}: {freq}')
        #elif opcao == '4':
            #converter_para_json(arquivo)
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')
        print("\n")

if __name__ == '__main__':
    main()
