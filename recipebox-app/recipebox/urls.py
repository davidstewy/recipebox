"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from recipebox import views
from django.contrib import admin
from recipebox.views import index, recipe, author
from django.conf import settings
from django.urls import include, path
from recipebox.models import *
from recipebox.views import recipeadd, authoradd, login_view, signup_view

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>', views.recipe),
    path('author/<int:author_id>', views.author),
    path('recipeadd/', views.recipeadd),
    path('authoradd/', views.authoradd),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
