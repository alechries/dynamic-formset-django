function delForm(btn, selector, type) {
    $(btn).parents(selector).remove();
    var forms = $(selector);
    $('#id_' + type + '-TOTAL_FORMS').val(forms.length);
    for (var i=0, formCount=forms.length; i<formCount; i++) {
        element = $(forms.get(i));
        element.find(':input').each(function() {
            var id_regex = new RegExp('(' + type + '-\\d+)');
		    var replacement = type + '-' + i;
		    var name = $(this).attr('name').replace(id_regex,replacement);
		    var id = 'id_' + name;
             $(this).attr({'name': name, 'id': id}).val('');
        });
        element.find('.addition-counter').text(i+1);
    }
    return false;
}

function addForm(selector, type) {
    let newElement = $(selector).clone(true);
    let total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find(':input').each(function() {
        let name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        let id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });

    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);

    newElement.find('.addition-counter').each(function() { $(this).text(total); });



    newElement.find('.del-row').click(function() {
        return delForm(this, '.addition-form-part', 'addition');
    });

    $(selector).after(newElement);

    height = document.body.scrollHeight;
    window.scrollTo(0, height);
}