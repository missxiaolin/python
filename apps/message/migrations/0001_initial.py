# Generated by Django 2.0.1 on 2018-01-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=100, verbose_name='联系地址')),
                ('message', models.CharField(max_length=500, verbose_name='留言信息')),
            ],
            options={
                'verbose_name': '用户留言信息',
            },
        ),
    ]
