

def main():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928

    print("Electricity Calculator","\n")
    kwh_price = float(input("Please enter the cents per kWh: "))
    kwh_daily = float(input("Please enter daily kWh use: "))
    bill_days = int(input("Please enter billing period in days: "))

    bill_price = float(((kwh_price * kwh_daily) * bill_days) / 100)

    print("Select which Tariff you are using: " + "\n" +
                      "For Tariff 11 please enter (A)" + "\n" +
                      "For Tariff 31 please enter (B)" + "\n"
                        "or to quit enter (Q)")
    menu_choice = input()

    if menu_choice == "A" or "a":
        bill_price =  float((((kwh_price + TARIFF_11) * kwh_daily) * bill_days) / 100)
    elif menu_choice== "B" or "b":
        bill_price = float((((kwh_price + TARIFF_31) * kwh_daily) * bill_days) / 100)
    else:
        print("Sorry that was an invalid choice, please try again.")


    print("Your estimated bill is: $", format(bill_price,'.2f'))
main()