# Generated by Django 3.1.7 on 2021-08-02 09:29

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='board.category')),
            ],
            options={
                'ordering': ['tree_id', 'lft'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('head_image', models.ImageField(blank=True, null=True, upload_to='board/images/%Y/%m')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL)),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.category')),
                ('voter', models.ManyToManyField(blank=True, related_name='voter_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comment', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post')),
                ('voter', models.ManyToManyField(related_name='voter_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
