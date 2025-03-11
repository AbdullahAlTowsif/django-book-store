from django.urls import path
# from book.views import home, store_book, show_books, edit_book, delete_book
from . import views
urlpatterns = [
    # rendering home.html template without any function view | class view
    # path('', views.TemplateView.as_view(template_name='home.html'), name="homepage"),
    
    # rendering home.html using class based view
    # path('', views.MyTemplateView.as_view(template_name='home.html'), name="homepage"),
    # path('<int:roll>/', views.MyTemplateView.as_view()),
    path('', views.MyTemplateView.as_view()),
    
    # path('store_new_book/', views.store_book, name="store_book"),
    path('store_new_book/', views.BookFormView.as_view(), name="store_book"),
    # path('show_books/', views.show_books, name="show_books"),
    path('show_books/', views.BookListView.as_view(), name="show_books"),
    path('book_details/<int:id>/', views.BookDetailsView.as_view(), name="book_details"),
    path('edit_book/<int:id>', views.edit_book, name="edit_book"),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
    
    # path('', home),
    # path('store_new_book/', store_book, name="store_book"),
    # path('show_books/', show_books, name="show_books"),
    # path('edit_book/<int:id>', edit_book, name="edit_book"),
    # path('delete_book/<int:id>', delete_book, name="delete_book"),
]
