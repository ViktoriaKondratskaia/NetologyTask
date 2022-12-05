from django.shortcuts import render
from django.http import HttpResponse


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    return HttpResponse('Добро пожаловать на страницу рецептов!')

DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },

        'pasta': {

            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },

        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1
         }
    }





def menu(request, recipe):
    recipe = DATA.get(recipe)
    servings = int(request.GET.get('servings', 1))
    print(servings)
    for ingredient in recipe.keys():
        recipe[ingredient] = recipe[ingredient] * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)








