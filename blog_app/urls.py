# blog_app/urls.py
from django.urls import path
from .views import blog_view, blog_update 

urlpatterns = [
    path('blog/', blog_view),  
    path('blog/<int:id>/', blog_update),    
]
