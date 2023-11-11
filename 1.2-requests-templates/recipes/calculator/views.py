from django.shortcuts import render

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
        'помидор, ломтик': 1,
    },
}

def dish_view(request, dish):
    res = {}
    servings = int(request.GET.get('servings', 1))
    if dish in DATA:
        ingredients = DATA[dish]
        for i, e in ingredients.items():
            res.update({i: e * int(servings)})
    context = {'recipe': res}
    return render(request, 'calculator/index.html', context)