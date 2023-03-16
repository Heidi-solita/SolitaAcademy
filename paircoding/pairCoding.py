def calculate_total_price(price, quantity):
    total_price = price * quantity
    return total_price

def calculate_total_with_taxes(total_price, tax_percent):
    total_tax = total_price * (tax_percent/100 + 1) 
    total_with_tax = total_price + total_tax
    return total_tax

def get_tax_rate(tax_dict, state):
    return tax_dict[state]

def get_discount_percent(total_price):
    if total_price >= 50000:
        return 15
        
    elif total_price >= 10000:
        return 10

    elif total_price >= 7000:
        return 7
    
    elif total_price >= 5000:
        return 5
    
    elif total_price >= 1000:
        return 3
    else:
        return 0


    
def main():

    tax_dict = {'UT': 6.85,
        'NV': 8.00,
        'TX': 6.25,
        'AL': 4.00,
        'CA': 8.25
        }

    valid_price = False
    while valid_price == False:
        try:
            price = float(input("Input product price: "))
            valid_price = True
        except:
            print("The input should be float")

    valid_quantity = False
    while valid_quantity == False:
        try:
            quantity = int(input("Input product quantity: "))
            valid_quantity = True
        except:
            print("The input should be int")
    #tax_percent = int(input("Input tax percentage of the product as an integer: "))

    valid_state = False
    while valid_state == False:
        state = input("Select tax state from one of the following (UT, NV, TX, AL, CA): ")
        if state in tax_dict.keys():
            valid_state = True
        else:
            print("The input should be one of the following (UT, NV, TX, AL, CA)")
        


    total_price = calculate_total_price(price, quantity)
    tax_percent = get_tax_rate(tax_dict, state)
    total_price_with_tax = calculate_total_with_taxes(total_price, tax_percent)
    discount_percent = get_discount_percent(total_price_with_tax)

    if discount_percent > 0:
        discount_price = round(total_price_with_tax * ((100 - discount_percent)/100), 2)
    else:
        discount_price = total_price_with_tax

    print("total price without tax: " + str(total_price))
    print("total price with tax: " + str(round(total_price_with_tax, 2)))
    print("calculated discount percent is " + str(discount_percent) + " %. The price with discount is " + str(discount_price))

if __name__ == "__main__":
    main()