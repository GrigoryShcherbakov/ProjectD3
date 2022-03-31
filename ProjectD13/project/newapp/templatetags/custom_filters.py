from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает,

# заменяет слова "жесть", "афигенно", "круто" на слово "здорово" (для рабочего примера: первая стать, 10 слово)
@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("жесть", "ЗДОРОВО")
    value = value.replace("афигенно", "ЗДОРОВО")
    value = value.replace("круто", "ЗДОРОВО")
    return value
