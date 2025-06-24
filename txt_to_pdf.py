from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file, pdf_file):
    c = canvas.Canvas(pdf_file)
    with open(txt_file, 'r') as file:
        lines = file.readlines()

y = 800  # Starting y position for the text
for line in lines: # type: ignore
        c.drawString(100, y, line.strip()) # type: ignore
        y -= 20  # Move down for the next line

c.save() # type: ignore

txt_to_pdf('input.txt', 'output.pdf')