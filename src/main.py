from invoice import Invoice, LineItem
from pdf_export import export_invoice_pdf

def main():
    inv = Invoice(
        shop_name="Steve's Auto Repair",
        shop_address="917 US-117 South, Goldsboro, NC 27530",
        shop_phone="919-330-4110",
        customer_name=input("Customer name: ").strip(),
        vehicle=input("Vehicle (e.g., 2012 Jeep Compass): ").strip(),
        tax_rate=0.0  # change to 0.07 if you want 7% tax
    )

    print("\nAdd PARTS (blank description to stop)")
    while True:
        desc = input("Part description: ").strip()
        if not desc:
            break
        cost = float(input("Part cost: "))
        inv.parts.append(LineItem(desc, qty=1, unit_price=cost))

    print("\nAdd LABOR (blank description to stop)")
    while True:
        desc = input("Labor description: ").strip()
        if not desc:
            break
        hours = float(input("Hours: "))
        rate = float(input("Rate per hour: "))
        inv.labor.append(LineItem(desc, qty=hours, unit_price=rate))

    inv.recalculate()
    print(f"\nTOTAL: ${inv.total:.2f}")

    path = export_invoice_pdf(inv, output_dir="output")
    print(f"Saved PDF: {path}")

if __name__ == "__main__":
    main()
