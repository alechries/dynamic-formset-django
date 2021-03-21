function delForm(btn, prefix, form, counter) {
    $(btn).parents(form).remove();
    let forms = $(form);
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);

    for (var i=0, formCount=forms.length; i<formCount; i++) {
        element = $(forms.get(i));
        element.find(':input').each(function() {
            let id_regex = new RegExp('(' + prefix + '-\\d+)');
		    let replacement = prefix + '-' + i;
		    let name = $(this).attr('name').replace(id_regex,replacement);
		    let id = 'id_' + name;
             $(this).attr({'name': name, 'id': id}).val('');
        });
        element.find(counter).text(i+1);
    }
    return false;
}

function addForm(prefix, form, counter, deleter) {
    let selector = form + ":last";
    let newElement = $(selector).clone(true);
    let total = $('#id_' + prefix + '-TOTAL_FORMS').val();

    newElement.find(':input').each(function() {
        let name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        let id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    if (counter) newElement.find(counter).each(function() { $(this).text(total); });
    $(selector).after(newElement);

    height = document.body.scrollHeight;
    window.scrollTo(0, height);
}