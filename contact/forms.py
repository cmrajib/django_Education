from django.contrib.auth.forms import UserCreationForm
from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = ('name','email', 'subject','comment')

    # Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'single-input'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Create Account', css_class='genric-btn success circle'))


