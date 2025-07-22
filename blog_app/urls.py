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
from .views import BlogView

urlpatterns = [
    path('blog', BlogView.as_view()),
    path('blog/<int:id>/', BlogView.as_view()),  
]