# Taxes
compra = float(input("Ingrese el total de la compra: "))
tax_county = 0.02
tax_state = 0.04
county_tax = compra * tax_county
state_tax = compra * tax_state
total_tax = county_tax + state_tax
print(f"El impuesto del condado es: {county_tax:.2f}")
print(f"El impuesto del estado es: {state_tax:.2f}")
print(f"El impuesto total es: {total_tax:.2f}")
total = compra + total_tax
print(f"El total a pagar es: {total:.2f}")