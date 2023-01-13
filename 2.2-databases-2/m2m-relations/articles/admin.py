from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter_main_scope = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter_main_scope += 1
                else:
                    pass
            else:
                pass
            if counter_main_scope == 0:
                raise ValidationError('Укажите основной раздел')
            elif counter_main_scope > 1:
                raise ValidationError('Основным может быть только один раздел')
            return super().clean()

        #     # вызовом исключения ValidationError можно указать админке о наличие ошибки
        #     # таким образом объект не будет сохранен,
        #     # а пользователю выведется соответствующее сообщение об ошибке
        #     raise ValidationError('Тут всегда ошибка')
        # return super().clean()  # вызываем базовый код переопределяемого метода




class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]



@admin.register(Tag)
class Tag(admin.ModelAdmin):
    pass

