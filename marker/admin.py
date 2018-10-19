from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
from django.utils.translation import ugettext_lazy

class MyClearableFileInput(forms.ClearableFileInput):
    clear_checkbox_label = ugettext_lazy('Delete')

class MarkerAdmin(admin.ModelAdmin):

#    fields = ('thumbnail','marker_image','target_name','width','asset_bundle','manifest')
    readonly_fields = ('marker_thumnail',)

    def marker_thumnail(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.marker_image.url,
            width=50,
            height=50,
        )
        )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.marker_image.url))

    def ios_asset_bundle_tag(self, obj):
        if not obj.ios_asset_bundle:
            return "-"
        else:
            return "ok"

    def ios_manifest_tag(self, obj):
        if not obj.ios_manifest:
            return "-"
        else:
            return "ok"

    def android_asset_bundle_tag(self, obj):
        if not obj.android_asset_bundle:
            return "-"
        else:
            return "ok"

    def android_manifest_tag(self, obj):
        if not obj.android_manifest:
            return "-"
        else:
            return "ok"

    image_tag.short_description = 'Marker(JPG)'
    ios_asset_bundle_tag.short_description = 'ios_AssetBundle'
    ios_asset_bundle_tag.short_description = 'ios_Manifest'

    list_display = ('image_tag', 'target_name','width', 'ios_asset_bundle_tag', 'ios_manifest_tag', 'android_asset_bundle_tag', 'android_manifest_tag', 'date_modified')

#    formfield_overrides = {
#        models.FileField: {'widget': MyClearableFileInput},
#    }

admin.site.register(Marker,MarkerAdmin)




