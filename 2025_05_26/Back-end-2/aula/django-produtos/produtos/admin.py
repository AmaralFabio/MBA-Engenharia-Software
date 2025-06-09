from django.contrib import admin

# Register your models here.
from .models import Produto

admin.site.site_header = "Administração de Produtos"
admin.site.register(Produto)