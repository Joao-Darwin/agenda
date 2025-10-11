from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',) # Colunas que serão mostradas na tabela no /admin
    ordering = ('id',) # Coluna de ordenação padrão
    list_filter = ('created_at',) # Filtros disponíveis
    search_fields = ('id', 'first_name', 'last_name',) # Colunas de pesquisas disponíveis
    list_per_page = 10 # Quant de 'linhas' por página na tabela