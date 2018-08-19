from django.db import models

# Create your models here.
class User(models.Model):
    uphone = models.CharField(max_length=11, verbose_name='电话')
    upwd = models.CharField(max_length=20, verbose_name='密码')
    uemail = models.EmailField(null=True, verbose_name='邮箱')
    uname = models.CharField(max_length=20, verbose_name='姓名')
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.uname
    class Meta:
        verbose_name_plural = '名字'

class GoodsType(models.Model):
    title = models.CharField(max_length=20, verbose_name='类型')
    picture = models.ImageField(upload_to='static/upload/goodstype')
    desc = models.CharField(max_length=100, verbose_name='描述')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '类型'

class Goods(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='价格')
    spec = models.CharField(max_length=50, verbose_name='规格')
    picture = models.ImageField(upload_to='static/upload/goods')
    isActive = models.BooleanField(default=True)
    goodsType = models.ForeignKey(GoodsType, null=True, verbose_name='类型')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '名称'