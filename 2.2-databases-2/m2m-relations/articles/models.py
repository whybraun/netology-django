from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Tag(models.Model):
    subject = models.CharField(max_length=200, verbose_name="name")
    article = models.ManyToManyField(Article, related_name="tag", through="ArticleTag")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class ArticleTag(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="scopes"
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="scopes")
    is_main = models.BooleanField(default=False)