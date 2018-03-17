from django.db import models


class acc(models.Model):
    accesstoken = models.TextField()
    accesstoken_time = models.IntegerField()
    expires_in = models.CharField(max_length=5, default=None)

    class Meta:
        db_table = 'wx_acc'


