import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_invoice_pdf(inv, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"invoice_{inv.invoice_number}.pdf"
    path = os.path.join(output_dir, filename)

    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    y = height - 60
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, inv.shop_name)

    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, inv.shop_address)
    y -= 14
    c.drawString(50, y, inv.shop_phone)

    y -= 28
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Invoice #: {inv.invoice_number}")
    y -= 16
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Customer: {inv.customer_name}")
    y -= 14
    c.drawString(50, y, f"Vehicle: {inv.vehicle}")

    y -= 26
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Description")
    c.drawString(420, y, "Amount")

    def draw_items(title, items, y):
        y -= 16
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, title)
        y -= 14
        c.setFont("Helvetica", 10)
        for it in items:
            c.drawString(50, y, f"{it.description} ({it.qty:g} @ ${it.unit_price:.2f})")
            c.drawRightString(520, y, f"${it.total:.2f}")
            y -= 14
        return y

    y = draw_items("Parts", inv.parts, y)
    y = draw_items("Labor", inv.labor, y)

    y -= 10
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(520, y, f"Subtotal: ${inv.subtotal:.2f}")
    y -= 14
    c.drawRightString(520, y, f"Tax: ${inv.tax:.2f}")
    y -= 14
    c.drawRightString(520, y, f"Total: ${inv.total:.2f}")

    c.showPage()
    c.save()
    return path
