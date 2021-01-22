from django.contrib import admin
from .models import Question, Answer, Randomized
# Register your models here.

admin.site.register(Question),
admin.site.register(Answer),
admin.site.register(Randomized),
