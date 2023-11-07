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

def omlet(request):
    res = {}
    servings = request.GET.get("servings", 1)
    for i, e in DATA['omlet'].items():
        res.update({i: e * int(servings)})
    context = {'recipe': res}
    return render(request, 'calculator/index.html', context)


def pasta(request):
    res = {}
    servings = request.GET.get("servings", 1)
    for i, e in DATA['pasta'].items():
        res.update({i: e * int(servings)})
    context = {'recipe': res}
    return render(request, 'calculator/index.html', context)


def buter(request):
    res = {}
    servings = request.GET.get("servings", 1)
    for i, e in DATA['buter'].items():
        res.update({i: e * int(servings)})
    context = {'recipe': res}
    return render(request, 'calculator/index.html', context)