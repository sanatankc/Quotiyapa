from django.contrib import admin
from .models import Quotes
# Register your models here.
class QuotesAdmin(admin.ModelAdmin):
    model = Quotes
    list_display = ('get_quotes', 'author', 'user')

admin.site.register(Quotes, QuotesAdmin)