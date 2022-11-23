from django.shortcuts import render


def video(request, slug):
    video = {
        'titulo': 'Bituquinha',
        'id': '58479'
    }
    return render(request, 'aperitivos/video.html', context={'video': video})

