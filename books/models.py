from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    score = models.PositiveSmallIntegerField()  # 회원 리뷰 평점(간단 정수)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Thread(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=100)
    content = models.TextField()
    read_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title