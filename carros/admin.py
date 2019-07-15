from django.contrib import admin
from .models import Carro
#imports para a geracao do PDF
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django_object_actions import DjangoObjectActions

#Customizando o cabecalho da pagina no admin
admin.site.site_header = 'Garagem'

#Função que gera a ação de gerar o PDF com os carros selecionados
def gerar_pdf(modeladmin, request, carros):
    html_string = render_to_string('carros/pdf_template.html', {'obj':carros})
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/carros.pdf');
    fs = FileSystemStorage('/tmp')
    with fs.open('carros.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="carros.pdf"'
        return response

    return response

gerar_pdf.short_description = 'Gerar PDF dos carros selecionados'

#CarroAdmin permite que eu customize a página do Admin para adicionar filtros, search boxes, definir
#o campo usado para ordenação dos resultados a exibir e as ações personalizadas (por exemplo, a de gerar o PDF)
class CarroAdmin(DjangoObjectActions, admin.ModelAdmin):
    #Permitir a filtragem por marca, estado, e existencia ou não de AC, VE, e airbag
    list_filter = ['marca', 'estado','ar_condicionado','vidro_eletrico','airbag']
    #Permitir a busca por chassi ou modelo
    search_fields = ['chassi','modelo']
    #Ordenar resultados por marca
    ordering = ['marca']
    #Insere ação de gerar o PDF
    actions = [gerar_pdf]

admin.site.register(Carro, CarroAdmin)
