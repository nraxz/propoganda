from django.contrib import admin
from .models import Case, People, Allegation, Category

admin.site.register(Case)
admin.site.register(People)
admin.site.register(Allegation)
admin.site.register(Category)

