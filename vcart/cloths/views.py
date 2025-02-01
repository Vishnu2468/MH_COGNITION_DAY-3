from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404

# Create your views here.

from .models import cloths
def cloth(request):
    cloth=cloths.objects.all()
    return render(request,'cloths.html',{'cloth':cloth})


def cloth_delete(request, cloth_id):
    if request.method == 'POST':
        cloth = get_object_or_404(cloths, id=cloth_id)
        cloth.delete()
        
        return redirect('cloths')
    else:
        return redirect('cloths')



def cloth_add(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        category = request.POST.get('category')
        description = request.POST.get('description')
        size = request.POST.get('size')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        cloths.objects.create(
            brand=brand,
            category=category,
            description=description,
            size=size,
            price=price,
            stock=stock
        )
        return redirect('cloths')
    return render(request, 'cloths/cloth_form.html')


def cloth_edit(request, cloth_id):
    cloth = get_object_or_404(cloths, id=cloth_id)
    if request.method == 'POST':
        cloth.brand = request.POST.get('brand')
        cloth.category = request.POST.get('category')
        cloth.description = request.POST.get('description')
        cloth.size = request.POST.get('size')
        cloth.price = request.POST.get('price')
        cloth.stock = request.POST.get('stock')
        cloth.save()
        return redirect('cloths')
    return render(request, 'cloths/cloth_edit_form.html', {'cloth': cloth})