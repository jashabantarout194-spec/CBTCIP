# payment_receipt.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(filename, store_name, customer_name, items, total_amount):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, store_name)

    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 80, "Payment Receipt")

    # Customer details
    c.drawString(50, height - 120, f"Customer: {customer_name}")

    # Items
    y_position = height - 160
    c.setFont("Helvetica", 12)
    for item, price in items.items():
        c.drawString(50, y_position, f"{item}: ₹{price}")
        y_position -= 20

    # Total
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position - 20, f"Total Amount: ₹{total_amount}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2, 50, "Thank you for your purchase!")

    # Save PDF
    c.save()

# Example usage
if __name__ == "__main__":
    items = {
        "Notebook": 120,
        "Pen": 20,
        "Bag": 450
    }
    total = sum(items.values())
    create_receipt("receipt.pdf", "ABC Store", "Jashabanta", items, total)
