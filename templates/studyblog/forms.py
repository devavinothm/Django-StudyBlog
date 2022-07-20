from django import forms
from .models import StudyBlog

class StudyBlogForm(forms.ModelForm):
	class Meta:
		model = StudyBlog
		fields="__all__"
