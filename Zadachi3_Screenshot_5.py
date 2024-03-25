import xml.etree.ElementTree as ET

tree = ET.parse('products.xml')
root = tree.getroot()

def get_product_info(product):
    name = product.find('name').text
    category = product.find('category').text
    price = float(product.find('price').text)
    return (name, category, price)

def sort_products_by_price():
    sorted_products = sorted(root.findall('product'), key=lambda x: float(x.find('price').text))
    for product in sorted_products:
        print(get_product_info(product))

def filter_products_by_category(category):
    filtered_products = [product for product in root.findall('product') if product.find('category').text == category]
    for product in filtered_products:
        print(get_product_info(product))

def calculate_total_order_price():
    total_price = sum([float(product.find('price').text) for product in root.findall('product')])
    print("Total order price:", total_price)

sort_products_by_price()
print("\nProducts in Electronics category:")
filter_products_by_category("Electronics")
calculate_total_order_price()
