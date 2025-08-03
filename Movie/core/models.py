from django.db import models
from django.contrib.auth.models import User

class Movielist(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Reviews(models.Model):
    movie =models.ForeignKey(Movielist,on_delete=models.CASCADE, related_name='reviews')
    # reviewer=models.CharField(max_length=100)
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.reviewer} -> {self.rating}"

