from django.db import models
from django.utils.html import format_html

class acc(models.Model):
    accesstoken = models.TextField()
    accesstoken_time = models.IntegerField()
    expires_in = models.CharField(max_length=5, default=None)

    class Meta:
        db_table = 'wx_acc'


class Fund(models.Model):
    """基金信息类"""
    # 基金的名称
    fund_name = models.CharField('基金名', max_length=50)
    # 基金的代码
    fund_code = models.IntegerField('基金代码')
    # 是否爬取此基金
    fund_get_state = models.BooleanField('是否获取', default=0)
    # 基金更新时间 auto_now_add 只添加一次， auto_now 每次更改都会更新时间
    fund_update_time = models.DateTimeField('更新时间', auto_now=True)
    # 基金涨跌率
    fund_rise_fall = models.FloatField('预估涨跌率', max_length=5, default=0, blank=True)
    # 该基金的投资额
    fund_invest = models.FloatField('投资额', max_length=5, default=0, blank=True)
    # 该基金的图片url
    fund_pic_url = models.CharField('图片地址', max_length=255, default=None, blank=True)

    def colored_name(self):
        name = '你好'
        if self.fund_get_state:
            return format_html(
                '<span style="color: #00868B;">获取</span>',
            )
        else:
            return format_html(
                '<span style="color: #FF3030;">不获取</span>',
            )

    class Meta:
        verbose_name = '基金'
        db_table = 'wx_Fund'
        verbose_name_plural = '基金'

