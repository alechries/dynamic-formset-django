function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });

    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    newElement.find('.addition-counter').text(total);
    $(selector).after(newElement);

    height = document.body.scrollHeight;
    window.scrollTo(0, height);
}

function delForm(btn,) {

}