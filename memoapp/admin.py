from django.contrib import admin
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin
from memoapp.models import Memo


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Memo, PostAdmin)