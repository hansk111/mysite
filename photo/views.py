from django.views.generic import ListView, DetailView
from photo.models import Album, Photo, Videos

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from config.views import OwnerOnlyMixin
from photo.forms import PhotoInlineFormSet
import ffmpeg
import sys
import requests

def upload_video(request):
     
    if request.method == 'POST': 
         
        title = request.POST['title']
        video = request.POST['video']
        video_path = 'videos/%Y/%m'
        image_path = 'videos/%Y/%m'
        time = '00:00:00.000'
        video_thumbnail = generate_thumbnail(video, video_thum)
        content = Videos(title=title,video=video,video_thumbnail=video_thumbnail)
        content.save()

        return redirect('videos_display')
     
    return render(request,'photo/video_upload.html')

def generate_thumbnail(in_filename, out_filename):
    probe = ffmpeg.probe(in_filename)
    time = float(probe['streams'][0]['duration']) // 2
    width = probe['streams'][0]['width']
    try:
        (
            ffmpeg
            .input(in_filename, ss=time)
            .filter('scale', width, -1)
            .output(out_filename, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)


def display(request):
     
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
     
    return render(request,'photo/videos_display.html',context)




class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo

#--- Create/Change-list/Update/Delete for Photo
class PhotoCV(LoginRequiredMixin, CreateView):
    login_url='common:login'
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
    login_url='common:login'
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUV(OwnerOnlyMixin, UpdateView):
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:album_list')


class PhotoDelV(OwnerOnlyMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:photo_change')


#--- Change-list/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    login_url='common:login'
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDelV(OwnerOnlyMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:album_list')


#--- (InlineFormSet) Create/Update for Album
class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    login_url='common:login'
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:album_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:album_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))