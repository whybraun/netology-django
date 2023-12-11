from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import forms, BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        tags_list = []
        for form in self.forms:
            if form.cleaned_data:
                if form.cleaned_data["is_main"]:
                    count += 1
                if "tag_name" in form.cleaned_data:
                    if form.cleaned_data["tag_name"] not in tags_list:
                        tags_list.append(form.cleaned_data["tag_name"])
                    else:
                        raise ValidationError(
                            f"Тег {form.cleaned_data['tag_name']} указан больше одного раза !!!"
                        )
            else:
                print("empty dict() !!!!!!!!")
        if count == 0:
            raise ValidationError("Основной раздел не указан!")
        if count >= 2:
            raise ValidationError("Основной раздел может быть один!")
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "text",
        "published_at",
        "image",
    ]
    inlines = [
        ArticleTagInline,
    ]
    list_filter = ["published_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "subject"]