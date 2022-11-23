from django.shortcuts import render


def video(request, slug):
    videos = {
        'bituca': {
            'titulo': 'Bituquinha',
            'id': 770026394
        },
        'peek-inside': {
            'titulo': 'Peek Inside',
            'id': 774443580
        },

    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

