from django import template


register = template.Library()

@register.filter(name='censor')
def currency(value):
    value = value.split()
    for i in range(len(value)):
        if value[i][:5] == 'редиск':
            value[i] = 'р'+ '*'*(len(value[i])-1)
        elif value[i][:5] == 'Редиск':
            value[i] = 'Р'+ '*'*(len(value[i])-1)
        elif value[i][:5] == 'больш':
            value[i] = 'б' + '*' * (len(value[i]) - 1)
        elif value[i][:5] == 'Больш':
            value[i] = 'Б' + '*' * (len(value[i]) - 1)
    value = ' '.join(value)
    return value