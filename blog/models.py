from django.db import models

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(
        'Category',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=64,
        verbose_name='Title'
    )
    text = models.TextField(
        verbose_name='Text'
    )
    created_date = models.DateTimeField(
        verbose_name='Created Date',
        auto_now_add=True,
    )
    publish_date = models.DateTimeField(
        verbose_name='Publish Date',
    )
    published = models.BooleanField(
        default=False,
    )
    author = models.ForeignKey(
        "auth.User",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    @property
    def rating(self):
        return self.feedbacks.aggregate(models.Avg('rating')).get('rating__avg')

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    text = models.TextField(
        verbose_name='Text'
    )
    publish_date = models.DateTimeField(
        verbose_name='Publish Date',
    )

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.text}"

class Category(models.Model):

    text = models.CharField(
        max_length=48,
        verbose_name='text'
    )
    def __str__(self):
        return f'{self.text}'


class Feedback(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Text'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    rating = models.IntegerField(
        verbose_name='Rating',
        default=3
    )

    def __str__(self):
        return
