'''
  Luis Montes
'''


def can_be_converted_to_float(value):
    try:
        float(value)
        return True
    except Exception:
        return False


def computeProfit(productData):
    return (productData.get("sell_price") - productData.get("cost_price")) * productData.get("inventory")


inventoryQuantity = input("Please enter inventory quantity: ")
while not(can_be_converted_to_float(inventoryQuantity)):
    inventoryQuantity = input("Please enter a non decimal number: ")

costPrice = input("Please enter unit cost price: ")
while not(can_be_converted_to_float(costPrice)):
    costPrice = input("Please enter unit cost price: ")

sellPrice = input("Please enter unit sell price: ")
while not(can_be_converted_to_float(sellPrice)):
    sellPrice = input("Please enter unit sell price: ")

productDictionary = {}
productDictionary["inventory"] = float(inventoryQuantity)
productDictionary["cost_price"] = float(costPrice)
productDictionary["sell_price"] = float(sellPrice)

profit = computeProfit(productDictionary)
print("Profit amount: ", str(profit))
