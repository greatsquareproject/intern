from django.shortcuts import render, redirect
from  . models import seller,buyer, products
from . forms import ProductForm
import datetime

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def index(request):
    pro = products.objects.all()
    slr = seller.objects.all()
    return render(request,'index.html',{'products':pro,'seller':slr})

def buy(request,pk):
    pro = products.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])
        
        by = buyer(name=name,address=address,phone=phone)
        by.save()
        amount = float(pro.price)
        pn = pro.name
        dis = pro.dis
        price = amount
        pro_quantity =quantity
        pro_total = amount*quantity         
        slr = seller.objects.all()
        data = {'pname':pn,'pprice':price,'bname':name,'baddress':address,'bphone':phone,'pdis':dis,'pquantity':pro_quantity, 'ptotal':pro_total}
        return render(request, 'pdf.html', {'data': data, 'seller': slr})

    return render(request, 'buy.html')


def pdf(request):
    slr = seller.objects.all()
    return render(request,'pdf.html',{'seller':slr})

