import re
import sys

def main():
    levantado = False
    accepted_coins = {'5c': 0.05, '10c': 0.10, '20c': 0.20, '50c': 0.50, '1e': 1.00, '2e': 2.00}
    saldo = 0
    print("Cabine Telefónica")
    print("Moedas Aceites -> 5c, 10c, 20c, 50c, 1e, 2e")

    while True:
        comando = input("> ")

        if re.match(r"^(?i:LEVANTAR)$", comando):
            if levantado:
                print('maq: "Auscultador já levantado!"')
                continue
            else:
                levantado = True
                print('maq: "Introduza moedas."')
        elif re.match(r"^(?i:POUSAR)$", comando):
            if levantado:
                coins_returned = []
                for coin, value in sorted(accepted_coins.items(), reverse=True, key=lambda x: x[1]):
                    while saldo >= value:
                        saldo -= value
                        coins_returned.append(coin)
                coins_str = ", ".join([f"1x{c}" for c in coins_returned])
                if saldo == 0:
                    print(f'maq: "Volte sempre!"')
                else:
                    print(f'maq: "troco= {coins_str}; Volte sempre!"')
                levantado = False
            else:
                print('maq: "Auscultador já pousado!"')
        elif re.match(r"^(?i:ABORTAR)$", comando):
            sys.exit()
        elif re.match(r"^(?i:MOEDA)", comando):
            if levantado:
                input_coins = re.findall(r'\b(\d+[ce])\b', comando)
                unaccepted_coins = []
                for c in input_coins:
                    if c not in accepted_coins:
                        unaccepted_coins.append(c)
                    else:
                        saldo += accepted_coins[c]
                if len(unaccepted_coins) != 0:
                    string = 'maq: ' + '"' + ', '.join(unaccepted_coins) + ' - moeda inválida; saldo = ' + str(saldo) + 'c"'
                    string = re.sub(r'\.', 'e', string)
                    string = re.sub(r'€', 'c', string)
                    print(string)
                else:
                    string = 'maq: ' + '"' + 'saldo = ' + str(saldo) + 'c"'
                    string = re.sub(r'\.', 'e', string)
                    string = re.sub(r'€', 'c', string)
                    print(string)
            else:
                print('maq: "Auscultador tem que estar levantado!"')
                continue
        elif re.match(r"^[Tt]=", comando):
            if levantado:
                num = re.search(r'[Tt]=(\d+)', comando).group(1)
                if re.search(r'(\d{3})', num).group(1) in ['601', '641']:
                    print('maq: "Esse número não é permitido neste telefone. Queira discar novo número!"')
                    continue
                elif re.search(r'(\d{2})', num).group(1) == '00':
                    if saldo < 1.5:
                        print('maq: "Saldo insuficiente!"')
                    else:
                        saldo -= 1.5
                        print('maq: "saldo = %.2f' % saldo + '"')
                elif re.search(r'(\d{1})', num).group(1) == '2':
                    if saldo < 0.25:
                        print('maq: "Saldo insuficiente!"')
                    else:
                        saldo -= 0.25
                        print('maq: "saldo = %.2f' % saldo + '"')
                elif re.search(r'(\d{3})', num).group(1) == '800':
                    print('maq: "saldo = %.2f' % saldo + '"')
                elif re.search(r'(\d{3})', num).group(1) == '808':
                    if saldo < 0.10:
                        print('maq: "Saldo insuficiente!"')
                    else:
                        saldo -= 0.10
                        print('maq: "saldo = %.2f' % saldo + '"')
            else:
                print("Auscultador tem que estar levantado!")
                continue
        else:
            print('maq: "Comando inválido! Tente novamente."')

if __name__ == "__main__":
    main()
