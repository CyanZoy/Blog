from django.contrib import admin
from Wx.models import Fund


class FundAdmin(admin.ModelAdmin):
    list_display = ('fund_name', 'fund_code', 'colored_name', 'fund_update_time', 'fund_rise_fall',
                    'fund_invest', 'fund_pic_url')
    search_fields = ('fund_code', 'fund_name')


admin.site.register(Fund, FundAdmin)

