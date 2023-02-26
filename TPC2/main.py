def main():
    sum = 0
    summing = True

    print("Introduza o texto.")
    text = input("> ")

    tmp_str = "0"

    i = 0
    while i < len(text):
        if text[i:i + 3].lower() == "off":
            summing = False
            sum += int(tmp_str)
            tmp_str = "0"
            i += 3
        elif summing != True and text[i:i + 2].lower() == "on":
            summing = True
            i += 2
        elif text[i] == "=":
            sum += int(tmp_str)
            tmp_str = "0"
            print(sum)
            i += 1
        elif summing == True:
            if text[i].isdigit():
                tmp_str += text[i]
            else:
                sum += int(tmp_str)
                tmp_str = "0"
            i += 1
        elif summing == False:
            i += 1


if __name__ == "__main__":
    main()
