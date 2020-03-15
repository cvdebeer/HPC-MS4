from django import template
'''
The entire Search app was copied and adjusted for this project from a tutorial by codingforentrepeneurs.com - https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine/

An issue creating an "Related Field has invalid lookup: icontains" was resolved with the help of stack overflow- https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains
'''
register = template.Library()


@register.filter()
def class_name(value):
    return value.__class__.__name__
