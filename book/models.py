from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    is_sub = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='categories'
        verbose_name = 'category'


class Book(models.Model):
    ACTIVE = 1
    COMING_SOON = 2
    FINISH = 3
    INACTIVE = 4

    STATUS_CHOICES = [
        (ACTIVE, "active"),
        (COMING_SOON, "coming soon"),
        (FINISH, "finish"),
        (INACTIVE, "in active"),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    published_date = models.DateField()
    price = models.PositiveBigIntegerField()
    image = models.ImageField()
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
