from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from . import forms, models
from django.http import HttpResponse


def example_view(request):

    models.Item.objects.order_by('id').delete()

    item = models.Item()
    addition_a_with_item_count = models.AdditionA.objects.filter(item=item).count()
    addition_b_with_item_count = models.AdditionB.objects.filter(item=item).count()
    AdditionAFormset = inlineformset_factory(
        parent_model=models.Item,
        model=models.AdditionA,
        fields=('name', 'count', 'count_type'),
        max_num=addition_a_with_item_count if addition_a_with_item_count > 0 else 3,
    )
    AdditionBFormset = inlineformset_factory(
        parent_model=models.Item,
        model=models.AdditionB,
        fields=('description', 'image'),
        max_num=addition_b_with_item_count if addition_b_with_item_count > 0 else 1,
    )

    alerts = []
    if request.method == "POST":

        item_form = forms.ItemForm(request.POST, request.FILES, prefix='item')
        addition_a_formset = AdditionAFormset(request.POST, request.FILES, instance=item, prefix='addition_a')
        addition_b_formset = AdditionBFormset(request.POST, request.FILES, instance=item, prefix='addition_b')

        if item_form.is_valid() and addition_a_formset.is_valid() and addition_b_formset.is_valid():

            item = item_form.save()
            addition_a_queryset = addition_b_formset.save(commit=False)
            addition_b_queryset = addition_b_formset.save(commit=False)

            for addition in addition_a_queryset:
                addition.item = item
                addition.save()
            for addition in addition_b_queryset:
                addition.item = item
                addition.save()

            alerts = ['Формы сохранены успешно!', ]

    else:

        item_form = forms.ItemForm(instance=item, prefix='item')
        addition_a_formset = AdditionAFormset(instance=item, prefix='addition_a')
        addition_b_formset = AdditionBFormset(instance=item, prefix='addition_b')

    return render(
        request, 'example.html',
        context={
            'item_form': item_form,
            'addition_a_formset': addition_a_formset,
            'addition_b_formset': addition_b_formset,
            'alerts': alerts,
        })


def add_addition_type_a_view(request):
    type_a_count = models.TypeA.objects.count()
    type_a = models.TypeA()
    type_a.name = f'Type {type_a_count}'
    type_a.save()
    return HttpResponse('')
