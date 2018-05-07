def exchange(money):
    usd = 57
    euro = 60
    al = 95
    currency = int(input("Укажите код валюты(доллары - 1. Евро - 2, Алжирский динар - 3 ): "))

    if currency == 1:
        cache = round(money / usd, 2)
        print("вылюта: доллары США ")
    elif currency == 2:
        cache = round(money / euro, 2)
        print("вылюта: Евро")
    elif currency == 3:
        cache = round(money / al, 2)
        print("вылюта: Алжирский динар")
    else:
        cache = 0
        print("Неизвестная валюта")
    print("к получению: ", cache)


def main():
    money = int(input("введите сумму, которую вы хотите обменять: "))
    exchange(money)


if __name__ == "__main__":
    main()