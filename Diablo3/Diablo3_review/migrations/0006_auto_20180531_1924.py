# Generated by Django 2.0.2 on 2018-05-31 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Diablo3_review', '0005_auto_20180530_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myarticle',
            name='comm',
        ),
        migrations.AddField(
            model_name='commentaire',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='Diablo3_review.MyArticle'),
            preserve_default=False,
        ),
    ]
