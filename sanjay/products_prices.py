stores = {}
for _ in range(int(input("No. of products: "))):
    inp = input().split(' ')
    product = inp[0]
    price = inp[1]
    stores[product.lower()] = int(price)

cust = input('Product name: ')
print(stores[cust.lower()])