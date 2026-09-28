"""Week 2 lab: calculate a purchase quote for two items."""

print("=== Two-Item Purchase Quote ===")

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

# Calculate each item line and then combine them into the subtotal.
line_one = quantity_one * unit_price_one
line_two = quantity_two * unit_price_two
subtotal = line_one + line_two

# Tax is calculated from the item subtotal only.
tax_amount = subtotal * tax_percent / 100

# The delivery fee is added after the tax calculation.
final_total = subtotal + tax_amount + delivery_fee

# Display all money values with exactly two decimal places.
print()
print("=" * 48)
print("                PURCHASE QUOTE")
print("=" * 48)
print(f"{item_one:20} {quantity_one:3d} x {unit_price_one:8.2f} = {line_one:9.2f} TRY")
print(f"{item_two:20} {quantity_two:3d} x {unit_price_two:8.2f} = {line_two:9.2f} TRY")
print("-" * 48)
print(f"Subtotal:                         {subtotal:9.2f} TRY")
print(f"Tax ({tax_percent:.2f}%):                       {tax_amount:9.2f} TRY")
print(f"Delivery:                         {delivery_fee:9.2f} TRY")
print(f"FINAL TOTAL:                      {final_total:9.2f} TRY")
print("=" * 48)
