# This is the urls for function based view.

# blog_app/urls.py
# from django.urls import path
# from .views import blog_view, blog_update 

# urlpatterns = [
#     path('blog/', blog_view),  
#     path('blog/<int:id>/', blog_update),    
# ]

# This is the urls for class based view.


from django.urls import path
from .views.main_view import BlogView, category_view, category_update, categories_with_products, product_view, product_update, get_products_by_category
from .views.auth_view import register_user, login_user

urlpatterns = [
    path('blog', BlogView.as_view()),
    path('blog/<int:id>', BlogView.as_view()),  
    path('register', register_user),  
    path('login', login_user), 
    path('category', category_view),
    path('category/<int:id>', category_update),
    path('tokenRefresh', BlogView.as_view()),  
    path('product', product_view),  
    path('product/<int:id>', product_update), 
    path('category_id/<int:id>', get_products_by_category),
    path('categories/', categories_with_products),

]