from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

# Class Base View
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# function base view below is equivalent to the class above
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

# Class Base View
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# function base view below is equivalent to the class above
# all Django object by default has a primary key
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
