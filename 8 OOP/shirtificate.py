from fpdf import FPDF
name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 36)
pdf.cell(190, 20, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", 40, 30, 133)
with pdf.local_context(text_color=(255, 255, 255)):
        pdf.cell(-185, 145, name + " CS50",align="C")
pdf.output("shirtificate.pdf")