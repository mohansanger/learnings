subTotal=float(input("Enter Subtotal Of Resturant Bill: "))
friends=int(input("Enter Number of Friends:"))

def bill_split(subTotal,friends):
    totalBill=subTotal+(subTotal*20)/100
    totalBill=totalBill/friends
    return totalBill

print("Each Friend has to pay:",round(bill_split(subTotal,friends),2))