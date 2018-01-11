from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .models import Articolo


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
                          (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []


    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


@admin.register(Articolo)
class ArticoloAdmin(ImageWidgetAdmin):

    def image_tag(self, obj):
        if not obj.image:
            return format_html('<img src="" width="130"/>')
        return format_html('<img src="{}" width="130"/>'.format(obj.image.url))


    image_tag.short_description = 'Image'

    list_display = ('image_tag', 'id', 'nome', 'ean', 'descrizione', 'prezzo')

    list_display_links = ('image_tag', 'id', 'nome', 'ean', 'descrizione', 'prezzo')

    search_fields = ('image_tag', 'id', 'nome', 'ean', 'descrizione', 'prezzo')

    image_fields = ('image')
