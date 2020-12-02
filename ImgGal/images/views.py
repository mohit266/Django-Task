from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image
from taggit.models import Tag
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'images/home.html')


def All_Images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            form.save_m2m()
        return redirect('success')
    else:
        form = ImageForm()

    return render(request, 'images/allimages.html', {'form':form})

def display_images(request):
    dis_images = Image.objects.all()
    print(dis_images)
    page = request.GET.get('page',1)
    paginator = Paginator(dis_images,8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
            
    return render(request, 'images/display_images.html', {'users':users})


def success(request):
    return  render(request, 'images/success.html')