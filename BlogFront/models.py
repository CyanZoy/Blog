from django.db import models


class NoteName(models.Model):
    """
    @ Create by CyanZoy on 2018/3/24 16:07
    @ Describe: 用来存放不同笔记名
    """
    name = models.CharField('笔记本名', max_length=255, default=None)
    creat_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        # verbose_name = '笔记本'
        verbose_name_plural = '笔记本'
        app_label = 'BlogFront'


class NoteT(models.Model):
    """
    @ Create by CyanZoy on 2018/3/24 16:14
    @ Describe: 用来存放笔记-
    """
    # 此条笔记的编号
    note_num = models.CharField(max_length=150)
    note_user = models.CharField(max_length=255, default=None)
    creat_time = models.DateTimeField(auto_now_add=True)
    note_title = models.CharField(max_length=255, default=None)
    note_label = models.CharField(max_length=20, default=None)
    belong = models.ForeignKey(NoteName, related_name='belong_name', on_delete=models.SET_NULL, null=True)


class NoteInfo(models.Model):
    # 笔记编号
    note_info_num = models.CharField(max_length=150)
    # 笔记顺序号
    note_info_sign = models.IntegerField()
    # 笔记的标题
    note_info_title = models.CharField(max_length=100, default=None)
    # 笔记的代码片
    note_info_code = models.TextField()
    # 笔记的图片路径
    note_info_img = models.CharField(max_length=50, default=None)
