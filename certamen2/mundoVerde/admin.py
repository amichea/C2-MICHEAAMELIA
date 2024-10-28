from django.contrib import admin
from .models import *

admin.site.register(Producto)
admin.site.register(Carrito)

class PedidoCompletoFilter(admin.SimpleListFilter):
    title = 'Estado del Pedido'  # Título del filtro
    parameter_name = 'estaCompletado'

    def lookups(self, request, model_admin):
        return (
            ('completado', 'Completado'),
            ('pendiente', 'Pendiente'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'completado':
            return queryset.filter(estaCompletado=True)
        elif self.value() == 'pendiente':
            return queryset.filter(estaCompletado=False)
        return queryset

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'estaCompletado')  # Campos a mostrar
    list_filter = (PedidoCompletoFilter,)
