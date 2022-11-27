from django.shortcuts import render

from djangoprojectjfobatista.aperitivos.models import Video

videos = [
    Video(slug='bituca', title='Cards - Bituquinha', titulo='Bituquinha', vimeo_id='770026394'),
    Video(slug='peek-inside', title='Cards - Peek Inside', titulo='Peek Inside', vimeo_id='774443580'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
