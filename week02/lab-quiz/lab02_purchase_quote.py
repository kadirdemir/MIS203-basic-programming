"""Week 2 lab: calculate a purchase quote for two items."""

print("Two-Item Purchase Quote")

# input() always returns text, so quantities are converted to int
# and money/tax values are converted to float before calculations.
item_one = input("First item name: ").strip()
quantity_one = int(input("First quantity: "))
unit_price_one = float(input("First unit price: "))

item_two = input("Second item name: ").strip()
quantity_two = int(input("Second quantity: "))
unit_price_two = float(input("Second unit price: "))

delivery_fee = float(input("Delivery fee: "))
tax_percent = float(input("Tax percentage: "))

# Calculate each item line and the subtotal.
line_one = quantity_one * unit_price_one
line_two = quantity_two * unit_price_two
subtotal = line_one + line_two

# Tax is applied only to the item subtotal.
tax_amount = subtotal * tax_percent / 100

# Delivery is added after the tax calculation.
final_total = subtotal + tax_amount + delivery_fee

print()
print("PURCHASE QUOTE")
print(f"{item_one}: {quantity_one} x {unit_price_one:.2f} = {line_one:.2f} TRY")
print(f"{item_two}: {quantity_two} x {unit_price_two:.2f} = {line_two:.2f} TRY")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax ({tax_percent:.2f}%): {tax_amount:.2f} TRY")
print(f"Delivery: {delivery_fee:.2f} TRY")
print(f"Final Total: {final_total:.2f} TRY")
