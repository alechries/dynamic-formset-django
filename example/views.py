from django.shortcuts import render
from django.forms import inlineformset_factory
from . import forms, models


def example_view(request):
    item = models.Item()
    AdditionFormset = inlineformset_factory(
        parent_model=models.Item,
        model=models.Addition,
        fields=('description', 'image')
    )

    if request.method == "POST":
        item_form = forms.ItemForm(request.POST, request.FILES, prefix='item')
        addition_formset = AdditionFormset(request.POST, request.FILES, instance=item, prefix='addition')

        if item_form.is_valid() and addition_formset.is_valid():
            item_form.save()
            addition_formset.save()

        else:
            print('[item] NOPE: ', item_form.errors or 'Not available')
            print('[addition] NOPE: ', addition_formset.errors or 'Not available')
    else:
        item_form = forms.ItemForm(instance=item, prefix='item')
        addition_formset = AdditionFormset(instance=item, prefix='addition')

    return render(
        request=request,
        template_name='example.html',
        context={
            'form': item_form,
            'formset': addition_formset,
        })
