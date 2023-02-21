import matplotlib.pyplot as plt
import numpy as np
def parser():
    data = []

    with open("myheart.csv", "r") as f:
        f.readline()

        for line in f.readlines():
            l = []
            for p in line.split(","):
                l.append(p)
            l[-1] = l[-1][0]
            data.append(l)

    return data


def get_age_range(age):
    low = (age // 5) * 5
    up = low + 4
    return f"[{low}-{up}]"


def get_col_range(col):
    low = (col // 10) * 10
    up = low + 9
    return f"[{low}-{up}]"


def dist_sex(data):
    results = {"M": [0, 0], "F": [0, 0]}  # [x, y], x = tem doenca, y = nao tem

    for d in data:
        if d[1] == "M":
            if d[5] == "1":
                results["M"][0] += 1
            else:
                results["M"][1] += 1
        else:
            if d[5] == "1":
                results["F"][0] += 1
            else:
                results["F"][1] += 1

    if not any(results.values()):
        return {}
    else:
        # Cria gráfico de barras
        labels = ['Com doença', 'Sem doença']
        men_values = [results["M"][0], results["M"][1]]
        women_values = [results["F"][0], results["F"][1]]
        x = np.arange(len(labels))
        width = 0.35
        fig, ax = plt.subplots()
        ax.bar(x - width / 2, men_values, width, label='Homens')
        ax.bar(x + width / 2, women_values, width, label='Mulheres')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        plt.show()

        return results


def dist_age(data):
    results = {}

    for d in data:
        age = int(d[0])
        a_range = get_age_range(age)
        if a_range in results:
            if d[5] == "1":
                results[a_range] += 1
        else:
            results[a_range] = 0

    # Cria gráfico de barras
    labels = list(results.keys())
    values = list(results.values())
    if not labels:
        return {}
    else:
        x = np.arange(len(labels))
        width = 0.35
        fig, ax = plt.subplots()
        ax.bar(x, values, width)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)

        plt.show()
        return results


def dist_col(data):
    results = {}

    for d in data:
        col = int(d[3])
        col_range = get_col_range(col)
        if col_range in results:
            if d[5] == "1":
                results[col_range] += 1
        else:
            results[col_range] = 0

    # Cria gráfico de barras
    labels = list(results.keys())
    values = list(results.values())
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))  # larger graph
    ax.bar(x, values, width)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    plt.show()

    return results


def main():
    d = parser()
    while True:
        print(
            "Which distribution do you want to visualize?\n1 - Disease by sex\n2 - Disease by age\n3 - Disease by cholesterol\n")
        try:
            o = int(input("-> "))
        except ValueError:
            print("Invalid option.\n")
            continue

        if o in [1, 2, 3]:
            if o == 1:
                print("Sex:")
                r = dist_sex(d)
                print(
                    "M with disease: " + str(r["M"][0]) + "\nM without disease: " + str(r["M"][1]) + "\nF with disease: " + str(
                        r["F"][0]) + "\nF without disease: " + str(r["F"][1]) + "\n")
            elif o == 2:
                print("Age:")
                r = dist_age(d)
                for ran in r:
                    print(ran + ": " + str(r[ran]))

                print("\n")
            elif o == 3:
                r = dist_col(d)
                print("Cholesterol:")
                for ran in r:
                    print(ran + ": " + str(r[ran]))

                print("\n")
        else:
            print("Invalid option.\n")
            r = None


if __name__ == "__main__":
    main()
