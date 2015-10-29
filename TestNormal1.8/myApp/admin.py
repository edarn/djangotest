from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] #specify the order
	fieldsets = [  #Divide into different sets. :)
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
	inlines = [ChoiceInline]
	
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)