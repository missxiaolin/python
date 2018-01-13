# Generated by Django 2.0.1 on 2018-01-12 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2)),
                ('learn_time', models.IntegerField(default=0, verbose_name='学习时长（分）')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
    ]