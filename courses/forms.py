from django import forms

from courses.models import Course_Review


class CourseReviewForm(forms.ModelForm):
    class Meta:
        model=Course_Review
        fields = ('rating', 'comments',)

    # Appling css class to the field and button
    def __init__(self, *args, **kwargs):
        super(CourseReviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        # self.helper = FormHelper()
        # self.helper.add_input(Submit('submit', 'Create Account', css_class='genric-btn success circle'))


