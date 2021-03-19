from django.shortcuts import render
from django.forms import inlineformset_factory
from . import forms, models


def example_view(request):

    item = models.Item()
    addition_with_item_count = models.Addition.objects.filter(item=item).count()
    AdditionFormset = inlineformset_factory(
        parent_model=models.Item,
        model=models.Addition,
        fields=('description', 'image'),
        min_num=addition_with_item_count,
        max_num=addition_with_item_count,
    )

    if request.method == "POST":

        item_form = forms.ItemForm(request.POST, request.FILES, prefix='item')
        addition_formset = AdditionFormset(request.POST, request.FILES, instance=item, prefix='addition')

        if item_form.is_valid() and addition_formset.is_valid():

            item = item_form.save()
            addition_queryset = addition_formset.save(commit=False)

            for addition in addition_queryset:
                addition.item = item
                addition.save()

    else:

        item_form = forms.ItemForm(instance=item, prefix='item')
        addition_formset = AdditionFormset(instance=item, prefix='addition')

    return render(
        request, 'example.html',
        context={
            'form': item_form,
            'formset': addition_formset,
        })