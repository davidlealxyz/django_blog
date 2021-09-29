# Generated by Django 3.2.3 on 2021-09-21 04:58

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=django.db.models.manager.BaseManager.get_queryset, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article'),
        ),
    ]