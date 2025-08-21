from abc import ABC, abstractmethod
from decimal import Decimal
import json
from datetime import datetime
import os

# =========================
# PRODUCT CLASSES
# =========================
class Product(ABC):
    def __init__(self, id: str, name: str, price: Decimal,
                 description: str, in_stock: bool, product_qty: int):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.in_stock = in_stock
        self.product_qty = product_qty

    @abstractmethod
    def get_final_price(self) -> Decimal:
        pass


class PhysicalProduct(Product):
    def get_final_price(self) -> Decimal:
        return self.price


class OrderItem:
    def __init__(self, product: Product, qty: int):
        if qty < 1:
            raise ValueError("qty is less than 1")
        if product.price < Decimal(0):
            raise ValueError("price is less than 0")
        if product.in_stock and qty > product.product_qty:
            raise ValueError("quantity more than stock")
        self.product = product
        self.qty = qty

    def line_total(self) -> Decimal:
        return self.product.get_final_price() * self.qty


# =========================
# DISCOUNT CLASSES
# =========================
class Discount(ABC):
    @abstractmethod
    def apply(self, subtotal: Decimal):
        pass


class CuponDiscount(Discount):
    def __init__(self, amount: Decimal, code: str):
        self.amount = amount
        self.code = code

    def apply(self, subtotal: Decimal) -> tuple[Decimal, str]:
        if subtotal < Decimal("0"):
            raise ValueError("subtotal is less than 0")
        discount_amount = min(self.amount, subtotal)
        return discount_amount, f"Cupon {self.code}"


class PercentDiscount(Discount):
    def __init__(self, percent: Decimal):
        self.percent = percent

    def apply(self, subtotal: Decimal) -> tuple[Decimal, str]:
        if subtotal < Decimal(0):
            raise ValueError("subtotal is less than 0")
        discount_amount = subtotal * (self.percent / Decimal("100"))
        return discount_amount, f"Percent {self.percent} off"


# =========================
# ORDER CLASS
# =========================
class Order:
    def __init__(self, id: str, customer_id: str,
                 items: list[OrderItem], created_at: datetime):
        if not items:
            raise ValueError("items is empty")
        self.id = id
        self.customer_id = customer_id
        self.items = items
        self.created_at = created_at
        if self.subtotal() < Decimal("0"):
            raise ValueError("subtotal is less than 0")

    def subtotal(self) -> Decimal:
        return sum(i.line_total() for i in self.items)

    def item_count(self) -> int:
        return sum(i.qty for i in self.items)


# =========================
# PRODUCT REPOSITORY CLASS
# =========================
class ProductRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_all(self) -> list[Product]:
        with open(self.db_path, "r", encoding="utf-8") as file:
            raw_data = json.load(file)

        products = []
        for p in raw_data:
            price = Decimal(str(p["price"]))
            products.append(
                PhysicalProduct(
                    p["id"],
                    p["name"],
                    price,
                    p["description"],
                    p["in_stock"],
                    p["product_qty"],
                )
            )
        return products

    def get_by_id(self, product_id: str) -> Product | None:
        for p in self.get_all():
            if p.id == product_id:
                return p
        return None


# =========================
# RECEIPT CLASS
# =========================
class Receipt:
    def __init__(self, subtotal: Decimal, discounts_total: Decimal,
                 after_discounts: Decimal, tax: Decimal,
                 grand_total: Decimal, details: list[dict]):
        self.subtotal = subtotal
        self.discounts_total = discounts_total
        self.after_discounts = after_discounts
        self.tax = tax
        self.grand_total = grand_total
        self.details = details


# =========================
# PRICE ORDER func
# =========================
def price_order(order: Order, discounts: list[Discount], tax_rate: Decimal) -> Receipt:
    subtotal = order.subtotal()
    discounts_total = Decimal("0")
    details = []

    for d in discounts:
        discount_amount, label = d.apply(subtotal - discounts_total)
        discounts_total += discount_amount
        details.append({"label": label, "amount": str(discount_amount)})

    after_discounts = subtotal - discounts_total
    tax = after_discounts * (tax_rate / Decimal("100"))
    grand_total = after_discounts + tax

    return Receipt(subtotal, discounts_total, after_discounts, tax, grand_total, details)


# =========================
# INVOICE CLASS
# =========================
class Invoice:
    def __init__(self, order: Order, receipt: Receipt):
        self.order = order
        self.receipt = receipt

    def to_dict(self) -> dict:
        return {
            "order_id": self.order.id,
            "customer_id": self.order.customer_id,
            "created_at": self.order.created_at.isoformat(),
            "items": [
                {
                    "product_id": item.product.id,
                    "name": item.product.name,
                    "qty": item.qty,
                    "unit_price": str(item.product.price),
                    "line_total": str(item.line_total()),
                }
                for item in self.order.items
            ],
            "totals": {
                "subtotal": str(self.receipt.subtotal),
                "discounts_total": str(self.receipt.discounts_total),
                "after_discounts": str(self.receipt.after_discounts),
                "tax": str(self.receipt.tax),
                "grand_total": str(self.receipt.grand_total),
            },
            "discount_details": self.receipt.details,
        }


# =========================
# SAVE ORDER CLASS
# =========================
class SaveOrder:
    def __init__(self, out_dir: str):
        self.out_dir = out_dir

    def save(self, invoice: "Invoice") -> str:
        os.makedirs(self.out_dir, exist_ok=True)
        ts = invoice.order.created_at.strftime("%Y%m%d_%H%M%S")
        safe_order_id = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in invoice.order.id)
        file_name = f"invoice_{safe_order_id}_{ts}.json"
        path = os.path.join(self.out_dir, file_name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(invoice.to_dict(), f, indent=2)
        return path


# =========================
# CART
# =========================
class Cart:
    def __init__(self):
        self._items: dict[str, int] = {}  # product_id -> qty

    def add(self, product_id: str, qty: int = 1):
        if qty < 1:
            raise ValueError("qty must be >= 1")
        self._items[product_id] = self._items.get(product_id, 0) + qty

    def remove(self, product_id: str, qty: int | None = None):
        if product_id not in self._items:
            return
        if qty is None or qty >= self._items[product_id]:
            del self._items[product_id]
        else:
            self._items[product_id] -= qty

    def clear(self):
        self._items.clear()

    def is_empty(self) -> bool:
        return not self._items

    def items(self) -> dict[str, int]:
        return dict(self._items)


class StoreApp:
    def __init__(self, products_path: str, invoices_dir: str):
        self.repo = ProductRepository(products_path)
        self.products = self.repo.get_all()
        self.cart = Cart()
        self.saver = SaveOrder(invoices_dir)

    def run(self):
        while True:
            print("\n=== STORE ===")
            print("1) Catalog")
            print("2) Add to cart")
            print("3) View cart")
            print("4) Remove from cart")
            print("5) Checkout")
            print("6) Exit")
            choice = input("Choose: ").strip()

            if choice == "1":
                self.show_catalog()
            elif choice == "2":
                self.handle_add()
            elif choice == "3":
                self.show_cart()
            elif choice == "4":
                self.handle_remove()
            elif choice == "5":
                self.checkout_flow()
            elif choice == "6":
                print("Bye.")
                return
            else:
                print("Unknown option.")

    def show_catalog(self):
        print("\n--- Catalog ---")
        for p in self.products:
            stock = f"{p.product_qty} pcs" if p.in_stock else "out of stock"
            print(f"{p.id}: {p.name} | ${p.price} | {stock}")
            print(f"    {p.description}")

    def handle_add(self):
        pid = input("Product ID: ").strip()
        qty = int(input("Qty: ").strip() or "1")
        prod = next((p for p in self.products if p.id == pid), None)
        if not prod:
            print("No such product.")
            return
        try:
            if prod.in_stock and qty > prod.product_qty:
                print("Quantity exceeds stock.")
                return
            self.cart.add(pid, qty)
            print("Added.")
        except ValueError as e:
            print(f"Error: {e}")

    def show_cart(self):
        if self.cart.is_empty():
            print("\nCart is empty.")
            return
        print("\n--- Cart ---")
        total = Decimal("0")
        for pid, qty in self.cart.items().items():
            p = next((x for x in self.products if x.id == pid), None)
            if not p:
                continue
            line = p.price * qty
            total += line
            print(f"{pid}: {p.name} x{qty}  = ${line}")
        print(f"Subtotal: ${total}")

    def handle_remove(self):
        pid = input("Product ID to remove: ").strip()
        mode = input("Remove qty (number) or 'all': ").strip().lower()
        if mode == "all":
            self.cart.remove(pid, None)
        else:
            try:
                self.cart.remove(pid, int(mode))
            except ValueError:
                print("Invalid qty.")
                return
        print("Updated.")

    def checkout_flow(self):
        if self.cart.is_empty():
            print("Cart is empty.")
            return

        customer_id = input("Customer ID: ").strip() or "CUST01"
        order_id = input("Order ID: ").strip() or f"ORD{datetime.now().strftime('%H%M%S')}"
        tax_rate = Decimal(input("Tax % (e.g. 7): ").strip() or "7")

        tokens = input("Discounts (C for cupon and/or \nP for % \nAs 'C5 P10'->cupon5 or 10%off; empty for none): ").strip().split()
        discounts: list[Discount] = []
        for t in tokens:
            t = t.upper()
            if t.startswith("C") and t[1:].isdigit():
                discounts.append(CuponDiscount(Decimal(t[1:]), t))
            elif t.startswith("P") and t[1:].isdigit():
                discounts.append(PercentDiscount(Decimal(t[1:])))
            else:
                print(f"Skip unknown discount token: {t}")

        # Build order items from cart
        items: list[OrderItem] = []
        for pid, qty in self.cart.items().items():
            p = next((x for x in self.products if x.id == pid), None)
            if not p:
                continue
            try:
                items.append(OrderItem(p, qty))
            except ValueError as e:
                print(f"Skip {pid}: {e}")
        if not items:
            print("Nothing to checkout.")
            return

        order = Order(order_id, customer_id, items, datetime.now())
        receipt = price_order(order, discounts, tax_rate)
        invoice = Invoice(order, receipt)
        path = self.saver.save(invoice)
        for it in items:
            if it.product.in_stock:
                it.product.product_qty -= it.qty
                if it.product.product_qty <= 0:
                    it.product.in_stock = False

        print("\n--- INVOICE ---")
        print(json.dumps(invoice.to_dict(), indent=2))
        print(f"Saved to: {path}")
        self.cart.clear()


if __name__ == "__main__":
    StoreApp(products_path="products.json", invoices_dir="invoices").run()
