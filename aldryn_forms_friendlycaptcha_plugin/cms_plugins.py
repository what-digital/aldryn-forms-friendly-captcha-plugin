from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from aldryn_forms.cms_plugins import Field
from friendly_captcha.fields import FrcCaptchaField



class FriendlyCaptchaFieldPlugin(Field):
    name = _("FriendlyCaptcha Field")
    render_template = True
    allow_children = False
    form_field = FrcCaptchaField

    form_field_enabled_options = [
        'error_messages',
    ]
    fieldset_general_fields = []
    fieldset_advanced_fields = []

    def get_error_messages(self, instance) -> dict:
        return {
            'required': _(
                "There was a problem with FriendlyCaptcha. "
                "Please contact support if this problem persists."
            ),
        }


plugin_pool.register_plugin(FriendlyCaptchaFieldPlugin)
