import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    print("""
====================
Inventory CLI
====================
1. View Inventory
2. Add Item
3. Update Item
4. Delete Item
5. Fetch External Product
6. Exit
""")

def view():
    r = requests.get(f"{BASE_URL}/inventory")
    print(r.json())

def add():
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    r = requests.post(f"{BASE_URL}/inventory", json={
        "product_name": name,
        "price": price,
        "stock": stock
    })

    print(r.json())

def update():
    item_id = input("Item ID: ")
    price = float(input("New price: "))

    r = requests.patch(f"{BASE_URL}/inventory/{item_id}", json={
        "price": price
    })

    print(r.json())

def delete():
    item_id = input("Item ID: ")
    r = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(r.json())

def external():
    barcode = input("Enter barcode: ")
    r = requests.get(f"{BASE_URL}/inventory/enrich/{barcode}")
    print(r.json())

def main():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            view()
        elif choice == "2":
            add()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            external()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()