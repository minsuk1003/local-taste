from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Rating(models.Model):
    rating = models.PositiveIntegerField()
    review = models.CharField(max_length=1000, blank=True, null=True)
    user_name = models.CharField(max_length=50)
    local_review_count = models.IntegerField(blank=True, null=True)
    total_review_count = models.IntegerField(blank=True, null=True)
    restaurant_num = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_num', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rating'


class Restaurant(models.Model):
    restaurant_num = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=1000, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    sun = models.CharField(max_length=45, blank=True, null=True)
    mon = models.CharField(max_length=45, blank=True, null=True)
    tue = models.CharField(max_length=45, blank=True, null=True)
    wed = models.CharField(max_length=45, blank=True, null=True)
    thu = models.CharField(max_length=45, blank=True, null=True)
    fri = models.CharField(max_length=45, blank=True, null=True)
    sat = models.CharField(max_length=45, blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    review_count = models.PositiveIntegerField(blank=True, null=True)
    image_link = models.CharField(max_length=3000, blank=True, null=True)
    local_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    normal_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    total_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    local_count = models.PositiveIntegerField(blank=True, null=True)
    normal_count = models.PositiveIntegerField(blank=True, null=True)
    map_image = models.CharField(max_length=3000, blank=True, null=True)
    local_word_image = models.CharField(max_length=3000, blank=True, null=True)
    normal_word_image = models.CharField(max_length=3000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'restaurant'
