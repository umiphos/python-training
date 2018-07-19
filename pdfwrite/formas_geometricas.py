from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("pdfs/formas_geometricas.pdf", pagesize=A4)

c.drawString(30, h - 50, "Línea")
x = 120
y = h - 45
# X punto inicio, Y punto inicio, X punto fin, Y punto fin
c.line(x, y, x + 100, y)

c.drawString(30, h - 100, "Rectángulo")
# X punto de inicio, Y punto de inicio, ancho, alto
c.rect(x, h - 120, 100, 50)

c.drawString(30, h - 170, "Círculo")
# X punto centro, Y punto centro, radio
c.circle(170, h - 165, 20)

c.drawString(30, h - 240, "Elipse")
# X punto inicio, Y punto inicio, X punto fin, Y punto fin
c.ellipse(x, y - 170, x + 100, y - 220)

c.showPage()
c.save()