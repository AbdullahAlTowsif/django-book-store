from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.

# function based view
# def home(request):
#     return render(request, 'home.html')

# class based view
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name': 'Rahim', 'age': 21}
        context.update(kwargs)
        return context

# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form': book})

# 1ST WAY TO ADD DATA BY FORM
# class BookFormView(FormView):
#     # we don't need to render the form. Django by default render the 'form' in FormView
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     # success_url = '/show_books/'
#     # success_url = reverse_lazy('show_books')
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save() # to save in database
#         return redirect('show_books')

# 2ND WAY TO ADD DATA 
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')

# def show_books(request):
#     book = BookStoreModel.objects.all()
#     return render(request, 'show_book.html', {'data': book})

class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    # ordering = ['author']
    # filtering in 2 way
    
    # 1st way
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='Jhankar Mahbub')
    
    # 2nd way
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'data': BookStoreModel.objects.filter(author='Towsif')}
    #     context = {'data': BookStoreModel.objects.order_by('author')}
    #     return context
    
    # conditional template view
    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = 'staff.html'
        else:
            template_name = self.template_name
        return [template_name]

class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance=book)
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('show_books')
#     return render(request, 'store_book.html', {'form': form})


class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')


# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk=id).delete()
#     return redirect('show_books')

class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_books')