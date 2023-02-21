
def converter(amount, conv_type):

    if conv_type == 1:
        amount *= 1.21
        return amount
    
    amount *= 0.82
    return amount

type_input = int(input("Convert GBP to USD (1), or USD to GBP (2): "))
amount_input = float(input("How much money would you like to covert?: "))

converted_output = converter(amount_input, type_input)
print("%.2f" % converted_output)