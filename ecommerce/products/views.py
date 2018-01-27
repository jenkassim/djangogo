from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product


###
# Featured Objects View
##
class ProductFeaturedListView(ListView):
    template_name = "products/featured.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

###
# Product List View : (i) Class Base View /products
#                     (ii) Function Base View /products-fbv
###
class ProductListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# function base view below is equivalent to the class above
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

###
# Product Slug View : A substitute tag name
#       (i) Class Base View /products/<slug>
###
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()

    print(queryset)
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        print("slug:")
        print(slug)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found.. Go figure it out!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("wth...")
        return instance



###
# Product Detailed View : (i) Class Base View /products/<pk>
#                         (ii) Function Base View /products-fbv/<pk>
###
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesnt exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


# function base view below is equivalent to the class above
# all Django object by default has a primary key
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, id=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #         print('no product here')
    #         raise Http404("Product does not exists")
    # except:
    #     print('Everything else')

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesnt exist")
    # print(instance)
    # qs = Product.objects.filter(id=pk)

    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesnt exist")


    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)

