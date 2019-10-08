import random

from django_jinja import library


@library.filter
def add_classname(field, classname):
    attrs = field.field.widget.attrs
    attrs["class"] = attrs.get('class', '') + ' ' + classname
    return field.as_widget(attrs=attrs)


@library.filter
def add_placeholder(field, placeholder):
    attrs = field.field.widget.attrs
    attrs['placeholder'] = placeholder
    return field


@library.filter
def shuffle(items):
    items = list(items)
    random.shuffle(items)
    return items
