from abc import ABC, abstractmethod
from decimal import Decimal
import json



#internet store: Product(ABC), DiscountPercentOff(ABC) and DiscountCuponCode(ABC), Receipt(ABC), SaveOrder(ABC)
# (id,name,price,description,in_stock,product_qty) (discount_percent:int) (discount_code:str)  (total_price,item_num,disc_amount,
# Order class
# Holds order ID, customer ID, list of OrderItems, and created_at.
# Method subtotal() → sum of OrderItem.line_total()
# Validation for non-empty items.
# Receipt class (can be a simple data container)
# Holds subtotal, discounts_total, after_discounts,
# tax, grand_total, details (list of discount info).
# price_order function
# Input: Order, list of Discounts, tax rate.
# Output: Receipt.
# Applies each discount, sums them, applies tax, builds receipt.
# SaveOrder
# Function or class to save order data to JSON file (append/upsert).
# Integration flow (demo for your homework)
# Load products → create OrderItems → create Order →
# apply discounts with price_order → make Invoice → save order + invoice

class Product(ABC):
    def __init__(self,
                 id:str,
                 name:str,
                 price:Decimal,
                 description:str,
                 in_stock:bool
                 ,product_qty:int
                 ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.in_stock = in_stock
        self.product_qty = product_qty
    @abstractmethod
    def get_final_price(self)->Decimal:pass

class PhysicalProduct(Product):
    def get_final_price(self)->Decimal:return self.price

class OrderItem:
    def __init__(self,product:Product,qty:int):
        if qty<1:
            raise ValueError('qty is less than 1')
        if product.price<Decimal(0):
            raise ValueError('price is less than 0')
        if product.in_stock and qty > product.product_qty:
            raise ValueError('quantity more then stock')
        self.product = product
        self.qty = qty
    def line_total(self)->Decimal:
        return self.product.get_final_price() * self.qty

class Discount(ABC):
    @abstractmethod
    def apply(self,subtotal:Decimal):pass

class CuponDiscount(Discount):
    def __init__(self,amount:Decimal,code:str):
        self.amount = amount
        self.code = code
    def apply(self,subtotal:Decimal)->tuple[Decimal,str]:
        if subtotal<Decimal("0"):
            raise ValueError('subtotal is less than 0')
        discount_amount = min(self.amount,subtotal)
        return discount_amount,f"Cupon {self.code}"

class PercentDiscount(Discount):
    def __init__(self,percent:Decimal):
        self.percent = percent
    def apply(self,subtotal:Decimal)->tuple[Decimal,str]:

        if subtotal<Decimal(0):
            raise ValueError('subtotal is less than 0')
        discount_amount = subtotal*(self.percent/Decimal('100'))
        return discount_amount,f"Percent {self.percent} off"

class Order:
    def __init__(self,id:str,customer_id:str,items:list[OrderItem],created_at:str):
        if not items:
            raise ValueError('items is empty')
        self.id = id
        self.customer_id = customer_id
        self.id = id
        self.customer_id = customer_id
        self.items = items
        self.created_at = created_at
        if self.subtotal()<Decimal('0'):
            raise ValueError('subtotal is less than 0')
    def subtotal(self)->int:
        total = Decimal('0')
        for i in self.items:
            total += i.line_total()
        return total
    def item_count(self)->int:
        return sum(i.qty for i in self.items)

# =========================
# PRODUCT REPOSITORY CLASS
# =========================
class ProductRepository:
    # Constructor: takes the file path where our product "database" (JSON) is stored
    def __init__(self, db_path: str):
        self.db_path = db_path

    # Load ALL products from the JSON file and return them as a list of Product objects
    def get_all(self) -> list[Product]:
        # Open the JSON file in read mode, using UTF-8 encoding
        with open(self.db_path, "r", encoding="utf-8") as file:
            # Load the raw JSON data into a Python list of dicts
            raw_data = json.load(file)

        products = []  # empty list to store converted Product objects

        # Loop through every product dictionary from the JSON file
        for p in raw_data:
            # Convert the 'price' from float to Decimal for accuracy
            price = Decimal(str(p["price"]))
            # Create a PhysicalProduct object from the dictionary data
            products.append(
                PhysicalProduct(
                    p['id'],           # product id (string)
                    p["name"],         # product name (string)
                    price,             # price (Decimal)
                    p["description"],  # description text
                    p["in_stock"],     # boolean: True if available
                    p["product_qty"],  # how many units in stock
                )
            )
        return products  # list of PhysicalProduct objects

    def get_by_id(self, product_id: str) -> Product | None:
        for p in self.get_all():
            if p.id == product_id:
                return p
        return None


# =========================
# INVOICE CLASS
# =========================
class Invoice:
    # Constructor: needs an Order object and a Receipt object
    def __init__(self, order, receipt):
        self.order = order      # the order with products, qty, customer info
        self.receipt = receipt  # the pricing result (totals, discounts, etc.)

    # Convert the invoice data into a dictionary (ready to turn into JSON)
    def to_dict(self) -> dict:
        return {
            # Order-level information
            "order_id": self.order.id,
            "customer_id": self.order.customer_id,
            # Convert datetime to a string in ISO format (e.g. "2025-08-15T14:30:00")
            "created_at": self.order.created_at.isoformat(),

            # Items in the order
            "items": [
                {
                    "product_id": item.product.id,             # product id
                    "name": item.product.name,                 # product name
                    "qty": item.qty,                           # quantity ordered
                    "unit_price": str(item.product.price),     # price per unit (as string for JSON)
                    "line_total": str(item.product.price * item.qty),  # qty × price
                }
                for item in self.order.items  # loop through all items in the order
            ],

            # Totals from the receipt object
            "totals": {
                "subtotal": str(self.receipt.subtotal),                 # total before discounts/tax
                "discounts_total": str(self.receipt.discounts_total),   # total discount amount
                "after_discounts": str(self.receipt.after_discounts),   # subtotal - discounts
                "tax": str(self.receipt.tax),                           # tax amount
                "grand_total": str(self.receipt.grand_total),           # final total
            },

            # Details of applied discounts (list of {"label":..., "amount":...})
            "discount_details": self.receipt.details,
        }
