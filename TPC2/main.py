def main():
    total = 0
    summing = True

    print("Enter the text:")
    text = input("> ")

    i = 0
    while i < len(text):
        if text[i:i+3].lower() == "off":
            summing = False
            i += 3
        elif text[i:i+2].lower() == "on":
            summing = True
            i += 2
        elif text[i] == "=":
            print(total)
            i += 1
        elif summing == True:
            num_str = ""
            while i < len(text) and (text[i].isdigit() or text[i] == " "):
                if text[i] != " ":
                    num_str += text[i]
                i += 1
            if num_str:
                total += int(num_str)
        elif summing == False:
            i += 1

if __name__ == "__main__":
    main()
