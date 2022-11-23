from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, titulo, vimeo_id):
        self.slug = slug
        self.title = title
        self.titulo = titulo
        self.id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('bituca', 'Cards - Bituquinha', 'Bituquinha', 770026394),
    Video('peek-inside', 'Cards - Peek Inside', 'Peek Inside', 774443580),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
