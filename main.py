from Classes.Stock import Stock

stock = Stock()

print("---------- MENU ----------")
print("Digite: ")

while True:

    input_text = "1 - para ver as 5 ações com maior volume\n"
    input_text += "2 - para cotação de uma ação específica\n"
    input_text += "S - para sair\n"

    option = input(input_text)

    if option.lower() == "s":
        break
    elif option == "1":
        top_stocks = stock.top_stocks(5)
        print(stock.format_stock(top_stocks))
    elif option == "2":
        search = input("Digite o código da ação: ")
        if len(search) < 5:
            print("Digite um código de ação válido")
        else:
            search_stocks = stock.search_stock(search.upper())
            print(stock.format_stock(search_stocks))
    else:
        print("Digite uma opção válida")

    print("\n")
