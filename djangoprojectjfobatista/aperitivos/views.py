from django.shortcuts import render


videos = [
    {
        'slug': 'bituca',
        'title': 'Cards - Bituquinha',
        'titulo': 'Bituquinha',
        'id': 770026394
    },
    {
        'slug': 'peek-inside',
        'title': 'Cards - Peek Inside',
        'titulo': 'Peek Inside',
        'id': 774443580
    },
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

