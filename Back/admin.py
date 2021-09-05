from django.contrib import admin

# Register your models here.
from .models import Category,Project,Value,Work,Blog

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Value)
admin.site.register(Work)
admin.site.register(Blog)
