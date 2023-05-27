from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Cart
from . handlers import bot
# Create your views here.
def main_page(request):
    product_info = Product.objects.all()

    category_info = Category.objects.all()

    context = {'product': product_info, 'categories': category_info}

    return render(request, 'index.html', context)

def get_full_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'exact_product.html', context)

def get_full_category(request, pk):
    category = Category.objects.filter(name=pk)

    context = {'category': category}
    return render(request, 'exact_category.html', context)

def user_cart(request):
    cart = Cart.objects.filter(user_id= request.user.id)
    if request .method == 'POST':
        main_text = 'Новый заказ\n\n'
        for i in cart:
            main_text += f'Товар: {i.user_product}\n' \
                         f'Количество: {i.user_product_quantity}'
            bot.send_message(736169495, main_text)
            cart.delete()
            return  redirect('/')
    return  render(request, 'user_cart.html', {'cart':cart})
