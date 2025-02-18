from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Category, Product
from company.models import Company

class ProductDetailView(DetailView):
    queryset = Product.available.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = Company.objects.all().first()
        return context


class ProductListView(ListView):
    category = None
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.available.all()

        category_slug = self.kwargs.get('slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = Company.objects.all().first()
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context
