from django.conf import settings
from django.forms import Widget
from django.utils import translation
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from aldryn_forms.cms_plugins import Field
from friendly_captcha.fields import FrcCaptchaField

from django.conf import settings


class FriendlyCaptchaWidget(Widget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_key = getattr(settings, 'FRC_CAPTCHA_SITE_KEY', None)
        self.frc_widget_module_js = getattr(
            settings, 'FRC_WIDGET_MODULE_JS',
            'https://unpkg.com/friendly-challenge@0.9.11/widget.module.min.js',
        )
        self.frc_widget_js = (
            settings, 'FRC_WIDGET_JS',
            'https://unpkg.com/friendly-challenge@0.9.11/widget.min.js'
        )

    def render(self, name, value, attrs=None, renderer=None):
        attrs['data-lang'] = translation.get_language()
        attrs['data-sitekey'] = self.site_key
        attrs['data-solution-field-name'] = name
        attrs['class'] = 'frc-captcha'
        final_attrs = self.build_attrs(attrs)
        frc_js = mark_safe(
            f'<script type="module" src="{self.frc_widget_module_js}" async defer></script>'
            f'<script nomodule src="{self.frc_widget_js}" async defer></script>'
        )
        return format_html('<div {}></div>{}', flatatt(final_attrs), frc_js)



class FriendlyCaptchaFieldPlugin(Field):
    name = _("FriendlyCaptcha Field")
    render_template = True
    allow_children = False
    form_field = FrcCaptchaField
    form_field_widget = FriendlyCaptchaWidget

    form_field_enabled_options = [
        'error_messages',
    ]
    fieldset_general_fields = []
    fieldset_advanced_fields = []

    def get_form_field_kwargs(self, instance):
        kwargs = super().get_form_field_kwargs(instance)
        kwargs['label'] = ''
        return kwargs

    def get_error_messages(self, instance) -> dict:
        return {
            'required': _(
                "There was a problem with FriendlyCaptcha. "
                "Please contact support if this problem persists."
            ),
        }


plugin_pool.register_plugin(FriendlyCaptchaFieldPlugin)
