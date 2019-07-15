from django.contrib import admin
from .models import Carro
import io
from reportlab.pdfgen import canvas
from django.http import FileResponse

admin.site.site_header = 'Garagem'

def muda_estado(modeladmin, request, carros):
    carros.update(estado = 'ZK')
muda_estado.short_description = "Tornar Zero Km"

def gerar_pdf(modeladmin, request, carros):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    for carro in carros:
        pdf.drawString(100,100,carro.chassi)
    pdf.showPage()
    pdf.save()
    return FileResponse(buffer, as_attachment=True, filename="carros.pdf")


class CarroAdmin(admin.ModelAdmin):
    list_filter = ['estado']
    ordering = ['marca']
    actions = [muda_estado,gerar_pdf]

admin.site.register(Carro, CarroAdmin)
