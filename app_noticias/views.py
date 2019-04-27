from django.shortcuts import render
from django.views.generic import ListView
from .models import Noticia, Tag
from django.http import HttpResponse


class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

def noticias_resumo(request):
    total = Noticia.objects.count()
    html = """
    <html>
    <body>
    <h1>Resumo</h1>
    <p>A quantidade total de notícias é {}.</p>
    </body>
    </html>
    """.format(total)
    return HttpResponse(html)

def noticias_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total': total})

def noticias_detalhes(request, noticia_id):
    try:
        noticia = Noticia.objects.get(id = noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})

'''def noticias_slug(request, tag_nome):
    tag = Tag.objects.get(nome = tag_nome)'''

#implementar uma consulta pelo slug, pela tag dela