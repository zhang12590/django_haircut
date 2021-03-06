# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-19 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name_plural': '名称'},
        ),
        migrations.AlterModelOptions(
            name='goodstype',
            options={'verbose_name_plural': '类型'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '名字'},
        ),
        migrations.AddField(
            model_name='goods',
            name='goodsType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType', verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(max_length=50, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='title',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='goodstype',
            name='title',
            field=models.CharField(max_length=20, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uphone',
            field=models.CharField(max_length=11, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='user',
            name='upwd',
            field=models.CharField(max_length=20, verbose_name='密码'),
        ),
    ]
