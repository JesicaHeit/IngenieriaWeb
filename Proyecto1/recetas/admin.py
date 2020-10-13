from django.contrib import admin
from .models import Comment, Reports, Receta

admin.site.register(Comment)
admin.site.register(Reports)

def bloquear_receta(modeladmin,request,queryset):
	queryset.update(state = 2)
bloquear_receta.description = "Bloquear receta"

class RecetaAdmin(admin.ModelAdmin):
	actions = [bloquear_receta]

admin.site.register(Receta,RecetaAdmin)

# Register your models here.
