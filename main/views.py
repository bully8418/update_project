from .models import *
from .forms import ProductForm, UserRegisterForm, UserLoginForm
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic import ListView,  CreateView


class HomeTasks(ListView):
    model = Task
    template_name = 'main/html/base.html'
    context_object_name = 'tasks'
    paginate_by = 4


class TaskCategory(ListView):
    model = Task
    template_name = 'main/html/base.html'
    context_object_name = 'tasks'
    paginate_by = 4

    def get_queryset(self):
        return Task.objects.filter(category_id=self.kwargs['category_id'])


class ByCategory(ListView):
    model = Category
    template_name = 'main/html/category.html'
    context_object_name = 'cat'


class DevicesList(ListView):
    model = Task
    template_name = 'main/html/base.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(device_id=self.kwargs['device_id'])


def delete_cart(request, pk):
    if request.method == 'POST':
        products = OrderItem.objects.get(id=pk)
        products.delete()
        orders = Order.objects.all()
        customer = Customer.objects.all()
        for item in orders, customer:
            if item:
                del item
        return redirect('cart')

    return render(request, 'main/html/cart_view.html')


def delete_full_cart(request):
    products = OrderItem.objects.all()
    products.delete()
    return render(request, 'main/html/base.html')


class AddProduct(CreateView):
    form_class = ProductForm
    template_name = 'main/html/products.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно прошли регистрацию')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/html/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/html/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class Search(ListView):
    template_name = 'main/html/search.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        return Task.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super() .get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


def product(request, pk):
    product = Task.objects.get(id=pk)

    if request.method == 'POST':
        product = Task.objects.get(id=pk)
        # Get user account information
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()

        return redirect('cart')

    context = {'product': product}
    return render(request, 'main/html/single.html', context)


def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    context = {'order': order}
    return render(request, 'main/html/cart_view.html',  context)


def test(request):
    return render(request, 'main/html/test.html')
