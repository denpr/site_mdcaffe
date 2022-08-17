from django.shortcuts import render, redirect
from .models import Category, InformCategory
from .models import MenuItem
from .models import InformBlockMenuContent
from .forms import MessageForm

def index(request):
    elements = {}
    categories = Category.objects.order_by('position')
    
    for el in categories:
        items = MenuItem.objects.filter(category__title=el.title)
        if items:
            elements[el.title] = items
    
    left_block = {
        'title': InformCategory.objects.get(position=0).title,
        'content': InformBlockMenuContent.objects.filter(informCategory__title=InformCategory.objects.get(position=0).title)
    }
    rigth_block = {
        'title': InformCategory.objects.get(position=2).title,
        'content': InformBlockMenuContent.objects.filter(informCategory__title=InformCategory.objects.get(position=2).title)
    }
    
    context = {
        'title' : 'Home',
        'categories' : categories,
        'items': items,
        'elements': elements,
        'left_block': left_block,
        'right_block': rigth_block
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect('home')
        else:
            print('no valid form')
            return render(request, "main/contacts.html", {'form':form}) 
            
    form = MessageForm()
    context = {'form': form}
    return render(request, 'main/contacts.html', context)
