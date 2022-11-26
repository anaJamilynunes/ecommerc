from django.contrib import admin
from django.urls import path
from apliecommerce.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('sobrenos/', sobrenos, name="sobrenos"),
    path('detalhe/<int:id>', detalhe, name="detalhe"),
    path('maisprodutos/', maisprodutos, name="maisprodutos")
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

