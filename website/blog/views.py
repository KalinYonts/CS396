from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import *
from .forms import CommentForm, AddForm, SaleForm, AddHealthForm
from datetime import datetime
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from cal.views import CalendarView
from cal.models import Event
from django.db.models import Q
from django.contrib import messages

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content', 'file']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def shopping(request):
    products = Product.objects.all().order_by('-id')

    return render(request,
                'blog/shopping.html',
                {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 
                 'blog/product_detail.html',
                 {'product': product})

def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price   
            new_sale.save()
            #To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt') 

    return render (request, 'blog/issue_item.html',
        {
    'sales_form': sales_form,
    })


def add_to_stock(request, pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
           #To add to the remaining stock quantity is reducing
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            return redirect('shopping')

    return render (request, 'blog/add_to_stock.html', {'form': form})

def receipt(request): 
    sales = Sale.objects.all().order_by('-id')
    return render(request,'blog/receipt.html',{'sales': sales})

def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'blog/receipt_detail.html', {'receipt': receipt})

def all_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'blog/all_sales.html',
     {
     'sales': sales, 
     'total': total,
     'change': change, 
     'net': net,
      })

def health(request):
    health = Health.objects.all().order_by('-id')
    return render(request, 'blog/health.html', {'health': health})

def add_health(request):
    form = AddHealthForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Health.objects.create(
                doctor_name = Doctor.objects.get(id=request.POST['doctor_name']),
                phone = request.POST.get('phone'),
                email = request.POST.get('email'),
                prescriptions = request.POST.get('prescriptions'),
                dose = request.POST.get('dose'),
                dosetime = request.POST.get('dosetime'))
            messages.success(request, f'Your Information was added successfully.')
        return redirect('health')
    return render(request, 'blog/addHealth.html', {'form': form})

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list

