#coding=utf-8
from django.shortcuts import render, get_object_or_404
from tagging.models import Tag
from endless_pagination.decorators import page_template
from aion.gide.models import Pages

# Список старниц родителя, страница
@page_template('pages/_page.html')
def detail(request, slug, template='pages/childrens.html', extra_context=None):
    page = get_object_or_404(Pages, slug=slug)
    if page.is_leaf_node():
        template = 'pages/detail.html'
    context = {
        'page': page,
        'pages': page.get_children(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)


# Главная страница
def main(request, template='pages/children_main.html'):
    context = {
        'list_page': Pages.objects.extra(where=["rght = lft + 1"]).filter(status=2).order_by('-up_date')
    }
    return render(request, template, context)

#Теги
def list_tags(request):
    return render(request, 'tags/tag_cloud.html', {'tags': Tag.objects.all()})
