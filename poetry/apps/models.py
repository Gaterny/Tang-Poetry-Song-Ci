from django.db import models

# Create your models here.


# 宋词
class Poems(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author_id = models.PositiveIntegerField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)
    author = models.CharField(max_length=150)

    class Meta:
        db_table = 'poems'

    def __str__(self):
        return self.title


# 宋词作者
class PoemsAuthor(models.Model):
    name = models.CharField(max_length=150)
    intro_l = models.TextField(blank=True, null=True)
    intro_s = models.TextField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'poems_author'


# 唐诗
class Poetry(models.Model):
    title = models.CharField(max_length=150)
    yunlv_rule = models.TextField()
    author_id = models.PositiveIntegerField()
    content = models.TextField()
    dynasty = models.CharField(max_length=10)
    author = models.CharField(max_length=150)

    class Meta:
        db_table = 'poetry'


# 唐诗作者
class PoetryAuthor(models.Model):
    name = models.CharField(max_length=150)
    intro = models.TextField(blank=True, null=True)
    dynasty = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'poetry_author'
