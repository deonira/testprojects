from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm, MediaFileForm
from .models import Book, MediaFile
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import BookForm,MediaFileForm


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'




class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = '/'
    login_url = 'login'



class HomePageView(TemplateView):
    template_name = 'home.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form} )


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 5
    template_name = 'book_list.html'

class MediaFileListView(ListView):
    model = MediaFile
    template_name = 'mediafile_list.html'
    context_object_name = '/'

class MediaFileCreateView(CreateView):
    model = MediaFile
    form_class = MediaFileForm
    template_name = 'mediafile_form.html'
    success_url = '/'

class PhotoListView(ListView):
    model = MediaFile
    template_name = 'photo_list.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return MediaFile.objects.filter(media_type='image')
