def item_add():
    num_items = int(input("Please enter the number of items: "+'\n'))
    total_price = 0
    for i in range(0,num_items,1):
        item_price = float(input("Price of item: "))
        if 0 < item_price > 100:
            print("sorry this was invalid price, please try again"+'\n')
            item_price = float(input("Price of item: "))
        else:
            total_price = total_price + item_price

    if total_price > 100:
        total_price = total_price - (total_price * 0.1)
        print("You recieved a loyal customer discount of 10%! "+"\n")
    print("Your total comes to: ","$", total_price)


def main():
    item_add()
main()