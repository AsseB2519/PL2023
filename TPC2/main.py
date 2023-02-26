def calculate_sum(text):
    if not text:
        return 0

    sum = 0
    summing = True
    tmp_str = "0"

    i = 0
    while i < len(text):
        if text[i:i + 3].lower() == "off":
            summing = False
            if tmp_str != "0":
                sum += int(tmp_str)
            tmp_str = "0"
            i += 3
        elif summing != True and text[i:i + 2].lower() == "on":
            summing = True
            i += 2
        elif text[i] == "=":
            if tmp_str != "0":
                sum += int(tmp_str)
            tmp_str = "0"
            i += 1
        elif summing == True:
            if text[i].isdigit():
                tmp_str += text[i]
            else:
                if tmp_str != "0":
                    sum += int(tmp_str)
                tmp_str = "0"
            i += 1
        elif summing == False:
            i += 1
    if tmp_str != "0" and summing:
        sum += int(tmp_str)
    return sum


def main():
    while True:
        text = input("Introduza o texto (# para sair): ")
        if text == "#":
            break
        result = 0
        i = 0
        while i < len(text):
            if text[i] == "=":
                partial_text = text[:i+1]
                partial_result = calculate_sum(partial_text)
                print(f"{partial_text} -> {partial_result}")
                result += partial_result
                text = text[i+1:]
                i = 0
                print(f"Resultado: {result}")
            else:
                i += 1


if __name__ == "__main__":
    print("Bem-vindo à Calculadora de Texto!")
    print("Digite uma sequência de caracteres com números e as palavras 'off' e 'on'")
    print("Use o sinal '=' para indicar o fim de uma sequência e calcular o resultado")
    print("Digite '#' para sair")

    main()
